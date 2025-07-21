import unittest
from utils.add import addition
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestAdd(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(addition(1,1),2)

    def test_add_2(self):
        self.assertEqual(addition(2,2),4)

if __name__ == "__main__":
    unittest.main()
