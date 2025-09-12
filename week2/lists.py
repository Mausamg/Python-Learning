# Lists are mutable, ordered collections of items

num_elements = int(input("Enter the number of elements in the list: "))
my_list = []

for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    my_list.append(element)  # appending as strings

# Changing first element to an integer 20 (optional, but causes mixed types)
# If you want to keep consistency, comment the next line out or convert all to int
my_list[0] = '20'  # changed to string '20' for consistency

print("Your list is:", my_list)
print("The length of the list is:", len(my_list))

for i in range(len(my_list)):
    print(f"Element {i + 1} is: {my_list[i]}")

# Sort the list alphabetically (since elements are strings)
my_list.sort()
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)

# Slicing the list (safe even if length < 4)
sliced_list = my_list[1:4]
print("Sliced list (from index 1 to 3):", sliced_list)

# Checking if an element exists in the list
element_to_check = input("Enter an element to check if it exists in the list: ")
if element_to_check in my_list:
    print(f"✅ {element_to_check} exists in the list.")
else:
    print(f"❌ {element_to_check} does not exist in the list.")

print("Final list:", my_list)