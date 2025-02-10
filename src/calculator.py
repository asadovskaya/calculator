class Calculator:
    """
    Calculator class provides basic arithmetic operations.
    Methods:
        add(x, y):
            Returns the sum of x and y.
        subtract(x, y):
            Returns the difference of x and y.
        multiply(x, y):
            Returns the product of x and y.
        divide(x, y):
            Returns the quotient of x and y.
            Raises ValueError if y is zero.
    """
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    