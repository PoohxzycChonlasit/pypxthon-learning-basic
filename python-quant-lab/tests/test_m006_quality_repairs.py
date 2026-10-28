import ast
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_function(path, function_name):
    spec = importlib.util.spec_from_file_location(function_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


class M006QualityRepairTests(unittest.TestCase):
    def test_oos_simple_returns_are_compounded(self):
        compare_oos = load_function(ROOT / "solutions" / "level_09" / "L09-E005.py", "compare_oos")
        result = compare_oos([0.1, 0.2], [0.0, 0.05])
        self.assertAlmostEqual(result["strategy_net"], 0.32)
        self.assertAlmostEqual(result["benchmark_net"], 0.05)
        self.assertAlmostEqual(result["excess"], 0.27)
        self.assertTrue(result["beats"])

    def test_prediction_prompt_is_self_contained_without_answer_leak(self):
        catalog = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))
        exercise = next(item for item in catalog if item["id"] == "L01-E007")
        self.assertIn("coins = 2", exercise["problem"])
        self.assertIn("print(\"BTC\")", exercise["problem"])
        self.assertNotIn("บรรทัดแรกเป็น 6", " ".join(exercise["hints"]))

    def test_difficulty_tier_stays_within_supported_range(self):
        catalog = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))
        self.assertEqual(len(catalog), 150)
        self.assertEqual(len({item["id"] for item in catalog}), 150)
        self.assertTrue(all(item["difficulty_tier"] in range(1, 6) for item in catalog))

    def test_final_assessment_variants_have_distinct_tasks_and_solutions(self):
        catalog = {item["id"]: item for item in json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))}
        for level in range(2, 11):
            exercise_id = f"L{level:02d}-E015"
            exercise = catalog[exercise_id]
            self.assertNotEqual(exercise["variant_prompts"]["A"], exercise["variant_prompts"]["B"], exercise_id)
            paths = [ROOT / "solutions" / "assessment" / f"{exercise_id}-{variant}.py" for variant in "AB"]
            trees = [ast.dump(ast.parse(path.read_text(encoding="utf-8")), include_attributes=False) for path in paths]
            self.assertNotEqual(trees[0], trees[1], exercise_id)
            cases = [json.loads((ROOT / "tests" / "assessment" / f"{exercise_id}-{variant}.json").read_text(encoding="utf-8")) for variant in "AB"]
            self.assertTrue(cases[0] and cases[1], exercise_id)

    def test_final_assessment_shared_guidance_and_hints_cover_both_variants(self):
        catalog = {item["id"]: item for item in json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))}
        for level in range(1, 11):
            exercise_id = f"L{level:02d}-E015"
            exercise = catalog[exercise_id]
            starter = ROOT / "exercises" / f"level_{level:02d}" / f"{exercise_id}.py"
            source = starter.read_text(encoding="utf-8")
            hints = json.loads((ROOT / "hints" / f"{exercise_id}.json").read_text(encoding="utf-8"))
            self.assertIn("variant", exercise["objective"].lower(), exercise_id)
            self.assertIn("variant ปัจจุบัน", exercise["lesson"], exercise_id)
            self.assertIn("variant", exercise["pitfall"].lower(), exercise_id)
            self.assertIn("prompt ของ variant ปัจจุบัน", source, exercise_id)
            self.assertIn("lesson ของ variant ที่ระบบเลือก", source, exercise_id)
            self.assertNotIn("ตัวอย่าง input:", source, exercise_id)
            self.assertEqual(exercise["hints"], hints, exercise_id)
            self.assertEqual(len(hints), 3, exercise_id)
            self.assertTrue(all("Hint 1:" not in hint for hint in hints), exercise_id)


if __name__ == "__main__":
    unittest.main()
