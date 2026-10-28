"""Checks the concise M008 starter headers and canonical lesson examples."""

import ast
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExerciseInstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(
            (ROOT / "curriculum.json").read_text(encoding="utf-8")
        )

    def test_all_exercises_have_a_short_header_and_a_runnable_lesson_example(self):
        self.assertEqual(len(self.catalog), 150)
        code_count = 0
        text_count = 0
        for exercise in self.catalog:
            exercise_id = exercise["id"]
            level = exercise["level"]
            lesson_path = ROOT / exercise["lesson_file"]
            self.assertTrue(lesson_path.is_file(), exercise_id)
            lesson = lesson_path.read_text(encoding="utf-8")
            example = re.search(r"~~~python\n(.*?)\n~~~", lesson, re.S)
            self.assertIsNotNone(example, exercise_id)
            try:
                ast.parse(example.group(1))
            except SyntaxError as error:
                self.fail(f"{exercise_id} lesson example is invalid Python: {error}")

            if exercise["submission_mode"] == "text_answer":
                text_count += 1
                instructions = (
                    ROOT
                    / "instructions"
                    / f"level_{level:02d}"
                    / f"{exercise_id}.md"
                )
                answer = ROOT / exercise["answer_file"]
                legacy = (
                    ROOT
                    / "exercises"
                    / f"level_{level:02d}"
                    / f"{exercise_id}.py"
                )
                self.assertTrue(instructions.is_file(), exercise_id)
                self.assertFalse(
                    answer.read_text(encoding="utf-8").lstrip().startswith("#"),
                    exercise_id,
                )
                self.assertIn("ไม่ใช่ไฟล์ส่งคำตอบ", legacy.read_text(encoding="utf-8"))
                self.assertIn(f"check {exercise_id}", lesson)
                self.assertNotIn(f"practice.py run {exercise_id}", lesson)
                continue

            code_count += 1
            starter = (
                ROOT
                / "exercises"
                / f"level_{level:02d}"
                / f"{exercise_id}.py"
            )
            source = starter.read_text(encoding="utf-8")
            self.assertTrue(source.startswith(f"# {exercise_id}"), exercise_id)
            self.assertNotIn("┌", source[:600], exercise_id)
            header = []
            for line in source.splitlines():
                if line.startswith("#"):
                    header.append(line)
                elif not line.strip():
                    continue
                else:
                    break
            self.assertLessEqual(len(header), 8, exercise_id)
            self.assertLessEqual(len("\n".join(header)), 650, exercise_id)
            joined_header = "\n".join(header)
            self.assertIn(f"Level {level}", joined_header, exercise_id)
            self.assertIn(f"Tier {exercise['difficulty_tier']}", joined_header, exercise_id)
            self.assertIn(f"lessons/{exercise_id}.md", joined_header, exercise_id)
            self.assertIn(f"practice.py check {exercise_id}", joined_header, exercise_id)
            self.assertIn("python3.12", joined_header, exercise_id)
            self.assertIn(f"practice.py run {exercise_id}", lesson, exercise_id)

        self.assertEqual((code_count, text_count), (138, 12))


if __name__ == "__main__":
    unittest.main()
