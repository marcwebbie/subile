import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import subile


class SubileTests(unittest.TestCase):

    def test_get_subtitles(self):
        subtitles_list = subile.get_subtitles(
            "The.Walking.Dead.S04E10.Inmates.BDRip.x264-DEMAND.mkv",
            "fre"
        )
        for subtitles in subtitles_list:
            self.assertIsInstance(subtitles, subile.Subtitle)

    def test_get_zip_content(self):
        subtitle_content = subile.utils.get_zip_content(
            "http://dl.opensubtitles.org/en/download/sub/5556626")
        subtitle_text = subtitle_content.decode('utf-8', 'ignore')
        self.assertIn("-->", subtitle_text)

if __name__ == "__main__":
    unittest.main()
