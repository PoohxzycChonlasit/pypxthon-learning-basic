import contextlib
import io
import re
import sqlite3
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class M006BDeliverableTests(unittest.TestCase):
    def test_new_track_and_roadmap_local_links_resolve(self):
        documents = [
            ROOT / "README.md",
            ROOT / "docs" / "learning-roadmap.md",
            ROOT / "docs" / "video-learning-roadmap.md",
            ROOT / "tracks" / "README.md",
            *sorted((ROOT / "tracks" / "engineering_thinking").rglob("*.md")),
        ]
        for document in documents:
            self.assertTrue(document.is_file(), str(document))
            for target in LINK.findall(document.read_text(encoding="utf-8")):
                target = target.strip().strip("<>")
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                local = unquote(target.split("#", 1)[0].split("?", 1)[0])
                if not local:
                    continue
                self.assertTrue((document.parent / local).exists(), f"{document}: {target}")

    def test_engineering_track_covers_scope_and_practical_scenarios(self):
        track = ROOT / "tracks" / "engineering_thinking"
        content = "\n".join(path.read_text(encoding="utf-8") for path in track.rglob("*.md")).lower()
        for term in (
            "problem decomposition", "requirements", "pseudocode", "input/output",
            "data model", "architecture", "implementation plan", "ai-assisted",
            "code review", "test", "reliability",
        ):
            self.assertIn(term, content)
        for name in (
            "expense-tracker.md", "ecommerce-order-processor.md", "csv-data-analyzer.md",
            "offline-quant-research-engine.md", "offline-paper-trading-bot.md",
        ):
            exercise = track / "exercises" / name
            self.assertTrue(exercise.is_file(), name)
            self.assertIn("before asking ai", exercise.read_text(encoding="utf-8").lower())

    def test_video_roadmap_covers_topics_and_distinguishes_verified_sources(self):
        roadmap = (ROOT / "docs" / "video-learning-roadmap.md").read_text(encoding="utf-8").lower()
        for topic in (
            "python phase 1", "python phase 2", "algorithms", "git and github", "sql",
            "file i/o", "unit testing", "numpy", "pandas", "matplotlib",
            "software architecture", "ai coding workflows", "quant research",
        ):
            self.assertIn(topic, roadmap)
        for video_id in (
            "heqxgfyk77i", "r8jq9hva2qs", "-fw2x7fh7yg", "uh2ebfw8oym",
            "ybpkmiujvk8", "zb7bzmhfpgk", "_t8lgqjtugc",
            "uo98ljq3qgi", "px7xlbygk7i",
        ):
            self.assertIn(video_id, roadmap)
        for topic in ("python phase 2", "algorithms and pseudocode", "software architecture", "quant research"):
            row = next(line for line in roadmap.splitlines() if line.startswith(f"| {topic} |"))
            self.assertIn("`unknown / unknown`", row, topic)

    def test_sqlite_example_explains_and_demonstrates_close(self):
        handbook = (ROOT / "docs" / "python-syntax-handbook.md").read_text(encoding="utf-8")
        section = handbook.split("### SQLite ด้วย standard library", 1)[1].split("### ", 1)[0]
        self.assertIn("ไม่ได้ปิด connection อัตโนมัติ", section)
        self.assertIn("contextlib import closing", section)
        code = section.split("~~~python", 1)[1].split("~~~", 1)[0]
        namespace = {}
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(code, namespace)
        self.assertEqual(output.getvalue().strip(), "[('2025-01', 12.5)]")
        with self.assertRaises(sqlite3.ProgrammingError):
            namespace["connection"].execute("SELECT 1")

    def test_l05_e010_scenario_matches_csv_header_task(self):
        starter = (ROOT / "exercises" / "level_05" / "L05-E010.py").read_text(encoding="utf-8")
        self.assertIn("ผู้ดูแลรายงานที่รับไฟล์ CSV", starter)
        self.assertNotIn("นักวิจัย Quant ที่ทดสอบสูตร", starter)


if __name__ == "__main__":
    unittest.main()
