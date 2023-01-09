import os
import unittest

from context import core

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

class TestFileGetters(unittest.TestCase):
    
    os.chdir(CURRENT_DIR)
    top_level = "../testing_data/S1_20170411_IW"
    
    def test_get_filenames(self):
        os.chdir(CURRENT_DIR)
        ref_values = [os.path.join(self.top_level, _) for _ in 
                      os.listdir(self.top_level)]

        test_values = core.get_filename(self.top_level)
        self.assertListEqual(ref_values, test_values, msg="List do not match")
    
    def test_get_basenames(self):
        ref_values = [os.path.join(self.top_level, _) for _ in 
                      os.listdir(self.top_level)]
        ref_base = [os.path.basename(_) for _ in ref_values]
        
        test_base = core.get_basenames(ref_values)
        self.assertListEqual(ref_base, test_base, msg="List do not match")

    def test_get_rows(self):
        ref_values = [os.path.join(self.top_level, _) for _ in 
                      os.listdir(self.top_level)]
        try:
            rows = core.get_rows(ref_values)
        except Exception as e:
            self.fail("has failed...")

    def test_get_files_by_row(self):
        ref_values = [os.path.join(self.top_level, _) for _ in 
                      os.listdir(self.top_level)]
        basenames = core.get_basenames(ref_values)
        row_idxs = core.get_rows(basenames=basenames)

        try:
            rows = core.files_by_row(row_idxs, basenames=basenames)
            b = ' '
    
        except Exception as e:
            self.fail("has failed...")