import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(3, 5), 8)
    
    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 4), 6)
    
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 4), 12)
    
    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)