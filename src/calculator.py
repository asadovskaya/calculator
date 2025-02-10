class Calculator:
   
    @staticmethod
    def add(x, y):
        """
        Adds two numbers together.

        Args:
            x (int or float): The first number.
            y (int or float): The second number.

        Returns:
            int or float: The sum of x and y.
        """
        return x + y
    
    @staticmethod
    def subtract(x, y):
        """
        Subtracts the second number from the first number.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The result of subtracting y from x.
        """
        return x - y
    
    @staticmethod
    def multiply(x, y):
        """
        Multiplies two numbers together.

        Args:
            x (int or float): The first number.
            y (int or float): The second number.

        Returns:
            int or float: The product of the two numbers.
        """
        return x * y
    
    @staticmethod
    def divide(x, y):
        """
        Divides two numbers and returns the result.

        Parameters:
        x (float): The numerator.
        y (float): The denominator.

        Returns:
        float: The result of the division.

        Raises:
        ValueError: If the denominator (y) is zero.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    