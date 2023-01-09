import os
import unittest

from context import tools

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


class TestStitcher(unittest.TestCase):
    
    def test_tiff_stitcher(self):
        os.chdir(CURRENT_DIR)
        try:
            tool = tools.TiffStitcher(
                src="../testing_data/S1_20170411_IW",
                dest="../testing_data/output.tif"
            )
            
            tool.run()
        except Exception:
            self.fail("Tool as Failed")