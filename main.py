from src.calculator import Calculator

def main():
    print("Simple Calculator")
    
    while True:
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
                continue
            
            print(f"Result: {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        
        cont = input("Continue? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()