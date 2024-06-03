import unittest
from lezione8 import MathOperations

class TestMathOperations(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(MathOperations.add(4, 6), 10, "The sum is wrong")
    
if __name__ == '__main__':
    unittest.main()