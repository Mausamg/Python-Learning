def greet():
    print("Hello, World!")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(base, exponent):
    return base ** exponent

greet()

# Example usage of the functions
num_1= int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

add_result = add(num_1, num_2)
multiply_result = multiply(num_1, num_2)
subtract_result = subtract(num_1, num_2)
divide_result = divide(num_1, num_2)
power_result = power(num_1, num_2)
print(f"Addition: {add_result}")
print(f"Multiplication: {multiply_result}")
print(f"Subtraction: {subtract_result}")
print(f"Division: {divide_result}")
print(f"Power: {power_result}")

def print_numbers(num_3):
    print("This function prints numbers from 1 to a given number.")
    for i in range(1, num_3 + 1):
        print(i)

num_3 = int(input("Enter a number to print from 1 to that number: "))
print_numbers(num_3)