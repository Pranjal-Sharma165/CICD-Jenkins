
import unittest
from app import add, subtract, multiply


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_zero(self):
        self.assertEqual(multiply(5, 0), 0)


if __name__ == "__main__":
    unittest.main()
