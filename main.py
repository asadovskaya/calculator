from src.calculator import Calculator
from src.advanced_calculator import AdvancedCalculator

def main():
    print("Comprehensive Calculator")
    
    while True:
        print("\nSelect Calculator Type:")
        print("1. Basic Operations")
        print("2. Advanced Operations")
        print("3. Exit")
        
        calculator_type = input("Enter choice (1-3): ")
        
        if calculator_type == '1':
            basic_calculator()
        elif calculator_type == '2':
            advanced_calculator()
        elif calculator_type == '3':
            break
        else:
            print("Invalid choice")

def basic_calculator():
    try:
        x = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        y = float(input("Enter second number: "))
        
        if operation == '+':
            result = Calculator.add(x, y)
        elif operation == '-':
            result = Calculator.subtract(x, y)
        elif operation == '*':
            result = Calculator.multiply(x, y)
        elif operation == '/':
            result = Calculator.divide(x, y)
        else:
            print("Invalid operation")
            return
        
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

def advanced_calculator():
    print("\nAdvanced Operations:")
    print("1. Power")
    print("2. Square Root")
    print("3. Factorial")
    print("4. Logarithm")
    
    choice = input("Enter choice (1-4): ")
    
    try:
        if choice == '1':
            x = float(input("Enter base number: "))
            y = float(input("Enter exponent: "))
            result = AdvancedCalculator.power(x, y)
        elif choice == '2':
            x = float(input("Enter number: "))
            result = AdvancedCalculator.square_root(x)
        elif choice == '3':
            x = int(input("Enter number: "))
            result = AdvancedCalculator.factorial(x)
        elif choice == '4':
            x = float(input("Enter number: "))
            base = input("Enter base (default 10): ")
            base = float(base) if base else 10
            result = AdvancedCalculator.logarithm(x, base)
        else:
            print("Invalid choice")
            return
        
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()