def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opera = input("Enter the operation (add, subtract, multiply, divide): ")
print(f"Result:) {perform_operation(num1,num2,opera)}")