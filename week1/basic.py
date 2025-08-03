print("Hello world")
a=3.5
c="Hello"
b=2
d=True

print(type(a))
print(type(b))  
print(type(c))
print(type(d))

name=input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old")

if age > 18 and name == "John":
    print("You are an adult named John")
else:
    print("You are either not an adult or not named John")
    for i in range(5):
        print("This is iteration number", i + 1)

count=0
while count<10:
            print("counting:",count)
            count+=1

n=10
sum=a+b
print("The sum of a and b is:", sum)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("The factorial of", n, "is:", factorial(n))

var1=20

def my_gloabalfunction():
    var2=30
    global var1
    print("Local variable var2:", var2)
    print("Global variable var1:", var1)

