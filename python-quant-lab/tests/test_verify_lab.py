"""Offline integrity checks for the bundled curriculum. Run: python -m unittest discover -s tests."""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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
            hints = json.loads((ROOT / "hints" / f"{ex['id']}.json").read_text(encoding="utf-8"))
            self.assertEqual(len(hints), 3, ex["id"])
            self.assertGreaterEqual(len(ex["cases"]), 2, ex["id"])
            self.assertTrue(all(p in known for p in ex["prerequisites"]), ex["id"])
            self.assertTrue(ex["assessment"] if ex["id"].endswith("E015") else True)

    def test_all_reference_solutions_satisfy_all_cases(self):
        for ex in self.curriculum:
            module = load(ROOT / "solutions" / f"level_{ex['level']:02d}" / f"{ex['id']}.py")
            fn = getattr(module, ex["function"])
            for case in ex["cases"]:
                got = normalize(fn(*case["args"], **case.get("kwargs", {})))
                expected = normalize(case["expected"])
                if isinstance(expected, float) and isinstance(got, (int, float)):
                    self.assertAlmostEqual(got, expected, delta=case.get("tolerance", 1e-8), msg=ex["id"])
                else:
                    self.assertEqual(got, expected, ex["id"])

    def test_starters_are_unfinished(self):
        for ex in self.curriculum:
            path = ROOT / "exercises" / f"level_{ex['level']:02d}" / f"{ex['id']}.py"
            module = load(path)
            with self.assertRaises(NotImplementedError, msg=ex["id"]):
                getattr(module, ex["function"])(*ex["cases"][0]["args"])

    def test_solution_reveal_and_locking_in_isolated_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            shutil.copytree(ROOT / "solutions", dest / "solutions")
            shutil.copytree(ROOT / "explanations", dest / "explanations")
            shutil.copytree(ROOT / "exercises", dest / "exercises")
            first = self.curriculum[0]
            student_file = dest / "exercises" / "level_01" / f"{first['id']}.py"
            before = student_file.read_bytes()
            start = subprocess.run([sys.executable, "practice.py", "start"], cwd=dest, capture_output=True, text=True, timeout=5)
            self.assertEqual(start.returncode, 0, start.stderr)
            self.assertIn("L01-E001", start.stdout)
            hint = subprocess.run([sys.executable, "practice.py", "hint", first["id"], "2"], cwd=dest, capture_output=True, text=True, timeout=5)
            self.assertEqual(hint.returncode, 0, hint.stderr)
            explanation = subprocess.run([sys.executable, "practice.py", "explain", first["id"], "--yes"], cwd=dest, capture_output=True, text=True, timeout=5)
            self.assertEqual(explanation.returncode, 0, explanation.stderr)
            result = subprocess.run([sys.executable, "practice.py", "solution", first["id"], "--yes"], cwd=dest, capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(student_file.read_bytes(), before)
            progress = json.loads((dest / "progress.json").read_text(encoding="utf-8"))
            self.assertTrue(progress["exercises"][first["id"]]["solution_viewed"])
            self.assertIn(2, progress["exercises"][first["id"]]["hints"])
            locked = subprocess.run([sys.executable, "practice.py", "check", "L01-E002"], cwd=dest, capture_output=True, text=True, timeout=5)
            self.assertIn("ยังล็อกอยู่", locked.stdout)
            reset = subprocess.run([sys.executable, "practice.py", "reset-progress", "--yes"], cwd=dest, capture_output=True, text=True, timeout=5)
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
            result = subprocess.run([sys.executable, "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, timeout=8)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("PASSED_INDEPENDENTLY", result.stdout)
            student.write_text(f"def {ex['function']}({ex['signature']}):\n    return None\n", encoding="utf-8")
            wrong = subprocess.run([sys.executable, "practice.py", "check", ex["id"]], cwd=dest, capture_output=True, text=True, timeout=8)
            self.assertIn("ยังไม่ผ่าน", wrong.stdout)

    def test_next_level_requires_independent_assessment(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for name in ("practice.py", "curriculum.json"):
                shutil.copy2(ROOT / name, dest / name)
            previous = {e["id"]: {"status": "PASSED_INDEPENDENTLY", "attempts": 1, "hints": [], "solution_viewed": False} for e in self.curriculum if e["level"] == 1}
            previous["L01-E015"]["status"] = "PASSED_WITH_HELP"
            (dest / "progress.json").write_text(json.dumps({"exercises": previous}), encoding="utf-8")
            result = subprocess.run([sys.executable, "practice.py", "check", "L02-E001"], cwd=dest, capture_output=True, text=True, timeout=5)
            self.assertIn("ยังล็อกอยู่", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
