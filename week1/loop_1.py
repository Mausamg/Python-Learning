#loop

#for loop
num_1=int(input("Enter first number: "))
for i in range(1, num_1 + 1):
    print(i)

# while loop
num_2 = int(input("Enter second number: "))
while num_2 > 0:
    print(num_2)
    num_2 -= 1

# do-while loop
num_3 = int(input("Enter third number: "))
i = 1
while True:
    print(i)
    i += 1
    if i > num_3:
        break
