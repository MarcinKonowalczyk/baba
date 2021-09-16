import unittest

# Add '.' to path so running this file by itself also works
import os, sys

sys.path.append(os.path.realpath("."))

from golf.golfing_short import Y
from baba.test_cases import TEST_CASES


class Golf(unittest.TestCase):
    def test_golf(self):
        """Test the minimal golfing implementation"""
        for name, case in TEST_CASES.items():
            sequence = case["sequence"]
            expected = case["outcome"]
            with self.subTest(name=name):
                self.assertEqual(Y(sequence), expected)


if __name__ == "__main__":
    unittest.main()
