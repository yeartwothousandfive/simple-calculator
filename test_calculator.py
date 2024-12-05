import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
