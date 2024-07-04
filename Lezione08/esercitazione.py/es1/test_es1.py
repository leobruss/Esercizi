import unittest
from es1 import merge
from test1 import test_1
from test2 import test_2

class Testmerge(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(test_1(), [1, 2, 3, 4, 4, 5])
        print(test_1())
        self.assertEqual(test_2(), [1, 3, 3, 5, 6, 7])
        print(test_2())

if __name__ == '__main__':
    unittest.main()
