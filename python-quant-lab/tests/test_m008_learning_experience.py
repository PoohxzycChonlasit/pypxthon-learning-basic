"""M008 learner-navigation and isolated first-use regression checks."""

import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))
DA_MODULES = {
    **{f"DA{i:02}": ("foundations.py", "grade_foundations.py") for i in range(1, 6)},
    **{f"DA{i:02}": ("numpy_practice.py", "grade_numpy_pandas.py") for i in range(6, 10)},
    **{f"DA{i:02}": ("pandas_practice.py", "grade_numpy_pandas.py") for i in range(10, 18)},
    "DA18": ("visualization.py", "grade_visualization.py"),
    "DA19": ("visualization.py", "grade_visualization.py"),
    "DA20": ("capstone.py", "grade_capstone.py"),
    "DA21": ("capstone.py", "grade_capstone.py"),
    "DA22": ("pandas_practice.py", "grade_numpy_pandas.py"),
    "DA23": ("plotly_extension.py", "grade_plotly_optional.py"),
}


def markdown_targets(path):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)\s]+)(?:\s+[^)]*)?\)", text):
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("//"):
            continue
        relative = unquote(parsed.path)
        if not relative:
            continue
        yield target, (path.parent / relative).resolve()


def isolated_project(destination):
    shutil.copytree(
        ROOT,
        destination,
        ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", "*.pyc", "progress.json", "docs.rar"
        ),
    )


def cli(project, *args):
    return subprocess.run(
        [sys.executable, "-X", "utf8", "-B", "practice.py", *args],
        cwd=project,
        text=True,
        encoding="utf-8",
        capture_output=True,
        timeout=20,
        check=False,
    )


