import unittest
from src.advanced_calculator import AdvancedCalculator

class TestAdvancedCalculator(unittest.TestCase):
    def test_power(self):
        self.assertEqual(AdvancedCalculator.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(AdvancedCalculator.square_root(4), 2)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            AdvancedCalculator.square_root(-4)

    def test_factorial(self):
        self.assertEqual(AdvancedCalculator.factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            AdvancedCalculator.factorial(-5)

    def test_factorial_non_integer(self):
        with self.assertRaises(TypeError):
            AdvancedCalculator.factorial(5.5)

    def test_logarithm(self):
        self.assertAlmostEqual(AdvancedCalculator.logarithm(100, 10), 2)

    def test_logarithm_non_positive(self):
        with self.assertRaises(ValueError):
            AdvancedCalculator.logarithm(-10)

if __name__ == '__main__':
    unittest.main()