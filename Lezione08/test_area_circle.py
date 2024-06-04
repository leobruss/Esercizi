import unittest
from shape import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        area = Circle(5)
        self.assertEqual(area.area(), 78.5, "The area is wrong")

if __name__ == '__main__':
    unittest.main()