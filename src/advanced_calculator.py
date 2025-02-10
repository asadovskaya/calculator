import math

class AdvancedCalculator:
        
    @staticmethod
    def power(x, y):
        """
        Calculate the power of a number.

        Args:
            x (float): The base number.
            y (float): The exponent.

        Returns:
            float: The result of raising x to the power of y.
        """
        """Exponentiation"""
        return x ** y
    
    @staticmethod
    def square_root(x):
        """Square root with error handling"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    @staticmethod
    def factorial(x):
        """Calculate factorial"""
        if x < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if not isinstance(x, int):
            raise TypeError("Factorial requires an integer")
        return math.factorial(x)
    
    @staticmethod
    def logarithm(x, base=10):
        """Logarithm with custom base (default 10)"""
        if x <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers")
        return math.log(x, base)