class M008LearningExperienceTests(unittest.TestCase):
    def test_all_core_exercises_have_individual_lessons_and_real_destinations(self):
        self.assertEqual(len(CURRICULUM), 150)
        self.assertEqual(len({exercise["id"] for exercise in CURRICULUM}), 150)
        for exercise in CURRICULUM:
            exercise_id = exercise["id"]
            lesson = ROOT / exercise["lesson_file"]
            self.assertTrue(lesson.is_file(), exercise_id)
            text = lesson.read_text(encoding="utf-8")
            for heading in (
                "เรียนรู้อะไร",
                "ก่อนเริ่ม",
                "ตัวอย่างสั้น",
                "งานของคุณ",
                "เขียนคำตอบที่ไหน",
                "ข้อมูลเข้าและผลลัพธ์",
                "ถ้าไม่ผ่าน",
                "เสร็จเมื่อ",
            ):
                self.assertIn(heading, text, f"{exercise_id}: {heading}")
            if exercise["submission_mode"] == "text_answer":
                answer_path = exercise["answer_file"]
                self.assertTrue((ROOT / answer_path).is_file(), exercise_id)
                self.assertIn("../" + answer_path, text, exercise_id)
                self.assertIn(f"practice.py check {exercise_id}", text, exercise_id)
                section = text.split("## 8. ตรวจคำตอบด้วย Check", 1)[1].split(
                    "## 9.", 1
                )[0]
                self.assertNotIn(f"practice.py run {exercise_id}", section, exercise_id)
                self.assertIn("ไม่ต้องกด VS Code Run Python File", section, exercise_id)
            else:
                path = (
                    f"exercises/level_{exercise['level']:02d}/"
                    f"{exercise_id}.py"
                )
                self.assertTrue((ROOT / path).is_file(), f"{exercise_id}: {path}")
                self.assertIn(f"practice.py run {exercise_id}", text, exercise_id)
                self.assertIn(f"practice.py check {exercise_id}", text, exercise_id)

    def test_level_overviews_link_exactly_fifteen_exercises_in_order(self):
        for level in range(1, 11):
            overview = ROOT / "lessons" / f"level_{level:02}.md"
            text = overview.read_text(encoding="utf-8")
            listed = re.findall(r"\[(L\d{2}-E\d{3}) —", text)
            expected = [
                exercise["id"]
                for exercise in CURRICULUM
                if exercise["level"] == level
            ]
            self.assertEqual(listed, expected, overview.name)
            for exercise in (e for e in CURRICULUM if e["level"] == level):
                line = next(line for line in text.splitlines() if exercise["id"] in line)
                destination = (
                    exercise["answer_file"]
                    if exercise["submission_mode"] == "text_answer"
                    else (
                        f"exercises/level_{level:02d}/"
                        f"{exercise['id']}.py"
                    )
                )
                self.assertIn(f"../{destination}", line, exercise["id"])
            if level > 1:
                self.assertIn(f"level_{level - 1:02}.md", text)
            if level < 10:
                self.assertIn(f"level_{level + 1:02}.md", text)

    def test_data_analysis_pages_map_all_twenty_three_ids_to_six_modules(self):
        self.assertEqual(len(DA_MODULES), 23)
        readme = ROOT / "tracks" / "data_analysis" / "README.md"
        readme_text = readme.read_text(encoding="utf-8")
        for number in range(1, 24):
            exercise_id = f"DA{number:02}"
            module, grader = DA_MODULES[exercise_id]
            page = ROOT / "tracks" / "data_analysis" / "lessons" / f"{exercise_id}.md"
            self.assertTrue(page.is_file(), exercise_id)
            text = page.read_text(encoding="utf-8")
            self.assertIn(exercise_id, readme_text)
            self.assertIn(f"tracks/data_analysis/exercises/{module}", text)
            self.assertIn(f"-p {grader} -k {exercise_id}", text)
            self.assertIn("ข้อมูลที่ใช้", text)
            self.assertIn("เสร็จเมื่อ", text)
            source = (
                ROOT / "tracks" / "data_analysis" / "exercises" / module
            ).read_text(encoding="utf-8")
            self.assertRegex(source, rf"def\s+\w+")
            self.assertIn(f"def {re.search(r'def (\w+)\(', text).group(1)}(", source)

    def test_text_answer_lessons_do_not_reveal_known_prediction_outputs(self):
        by_id = {exercise["id"]: exercise for exercise in CURRICULUM}
        for exercise_id in ("L01-E002", "L01-E012", "L08-E002"):
            exercise = by_id[exercise_id]
            page = (ROOT / exercise["lesson_file"]).read_text(encoding="utf-8")
            expected = exercise["expected"].strip()
            self.assertNotIn(expected, page, exercise_id)
        level_08 = (ROOT / "lessons" / "level_08.md").read_text(encoding="utf-8")
        self.assertNotIn(by_id["L08-E002"]["expected"], level_08)

    def test_function_signatures_and_assessment_variants_remain_in_catalog_contract(self):
        assessment_count = 0
        for exercise in CURRICULUM:
            if exercise["submission_mode"] == "function":
                path = (
                    ROOT
                    / "exercises"
                    / f"level_{exercise['level']:02d}"
                    / f"{exercise['id']}.py"
                )
                tree = ast.parse(path.read_text(encoding="utf-8"))
                function = next(
                    node
                    for node in tree.body
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and node.name == exercise["function"]
                )
                args = function.args
                actual = [
                    arg.arg
                    for arg in args.posonlyargs + args.args + args.kwonlyargs
                ]
                expected = [
                    name.strip()
                    for name in exercise["signature"].split(",")
                    if name.strip()
                ]
                self.assertEqual(actual, expected, exercise["id"])
            if exercise.get("assessment"):
                assessment_count += 1
                for variant in ("A", "B"):
                    case_path = (
                        ROOT
                        / "tests"
                        / "assessment"
                        / f"{exercise['id']}-{variant}.json"
                    )
                    self.assertTrue(case_path.is_file(), case_path)
                    self.assertTrue(
                        json.loads(case_path.read_text(encoding="utf-8")),
                        case_path,
                    )
                    solution_path = (
                        ROOT
                        / "solutions"
                        / "assessment"
                        / f"{exercise['id']}-{variant}.py"
                    )
                    self.assertTrue(solution_path.is_file(), solution_path)
        self.assertEqual(assessment_count, 10)

    def test_changed_documentation_navigation_links_resolve(self):
        paths = [
            ROOT / "README.md",
            ROOT / "docs" / "submission-types.md",
            ROOT / "docs" / "vscode-beginner-guide.md",
            *sorted((ROOT / "lessons").glob("*.md")),
            ROOT / "tracks" / "data_analysis" / "README.md",
            *sorted((ROOT / "tracks" / "data_analysis" / "lessons").glob("*.md")),
        ]
        broken = []
        for path in paths:
            for target, resolved in markdown_targets(path):
                if not resolved.exists():
                    broken.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual(broken, [])

    def test_first_use_and_text_answer_workflow_in_temporary_copy(self):
        with tempfile.TemporaryDirectory(prefix="m008-smoke-") as temporary:
            project = Path(temporary) / "python-quant-lab"
            isolated_project(project)
            self.assertFalse((project / "progress.json").exists())

            listed = cli(project, "list", "--level", "1")
            self.assertEqual(listed.returncode, 0, listed.stderr)
            rows = [
                line
                for line in listed.stdout.splitlines()
                if re.match(r"L01-E\d{3}\s", line)
            ]
            self.assertEqual(len(rows), 15)
            self.assertTrue(
                any("answers\\level_01\\L01-E002.txt" in row or
                    "answers/level_01/L01-E002.txt" in row for row in rows)
            )

            plain_list = subprocess.run(
                [sys.executable, "-B", "practice.py", "list", "--level", "1"],
                cwd=project,
                capture_output=True,
                timeout=20,
            )
            self.assertEqual(plain_list.returncode, 0, plain_list.stderr)
            help_text = cli(project, "help").stdout
            self.assertIn("VS Code Run", help_text)
            self.assertIn("check ตรวจทุกกรณี", help_text)

            started = subprocess.run(
                [sys.executable, "-B", "practice.py", "start"],
                cwd=project,
                capture_output=True,
                timeout=20,
            )
            self.assertEqual(started.returncode, 0, started.stderr)
            progress_path = project / "progress.json"
            self.assertTrue(progress_path.is_file())

            spec = importlib.util.spec_from_file_location(
                "m008_temp_practice", project / "practice.py"
            )
            practice = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(practice)
            original_argv = sys.argv[:]
            try:
                for exercise_id in ("L01-E001", "L01-E002"):
                    captured = io.StringIO()
                    with patch.object(practice.subprocess, "Popen") as popen:
                        sys.argv = ["practice.py", "open", exercise_id]
                        with contextlib.redirect_stdout(captured):
                            practice.main()
                        self.assertTrue(popen.called)
                    self.assertIn(exercise_id, captured.getvalue())
                    if exercise_id == "L01-E002":
                        call_text = repr(popen.call_args)
                        self.assertIn("L01-E002.txt", call_text)
                        self.assertIn("L01-E002.md", call_text)
                        self.assertIn("L01-E002.md", captured.getvalue())
                        self.assertIn("ไม่ต้องรันไฟล์ Python", captured.getvalue())
            finally:
                sys.argv = original_argv

            first_file = project / "exercises" / "level_01" / "L01-E001.py"
            first_file.write_text("", encoding="utf-8")
            unfinished = cli(project, "check", "L01-E001")
            self.assertIn("FAIL", unfinished.stdout)
            first_answer = 'print("สวัสดี Python")\n'
            first_file.write_text(first_answer, encoding="utf-8")
            correct = cli(project, "check", "L01-E001")
            self.assertIn("PASS", correct.stdout)

            text_path = project / "answers" / "level_01" / "L01-E002.txt"
            original_text_answer = text_path.read_text(encoding="utf-8")
            run_hash = hashlib.sha256((project / "progress.json").read_bytes()).hexdigest()
            run_text = cli(project, "run", "L01-E002")
            self.assertIn("ไม่ต้องเขียนหรือรันโปรแกรม Python", run_text.stdout)
            self.assertIn("L01-E002.txt", run_text.stdout)
            self.assertIn("check L01-E002", run_text.stdout)
            self.assertEqual(
                run_hash, hashlib.sha256((project / "progress.json").read_bytes()).hexdigest()
            )
            for exercise in (
                entry for entry in CURRICULUM
                if entry["submission_mode"] == "text_answer"
            ):
                legacy = (
                    project
                    / "exercises"
                    / f"level_{exercise['level']:02d}"
                    / f"{exercise['id']}.py"
                )
                redirected = subprocess.run(
                    [sys.executable, "-X", "utf8", "-B", str(legacy)],
                    cwd=project,
                    text=True,
                    encoding="utf-8",
                    capture_output=True,
                    timeout=10,
                )
                self.assertEqual(redirected.returncode, 0, exercise["id"])
                self.assertIn(exercise["id"], redirected.stdout)
                self.assertIn(exercise["answer_file"].split("/")[-1], redirected.stdout)
                self.assertIn("check", redirected.stdout.lower())

            text_path.write_text("wrong\nanswer\n", encoding="utf-8")
            failed = cli(project, "check", "L01-E002")
            self.assertIn("FAIL", failed.stdout)
            expected = next(e for e in CURRICULUM if e["id"] == "L01-E002")["expected"]
            text_path.write_text(expected, encoding="utf-8")
            passed = cli(project, "check", "L01-E002")
            self.assertIn("PASS", passed.stdout)

            student_text = text_path.read_bytes()
            student_code = first_file.read_bytes()
            hinted = cli(project, "hint", "L01-E002", "1")
            self.assertIn("คำใบ้", hinted.stdout)
            revealed = cli(project, "solution", "L01-E002", "--yes")
            self.assertEqual(revealed.returncode, 0, revealed.stderr)
            final_check = cli(project, "check", "L01-E002")
            self.assertIn("PASSED_WITH_HELP", final_check.stdout)
            self.assertEqual(text_path.read_bytes(), student_text)
            self.assertEqual(first_file.read_bytes(), student_code)

            saved = json.loads(progress_path.read_text(encoding="utf-8"))
            self.assertEqual(
                saved["exercises"]["L01-E002"]["status"], "PASSED_WITH_HELP"
            )
            self.assertEqual(saved["exercises"]["L01-E002"]["attempts"], 3)


if __name__ == "__main__":
    unittest.main()
