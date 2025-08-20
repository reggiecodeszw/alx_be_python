num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose an operator (+, -, *, /): ")

match operator:
    case "+":
        result = num1 + num2
        print("Result:", result)
    case "-":
        result = num1 - num2
        print("Result:", result)
    case "*":
        result = num1 * num2
        print("Result:", result)
    case "/":
        try:
            result = num1 // num2
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print("Result:", result)
    case _:
        print("Invalid operator")