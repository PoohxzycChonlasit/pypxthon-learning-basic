"""Offline integrity checks for the bundled curriculum. Run: python -m unittest discover -s tests."""
import importlib.util
import json
import os
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from materialize_level1 import write_student

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalize(value):
    if isinstance(value, (list, tuple)):
        return [normalize(x) for x in value]
    if isinstance(value, dict):
        return {str(k): normalize(v) for k, v in value.items()}
    return value


class LabIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))

    def test_catalog_completeness_and_links(self):
        ids = [e["id"] for e in self.curriculum]
        self.assertEqual(len(ids), 150)
        self.assertEqual(len(set(ids)), 150)
        known = set(ids)
        for ex in self.curriculum:
            level = f"level_{ex['level']:02d}"
            self.assertTrue((ROOT / "exercises" / level / f"{ex['id']}.py").is_file(), ex["id"])
            self.assertTrue((ROOT / "solutions" / level / f"{ex['id']}.py").is_file(), ex["id"])
            self.assertTrue((ROOT / "explanations" / f"{ex['id']}.md").is_file(), ex["id"])
            self.assertTrue((ROOT / ex["lesson_file"]).is_file(), ex["id"])
            if ex["level"] == 1:
                self.assertTrue((ROOT / "lessons" / f"{ex['id']}.md").is_file(), ex["id"])
            else:
                self.assertTrue((ROOT / "lessons" / f"level_{ex['level']:02d}.md").is_file(), ex["id"])
            hints = json.loads((ROOT / "hints" / f"{ex['id']}.json").read_text(encoding="utf-8"))
            self.assertEqual(len(hints), 3, ex["id"])
            cases = ex["cases"]
            if ex.get("assessment"):
                cases = json.loads((ROOT / "tests" / "assessment" / "L01-E015-A.json").read_text(encoding="utf-8"))
                self.assertTrue((ROOT / "tests" / "assessment" / "L01-E015-B.json").is_file())
            self.assertGreaterEqual(len(cases), 1, ex["id"])
            self.assertTrue(all(p in known for p in ex["prerequisites"]), ex["id"])
            self.assertTrue(ex["assessment"] if ex["id"].endswith("E015") else True)

    def test_all_reference_solutions_satisfy_all_cases(self):
        for ex in self.curriculum:
            if ex["level"] == 1:
                solution_path = ROOT / "solutions" / "level_01" / f"{ex['id']}.py"
                oracle_path = ROOT / "tests" / f"{ex['id']}.json"
                base_cases = json.loads(oracle_path.read_text(encoding="utf-8")) if oracle_path.is_file() else ex["cases"]
                variants = [(None, base_cases)]
                if ex.get("assessment"):
                    variants = [(v, json.loads((ROOT / "tests" / "assessment" / f"{ex['id']}-{v}.json").read_text(encoding="utf-8"))) for v in ("A", "B")]
                for variant, cases in variants:
                    path = solution_path if variant is None else ROOT / "solutions" / "assessment" / f"{ex['id']}-{variant}.py"
                    if ex["submission_mode"] == "text_answer":
                        answer_path = ROOT / "solutions" / "level_01" / f"{ex['id']}.txt"
                        answer = answer_path.read_text(encoding="utf-8").rstrip("\n")
                        self.assertEqual(answer, cases[0]["expected"], ex["id"])
                    elif ex["submission_mode"] == "literal":
                        answer = runpy.run_path(str(path))["ANSWER"]
                        self.assertEqual(answer, cases[0]["expected"], ex["id"])
                    else:
                        for case in cases:
                            result = subprocess.run([sys.executable, "-X", "utf8", "-I", str(path)], input=case.get("stdin", ""), text=True, encoding="utf-8", capture_output=True, timeout=4)
                            self.assertEqual(result.returncode, 0, f"{ex['id']} {variant}: {result.stderr}")
                            self.assertEqual(result.stdout.replace("\r\n", "\n"), case["expected_stdout"], f"{ex['id']} {variant} {case['name']}")
            elif ex.get("submission_mode") == "text_answer":
                answer_path = ROOT / "solutions" / f"level_{ex['level']:02d}" / f"{ex['id']}.txt"
                answer = answer_path.read_text(encoding="utf-8").rstrip("\n")
                cases = json.loads((ROOT / "tests" / f"{ex['id']}.json").read_text(encoding="utf-8"))
                for case in cases:
                    self.assertEqual(answer, case["expected"], ex["id"])
            elif ex.get("submission_mode") == "stdout":
                solution_path = ROOT / "solutions" / f"level_{ex['level']:02d}" / f"{ex['id']}.py"
                cases = json.loads((ROOT / "tests" / f"{ex['id']}.json").read_text(encoding="utf-8"))
                for case in cases:
                    result = subprocess.run(
                        [sys.executable, "-X", "utf8", "-I", str(solution_path)],
                        input=case.get("stdin", ""), text=True, encoding="utf-8", capture_output=True, timeout=4
                    )
                    self.assertEqual(result.returncode, 0, f"{ex['id']}: {result.stderr}")
                    self.assertEqual(result.stdout.replace("\r\n", "\n"), case["expected_stdout"], ex["id"])
            else:
                module = load(ROOT / "solutions" / f"level_{ex['level']:02d}" / f"{ex['id']}.py")
                fn = getattr(module, ex["function"])
                cases = json.loads((ROOT / "tests" / f"{ex['id']}.json").read_text(encoding="utf-8"))
                for case in cases:
                    got = normalize(fn(*case["args"], **case.get("kwargs", {})))
                    expected = normalize(case["expected"])
                    self.assert_values_close(got, expected, case.get("tolerance", 1e-8), ex["id"])

    def test_starters_are_unfinished(self):
        for ex in self.curriculum:
            path = ROOT / "exercises" / f"level_{ex['level']:02d}" / f"{ex['id']}.py"
            if ex["level"] == 1:
                if ex["submission_mode"] == "text_answer":
                    answer_path = ROOT / ex["answer_file"]
                    self.assertNotEqual(answer_path.read_text(encoding="utf-8").strip(), ex["cases"][0]["expected"], ex["id"])
                elif ex["submission_mode"] == "literal":
                    self.assertNotEqual(runpy.run_path(str(path)).get("ANSWER"), ex["cases"][0]["expected"], ex["id"])
                else:
                    cases = ex["cases"]
                    if ex.get("assessment"):
                        cases = json.loads((ROOT / "tests" / "assessment" / f"{ex['id']}-A.json").read_text(encoding="utf-8"))
                    else:
                        oracle_path = ROOT / "tests" / f"{ex['id']}.json"
                        if oracle_path.is_file():
                            cases = json.loads(oracle_path.read_text(encoding="utf-8"))
                    self.assertTrue(any(subprocess.run([sys.executable, "-X", "utf8", "-I", str(path)], input=c.get("stdin", ""), text=True, encoding="utf-8", capture_output=True, timeout=4).stdout.replace("\r\n", "\n") != c["expected_stdout"] for c in cases), ex["id"])
            elif ex.get("submission_mode") == "text_answer":
                answer_path = ROOT / ex["answer_file"]
                self.assertNotEqual(answer_path.read_text(encoding="utf-8").strip(), ex["cases"][0]["expected"], ex["id"])
            elif ex.get("submission_mode") == "stdout":
                oracle_path = ROOT / "tests" / f"{ex['id']}.json"
                cases = json.loads(oracle_path.read_text(encoding="utf-8")) if oracle_path.is_file() else ex["cases"]
                results = [
                    subprocess.run(
                        [sys.executable, "-X", "utf8", "-I", str(path)], input=case.get("stdin", ""),
                        text=True, encoding="utf-8", capture_output=True, timeout=4
                    )
                    for case in cases
                ]
                self.assertTrue(
                    any(result.returncode != 0 or result.stdout.replace("\r\n", "\n") != case["expected_stdout"]
                        for result, case in zip(results, cases)), ex["id"]
                )
            else:
                module = load(path)
                with self.assertRaises(NotImplementedError, msg=ex["id"]):
                    getattr(module, ex["function"])(*ex["cases"][0]["args"])

    def test_cli_rejects_deliberately_wrong_submission_for_all_exercises(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "lab"
            shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "progress.json"))
            progress = {
                "exercises": {
                    ex["id"]: {
                        "status": "PASSED_INDEPENDENTLY", "attempts": 1, "hints": [], "solution_viewed": False,
                        "assessment_variant": "A", "revealed_assessments": [], "hinted_assessments": [],
                        "assessment_results": {"A": "PASSED_INDEPENDENTLY"}, "assessment_verified": True,
                    }
                    for ex in self.curriculum
                }
            }
            (dest / "progress.json").write_text(json.dumps(progress), encoding="utf-8")

            for ex in self.curriculum:
                if ex["submission_mode"] == "text_answer":
                    target = dest / ex["answer_file"]
                    target.write_text("__deliberately_wrong__", encoding="utf-8")
                elif ex["submission_mode"] == "function":
                    target = dest / "exercises" / f"level_{ex['level']:02d}" / f"{ex['id']}.py"
                    target.write_text(
                        f"def {ex['function']}(*args, **kwargs):\n    return None\n",
                        encoding="utf-8",
                    )
                else:
                    target = dest / "exercises" / f"level_{ex['level']:02d}" / f"{ex['id']}.py"
                    target.write_text('print("__deliberately_wrong__")\n', encoding="utf-8")

                result = subprocess.run(
                    [sys.executable, "-X", "utf8", "practice.py", "check", ex["id"]],
                    cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8,
                )
                self.assertEqual(result.returncode, 0, f"{ex['id']}: {result.stdout} {result.stderr}")
                self.assertIn("NEEDS_REVIEW", result.stdout, f"{ex['id']}: {result.stdout} {result.stderr}")
                progress_now = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
                progress_now["exercises"][ex["id"]]["status"] = "PASSED_INDEPENDENTLY"
                if ex.get("assessment"):
                    progress_now["exercises"][ex["id"]]["assessment_verified"] = True
                (dest / "progress.json").write_text(json.dumps(progress_now), encoding="utf-8")

    def test_levels_two_through_ten_have_five_workflows_and_assessment_variants(self):
        mode_by_category = {
            "เขียนโค้ด": "function",
            "ทำนายผล": "text_answer",
            "เติมโค้ด": "stdout",
            "แก้โค้ดที่ผิด": "stdout",
            "โจทย์ประยุกต์": "stdout",
        }
        for level in range(2, 11):
            exercises = [e for e in self.curriculum if e["level"] == level and e["id"].endswith(tuple(f"E{i:03d}" for i in range(1, 6)))]
            by_category = {e["category"]: e for e in exercises}
            self.assertEqual(set(by_category), set(mode_by_category), f"level {level}")
            for category, mode in mode_by_category.items():
                self.assertEqual(by_category[category]["submission_mode"], mode, by_category[category]["id"])

            assessment_id = f"L{level:02d}-E015"
            assessment = next(e for e in self.curriculum if e["id"] == assessment_id)
            self.assertTrue(assessment["assessment"])
            self.assertNotEqual(assessment["variant_prompts"]["A"], assessment["variant_prompts"]["B"])
            for variant in ("A", "B"):
                fixture = ROOT / "tests" / "assessment" / f"{assessment_id}-{variant}.json"
                solution = ROOT / "solutions" / "assessment" / f"{assessment_id}-{variant}.py"
                self.assertTrue(fixture.is_file(), assessment_id)
                self.assertTrue(solution.is_file(), assessment_id)
                cases = json.loads(fixture.read_text(encoding="utf-8"))
                self.assertGreaterEqual(len(cases), 3, assessment_id)
                module = load(solution)
                fn = getattr(module, assessment["function"])
                for case in cases:
                    got = normalize(fn(*case["args"], **case.get("kwargs", {})))
                    expected = normalize(case["expected"])
                    self.assert_assessment_values(got, expected, f"{assessment_id}-{variant}")

    def test_cli_checks_each_added_format_and_each_assessment_variant(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "lab"
            shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "progress.json"))
            progress = {e["id"]: {"status": "PASSED_INDEPENDENTLY", "attempts": 1, "hints": [], "solution_viewed": False} for e in self.curriculum}
            progress["L01-E015"]["assessment_verified"] = True
            for level in range(2, 11):
                aid = f"L{level:02d}-E015"
                progress[aid] = {
                    "status": "PASSED_INDEPENDENTLY", "attempts": 1, "hints": [], "solution_viewed": False,
                    "assessment_variant": "A", "revealed_assessments": [], "hinted_assessments": [],
                    "assessment_results": {"A": "PASSED_INDEPENDENTLY"}, "assessment_verified": True,
                }
            (dest / "progress.json").write_text(json.dumps({"exercises": progress}), encoding="utf-8")

            def run_cli(*args):
                return subprocess.run(
                    [sys.executable, "-X", "utf8", "practice.py", *args], cwd=dest,
                    capture_output=True, text=True, encoding="utf-8", timeout=8
                )

            level1_student = dest / "exercises" / "level_01" / "L01-E008.py"
            level1_student.write_text("print(5)\n", encoding="utf-8")
            level1_hidden_cases = run_cli("check", "L01-E008")
            self.assertIn("NEEDS_REVIEW", level1_hidden_cases.stdout, "L01-E008")

            for level in range(2, 11):
                for number in range(1, 6):
                    ex = next(e for e in self.curriculum if e["id"] == f"L{level:02d}-E{number:03d}")
                    if number == 2 and level == 2:
                        wrong_prediction = run_cli("check", ex["id"])
                        self.assertIn("NEEDS_REVIEW", wrong_prediction.stdout, ex["id"])
                        self.assertNotIn(ex["cases"][0]["expected"], wrong_prediction.stdout, ex["id"])
                    if ex["submission_mode"] == "text_answer":
                        target = dest / ex["answer_file"]
                        source = dest / "solutions" / f"level_{level:02d}" / f"{ex['id']}.txt"
                    else:
                        target = dest / "exercises" / f"level_{level:02d}" / f"{ex['id']}.py"
                        source = dest / "solutions" / f"level_{level:02d}" / f"{ex['id']}.py"
                    # A student answer that hardcodes public cases must fail the hidden oracle.
                    if ex["id"] == "L02-E006":
                        target.write_text(
                            "def keep_nonzero_readings(values):\n"
                            "    if values == [0, 3, 0, -2, 5]:\n"
                            "        return [3, -2, 5]\n"
                            "    return []\n",
                            encoding="utf-8",
                        )
                        hidden_case_check = run_cli("check", ex["id"])
                        self.assertIn("NEEDS_REVIEW", hidden_case_check.stdout, ex["id"])
                    shutil.copy2(source, target)
                    if ex["id"] == "L02-E001":
                        ran = run_cli("run", ex["id"])
                        self.assertEqual(ran.returncode, 0, f"{ex['id']}: {ran.stdout} {ran.stderr}")
                        self.assertTrue(ran.stdout.strip(), ex["id"])
                    checked = run_cli("check", ex["id"])
                    self.assertIn("PASSED_INDEPENDENTLY", checked.stdout, f"{ex['id']}: {checked.stdout} {checked.stderr}")

            # Exercise the level-aware solution path for both source and text formats.
            for ex_id in ("L02-E003", "L08-E002"):
                revealed = run_cli("solution", ex_id, "--yes")
                self.assertEqual(revealed.returncode, 0, f"{ex_id}: {revealed.stdout} {revealed.stderr}")
                self.assertTrue(revealed.stdout.strip())

            progress_now = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
            for level in range(2, 11):
                aid = f"L{level:02d}-E015"
                progress_now["exercises"][aid] = {
                    "status": "NOT_STARTED", "attempts": 0, "hints": [], "solution_viewed": False,
                    "assessment_variant": "A", "revealed_assessments": [], "hinted_assessments": [],
                    "assessment_results": {}, "assessment_verified": False,
                }
            (dest / "progress.json").write_text(json.dumps(progress_now), encoding="utf-8")

            for level in range(2, 11):
                aid = f"L{level:02d}-E015"
                assessment = next(e for e in self.curriculum if e["id"] == aid)
                student = dest / "exercises" / f"level_{level:02d}" / f"{aid}.py"
                solution_a = dest / "solutions" / "assessment" / f"{aid}-A.py"
                wrong_assessment = run_cli("check", aid)
                self.assertIn("NEEDS_REVIEW", wrong_assessment.stdout, aid)
                assessment_expected = next(e for e in self.curriculum if e["id"] == aid)["variant_expected"]["A"]
                self.assertNotIn(assessment_expected, wrong_assessment.stdout, aid)
                shutil.copy2(solution_a, student)
                passed_a = run_cli("check", aid)
                self.assertIn("PASSED_INDEPENDENTLY", passed_a.stdout, f"{aid}-A: {passed_a.stdout} {passed_a.stderr}")
                progress_now = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
                self.assertTrue(progress_now["exercises"][aid]["assessment_verified"], aid)

                reassess = run_cli("retry", aid)
                self.assertIn("variant ใหม่: B", reassess.stdout, aid)
                assessment_expected = next(e for e in self.curriculum if e["id"] == aid)["variant_expected"]["B"]
                self.assertNotIn(assessment_expected, reassess.stdout, aid)
                # On variant B, an implementation keyed only to all A cases must fail.
                cases_a = json.loads((dest / "tests" / "assessment" / f"{aid}-A.json").read_text(encoding="utf-8"))
                table = {
                    json.dumps([case["args"], case.get("kwargs", {})], sort_keys=True): case["expected"]
                    for case in cases_a
                }
                student.write_text(
                    "import json\n"
                    f"TABLE = {table!r}\n"
                    f"def {assessment['function']}(*args, **kwargs):\n"
                    "    key = json.dumps([list(args), kwargs], sort_keys=True)\n"
                    "    return TABLE.get(key, {})\n",
                    encoding="utf-8",
                )
                wrong_variant_b = run_cli("check", aid)
                self.assertIn("NEEDS_REVIEW", wrong_variant_b.stdout, aid)
                assessment_expected = next(e for e in self.curriculum if e["id"] == aid)["variant_expected"]["B"]
                self.assertNotIn(assessment_expected, wrong_variant_b.stdout, aid)
                shutil.copy2(dest / "solutions" / "assessment" / f"{aid}-B.py", student)
                passed_b = run_cli("check", aid)
                self.assertIn("PASSED_INDEPENDENTLY", passed_b.stdout, f"{aid}-B: {passed_b.stdout} {passed_b.stderr}")
                progress_now = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
                self.assertTrue(progress_now["exercises"][aid]["assessment_verified"], aid)

    def assert_assessment_values(self, actual, expected, label):
        if isinstance(expected, dict):
            self.assertEqual(set(actual), set(expected), label)
            for key in expected:
                self.assert_assessment_values(actual[key], expected[key], f"{label}.{key}")
        elif isinstance(expected, list):
            self.assertEqual(len(actual), len(expected), label)
            for index, (got, wanted) in enumerate(zip(actual, expected)):
                self.assert_assessment_values(got, wanted, f"{label}[{index}]")
        elif isinstance(expected, float) and isinstance(actual, (int, float)):
            self.assertAlmostEqual(actual, expected, delta=1e-8, msg=label)
        else:
            self.assertEqual(actual, expected, label)

    def assert_values_close(self, actual, expected, tolerance, label):
        if isinstance(expected, dict):
            self.assertEqual(set(actual), set(expected), label)
            for key in expected:
                self.assert_values_close(actual[key], expected[key], tolerance, f"{label}.{key}")
        elif isinstance(expected, list):
            self.assertEqual(len(actual), len(expected), label)
            for index, (got, wanted) in enumerate(zip(actual, expected)):
                self.assert_values_close(got, wanted, tolerance, f"{label}[{index}]")
        elif isinstance(expected, float) and isinstance(actual, (int, float)):
            self.assertAlmostEqual(actual, expected, delta=tolerance, msg=label)
        else:
            self.assertEqual(actual, expected, label)

    def test_level1_has_real_submission_modes_and_independent_fixtures(self):
        level = [e for e in self.curriculum if e["level"] == 1]
        self.assertEqual(len(level), 15)
        self.assertEqual({e["category"] for e in level}, {"เขียนโค้ดจากศูนย์", "ทำนายผล", "แก้โค้ดที่ผิด", "เติมโค้ด", "โจทย์ประยุกต์"})
        self.assertEqual([e["submission_mode"] for e in level].count("text_answer"), 3)
        self.assertTrue(all(e["lesson"] and len(e["hints"]) == 3 and e["explanation"] for e in level))
        for ex in level:
            if ex["submission_mode"] == "stdout":
                cases = ex["cases"] or json.loads((ROOT / "tests" / "assessment" / "L01-E015-A.json").read_text(encoding="utf-8"))
                self.assertGreaterEqual(len(cases), 1, ex["id"])
                for case in cases:
                    self.assertIn("expected_stdout", case)

    def test_materializer_preserves_existing_student_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            student = Path(tmp) / "answer.py"
            authored = "my submitted answer = 42\n"
            student.write_text(authored, encoding="utf-8")
            self.assertFalse(write_student(student, "new starter\n"))
            self.assertEqual(student.read_text(encoding="utf-8"), authored)

    def test_level1_cli_text_is_windows_console_encodable(self):
        for ex in [e for e in self.curriculum if e["level"] == 1]:
            values = [ex.get(k, "") for k in ("title", "objective", "lesson", "example", "pitfall", "problem", "sample", "expected", "constraints", "explanation")]
            values.extend(ex.get("variant_prompts", {}).values())
            values.extend(ex.get("variant_expected", {}).values())
            for value in values:
                if isinstance(value, str):
                    value.encode("cp874")
            (ROOT / "explanations" / f"{ex['id']}.md").read_text(encoding="utf-8").encode("cp874")

    def test_hardcoded_outputs_fail_parameterized_exercises(self):
        for exercise_id in ("L01-E008", "L01-E010", "L01-E011", "L01-E013", "L01-E014", "L01-E015"):
            ex = next(e for e in self.curriculum if e["id"] == exercise_id)
            path = ROOT / "exercises" / "level_01" / f"{exercise_id}.py"
            cases = ex["cases"]
            if ex.get("assessment"):
                cases = json.loads((ROOT / "tests" / "assessment" / "L01-E015-A.json").read_text(encoding="utf-8"))
            bad_source = 'print("hardcoded answer")\n'
            with tempfile.TemporaryDirectory() as tmp:
                bad = Path(tmp) / "bad.py"
                bad.write_text(bad_source, encoding="utf-8")
                results = [subprocess.run([sys.executable, "-X", "utf8", "-I", str(bad)], input=c.get("stdin", ""), text=True, encoding="utf-8", capture_output=True, timeout=4).stdout for c in cases]
            self.assertTrue(any(out != c["expected_stdout"] for out, c in zip(results, cases)), exercise_id)

    def test_solution_reveal_and_locking_in_isolated_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            for name in ("solutions", "explanations", "exercises", "lessons"):
                shutil.copytree(ROOT / name, dest / name)
            first = self.curriculum[0]
            student_file = dest / "exercises" / "level_01" / f"{first['id']}.py"
            before = student_file.read_bytes()
            start = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "start"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertEqual(start.returncode, 0, start.stderr)
            self.assertIn("L01-E001", start.stdout)
            lesson = (dest / "lessons" / "L01-E001.md").read_text(encoding="utf-8")
            self.assertTrue(any(0x0E00 <= ord(ch) <= 0x0E7F for ch in lesson))
            isolated_env = os.environ.copy()
            isolated_env["PATH"] = tmp
            opened = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "open"], cwd=dest, env=isolated_env, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertIn("L01-E001.py", opened.stdout)
            cancel_solution = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "solution", "L01-E001"], input="NO\n", cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertEqual(cancel_solution.returncode, 0, cancel_solution.stderr)
            self.assertEqual(student_file.read_bytes(), before)
            progress_after_cancel = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
            self.assertFalse(progress_after_cancel.get("exercises", {}).get(first["id"], {}).get("solution_viewed", False))
            hint = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "hint", first["id"], "2"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertEqual(hint.returncode, 0, hint.stderr)
            explanation = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "explain", first["id"], "--yes"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertEqual(explanation.returncode, 0, explanation.stderr)
            result = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "solution", first["id"], "--yes"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(student_file.read_bytes(), before)
            progress = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
            self.assertTrue(progress["exercises"][first["id"]]["solution_viewed"])
            self.assertIn(2, progress["exercises"][first["id"]]["hints"])
            self.assertEqual(progress["exercises"][first["id"]]["status"], "NOT_STARTED")
            locked = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", "L01-E002"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertIn("ยังล็อกอยู่", locked.stdout)
            reset = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "reset-progress", "--yes"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertEqual(reset.returncode, 0, reset.stderr)
            self.assertEqual(student_file.read_bytes(), before)

    def test_cli_grader_accepts_reference_and_rejects_wrong_answer(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            ex = self.curriculum[0]
            level = f"level_{ex['level']:02d}"
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            shutil.copytree(ROOT / "exercises", dest / "exercises")
            shutil.copytree(ROOT / "solutions", dest / "solutions")
            student = dest / "exercises" / level / f"{ex['id']}.py"
            solution = dest / "solutions" / level / f"{ex['id']}.py"
            student.write_bytes(solution.read_bytes())
            result = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("PASSED_INDEPENDENTLY", result.stdout)
            student.write_text('print("wrong output")\n', encoding="utf-8")
            wrong = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
            self.assertIn("NEEDS_REVIEW", wrong.stdout)

    def test_cli_checks_all_five_real_level1_formats(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            for name in ("exercises", "solutions", "tests", "answers"):
                shutil.copytree(ROOT / name, dest / name)
            for ex in [e for e in self.curriculum if e["level"] == 1]:
                student = dest / ex["answer_file"] if ex["submission_mode"] == "text_answer" else dest / "exercises" / "level_01" / f"{ex['id']}.py"
                first = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
                self.assertIn("NEEDS_REVIEW", first.stdout, ex["id"])
                solution = dest / "solutions" / "level_01" / f"{ex['id']}.{'txt' if ex['submission_mode'] == 'text_answer' else 'py'}"
                if ex.get("assessment"):
                    solution = dest / "solutions" / "assessment" / f"{ex['id']}-A.py"
                shutil.copy2(solution, student)
                if ex["id"] == "L01-E001":
                    ran = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "run", ex["id"]], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
                    self.assertEqual(ran.returncode, 0, ran.stderr)
                    self.assertIn("สวัสดี Python", ran.stdout)
                    hint = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "hint", ex["id"], "1"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
                    self.assertEqual(hint.returncode, 0, hint.stderr)
                passed = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
                expected_status = "PASSED_WITH_HELP" if ex["id"] == "L01-E001" else "PASSED_INDEPENDENTLY"
                self.assertIn(expected_status, passed.stdout, f"{ex['id']}: {passed.stdout} {passed.stderr}")
                if ex["id"] == "L01-E001":
                    next_result = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "next"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
                    self.assertIn("L01-E002", next_result.stdout)
                if ex["id"] in {"L01-E008", "L01-E011", "L01-E015"}:
                    cases = ex["cases"]
                    if ex.get("assessment"):
                        cases = json.loads((ROOT / "tests" / "assessment" / "L01-E015-A.json").read_text(encoding="utf-8"))
                    first_output = cases[0]["expected_stdout"].rstrip("\n")
                    student.write_text(f"print({first_output!r})\n", encoding="utf-8")
                    hardcoded = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
                    self.assertIn("NEEDS_REVIEW", hardcoded.stdout, ex["id"])
                    shutil.copy2(solution, student)
                    passed_again = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
                    self.assertIn("PASSED_INDEPENDENTLY", passed_again.stdout, ex["id"])

    def test_next_level_requires_independent_assessment(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            previous = {e["id"]: {"status": "PASSED_INDEPENDENTLY", "attempts": 1, "hints": [], "solution_viewed": False} for e in self.curriculum if e["level"] == 1}
            previous["L01-E015"]["status"] = "PASSED_WITH_HELP"
            (dest / "progress.json").write_text(json.dumps({"exercises": previous}), encoding="utf-8")
            result = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", "L02-E001"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertIn("ยังล็อกอยู่", result.stdout)

    def test_assessment_reveal_is_assisted_and_fresh_variant_can_pass_independently(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            for name in ("exercises", "solutions", "tests"):
                shutil.copytree(ROOT / name, dest / name)
            prior = {f"L01-E{i:03d}": {"status": "PASSED_INDEPENDENTLY", "attempts": 1, "hints": [], "solution_viewed": False} for i in range(1, 15)}
            (dest / "progress.json").write_text(json.dumps({"exercises": prior}), encoding="utf-8")
            student = dest / "exercises" / "level_01" / "L01-E015.py"
            starter_before_reveal = student.read_bytes()
            reveal = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "solution", "L01-E015", "--yes"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertEqual(reveal.returncode, 0, reveal.stderr)
            self.assertEqual(student.read_bytes(), starter_before_reveal)
            progress = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
            self.assertEqual(progress["exercises"]["L01-E015"]["status"], "NOT_STARTED")
            self.assertIn("A", progress["exercises"]["L01-E015"]["revealed_assessments"])
            first_solution = dest / "solutions" / "assessment" / "L01-E015-A.py"
            shutil.copy2(first_solution, student)
            assisted = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", "L01-E015"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
            self.assertIn("PASSED_WITH_HELP", assisted.stdout)
            progress = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
            self.assertFalse(progress["exercises"]["L01-E015"]["assessment_verified"])
            reassess = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "retry", "L01-E015"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertIn("B", reassess.stdout)
            self.assertIn("Expenses:", reassess.stdout)
            self.assertNotIn("Gross:", reassess.stdout)
            second_solution = dest / "solutions" / "assessment" / "L01-E015-B.py"
            self.assertNotEqual(first_solution.read_bytes(), second_solution.read_bytes())
            shutil.copy2(second_solution, student)
            independent = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", "L01-E015"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
            self.assertIn("PASSED_INDEPENDENTLY", independent.stdout)
            progress = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
            self.assertTrue(progress["exercises"]["L01-E015"]["assessment_verified"])
            unlocked = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", "L02-E001"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=8)
            self.assertNotIn("ยังล็อกอยู่", unlocked.stdout)

    def test_legacy_level1_assessment_evidence_is_preserved_but_not_trusted(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            exercises = {f"L01-E{i:03d}": {"status": "PASSED_INDEPENDENTLY", "attempts": 2, "hints": [], "solution_viewed": False} for i in range(1, 16)}
            exercises["L01-E015"]["attempts"] = 7
            exercises["L01-E015"]["results"] = [{"passed": True, "tests": 1}]
            original = json.loads(json.dumps(exercises["L01-E015"]))
            (dest / "progress.json").write_text(json.dumps({"exercises": exercises}), encoding="utf-8")
            blocked = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", "L02-E001"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertIn("ยังล็อกอยู่", blocked.stdout)
            migrated = json.loads((dest / "progress.json").read_text(encoding="utf-8"))["exercises"]["L01-E015"]
            self.assertEqual(migrated["status"], original["status"])
            self.assertEqual(migrated["attempts"], original["attempts"])
            self.assertEqual(migrated["results"], original["results"])
            self.assertTrue(migrated["legacy_assessment_pending"])
            self.assertFalse(migrated["assessment_verified"])

    def test_existing_level2_assessment_unlock_rules_are_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            previous = {f"L02-E{i:03d}": {"status": "PASSED_INDEPENDENTLY", "attempts": 1, "hints": [], "solution_viewed": False} for i in range(1, 16)}
            (dest / "progress.json").write_text(json.dumps({"exercises": previous}), encoding="utf-8")
            result = subprocess.run([sys.executable, "-X", "utf8", "practice.py", "check", "L03-E001"], cwd=dest, capture_output=True, text=True, encoding="utf-8", timeout=5)
            self.assertNotIn("ยังล็อกอยู่", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
