# Simple Calculator using match-case in Python 3.10+

def calculator():
    print("=== Simple Calculator ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    match op:
        case '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        case '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        case '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        case '/':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("❌ Error: Cannot divide by zero.")
        case _:
            print("❌ Invalid operator. Please choose from +, -, *, /")

calculator()
