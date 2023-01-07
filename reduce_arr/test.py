import unittest
from main import grow

class TestReduceArr(unittest.TestCase):
    def test_function(self):
        self.assertEqual(grow([1,2,3]), 6)

if __name__ == "__main__":
    unittest.main()