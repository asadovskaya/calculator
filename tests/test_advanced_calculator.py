import unittest
from src.advanced_calculator import AdvancedCalculator

class TestAdvancedCalculator(unittest.TestCase):
    def test_power(self):
        self.assertEqual(AdvancedCalculator.power(2, 3), 8)
        self.assertEqual(AdvancedCalculator.power(5, 0), 1)
    
    def test_square_root(self):
        self.assertEqual(AdvancedCalculator.square_root(9), 3)
        self.assertEqual(AdvancedCalculator.square_root(0), 0)
        with self.assertRaises(ValueError):
            AdvancedCalculator.square_root(-4)
    
    def test_factorial(self):
        self.assertEqual(AdvancedCalculator.factorial(5), 120)
        self.assertEqual(AdvancedCalculator.factorial(0), 1)
        with self.assertRaises(ValueError):
            AdvancedCalculator.factorial(-3)
        with self.assertRaises(TypeError):
            AdvancedCalculator.factorial(3.5)
    
    def test_logarithm(self):
        self.assertAlmostEqual(AdvancedCalculator.logarithm(100, 10), 2)
        self.assertAlmostEqual(AdvancedCalculator.logarithm(8, 2), 3)
        with self.assertRaises(ValueError):
            AdvancedCalculator.logarithm(-10)
        with self.assertRaises(ValueError):
            AdvancedCalculator.logarithm(0)

if __name__ == '__main__':
    unittest.main()
