"""Structural and runnable-example checks for all main-course instructions."""

import contextlib
import io
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExerciseInstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))

    def test_all_exercises_have_the_required_instruction_format(self):
        self.assertEqual(len(self.catalog), 150)
        code_count = 0
        text_count = 0
        for exercise in self.catalog:
            exercise_id = exercise["id"]
            level = exercise["level"]
            if exercise.get("submission_mode") == "text_answer":
                text_count += 1
                instructions = ROOT / "instructions" / f"level_{level:02d}" / f"{exercise_id}.md"
                answer = ROOT / exercise["answer_file"]
                self.assertTrue(instructions.is_file(), exercise_id)
                self.assertEqual(answer.read_text(encoding="utf-8").lstrip().startswith("#"), False, exercise_id)
                continue

            code_count += 1
            starter = ROOT / "exercises" / f"level_{level:02d}" / f"{exercise_id}.py"
            source = starter.read_text(encoding="utf-8")
            self.assertNotIn("…", source, f"{exercise_id} contains truncated instruction text")
            for heading in (
                "EXERCISE", "LEARNING OBJECTIVE", "REAL-WORLD SCENARIO", "TASK CHECKLIST",
                "INPUT AND OUTPUT", "SYNTAX REFERENCE", "IMPLEMENTATION", "VERIFICATION",
                "HELP AND COMPLETION", "TODO(student)",
            ):
                self.assertIn(heading, source, f"{exercise_id} missing {heading}")
            self.assertIn(exercise["difficulty_tier"], range(1, 6), exercise_id)
            tier_line = next(line for line in source.splitlines() if "Level " in line and "Tier " in line)
            displayed_tier = int(tier_line.split("Tier ", 1)[1].split(":", 1)[0])
            self.assertEqual(displayed_tier, exercise["difficulty_tier"], exercise_id)
            self._check_box_width(starter, exercise_id)
            self._check_syntax_example(starter, exercise_id)
        self.assertEqual((code_count, text_count), (138, 12))

    def _check_box_width(self, path, exercise_id):
        lines = path.read_text(encoding="utf-8").splitlines()
        start = next(i for i, line in enumerate(lines) if "M005 EXERCISE BOX" in line)
        help_start = next(i for i in range(start, len(lines)) if "HELP AND COMPLETION" in lines[i])
        end = next(i for i in range(help_start + 1, len(lines)) if lines[i].startswith("# └"))
        for number, line in enumerate(lines[start : end + 1], start + 1):
            self.assertLessEqual(len(line), 80, f"{exercise_id}:{number}")

    def _check_syntax_example(self, path, exercise_id):
        lines = path.read_text(encoding="utf-8").splitlines()
        start = next(i for i, line in enumerate(lines) if "ตัวอย่างสั้น" in line)
        code = []
        expected = None
        for line in lines[start + 1 :]:
            if "ผลที่คาด:" in line:
                expected = line.split("ผลที่คาด:", 1)[1].rsplit("│", 1)[0].strip()
                break
            if line.startswith("# │"):
                body = line[len("# │ ") :]
                if body.endswith(" │"):
                    body = body[:-2].rstrip()
                if body.startswith("    "):
                    code.append(body[4:].rstrip())
        self.assertTrue(code, exercise_id)
        self.assertIsNotNone(expected, exercise_id)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec("\n".join(code), {})
        self.assertEqual(output.getvalue().rstrip("\n"), expected, exercise_id)


if __name__ == "__main__":
    unittest.main()
