#conditional statements

#if statement
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
if num_1 > num_2:
    print("First number is greater than second number")

# Nested if statement
if num_1 > 0:
    print("First number is positive")
    if num_2 > 0:
        print("Second number is also positive")
    else:
        print("Second number is not positive")

# if-else statement
if num_1 > num_2:
    print("First number is greater than second number")
else:
    print("First number is not greater than second number")

# if-elif-else statement
if num_1 > num_2:
    print("First number is greater than second number") 
elif num_1 < num_2:
    print("First number is less than second number")
else:
    print("Both numbers are equal")

# Ternary operator
result = "First number is greater than second number" if num_1 > num_2 else "First number is not greater than second number"
print(result)
