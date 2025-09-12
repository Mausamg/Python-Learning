# Creating a set
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}  (duplicate '4' removed)

# Adding an element
my_set.add(6)

# Removing an element
my_set.remove(2)

print(my_set)  # Output: {1, 3, 4, 5, 6}


# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing a value
print(my_dict["name"]) 

# Adding a new key-value pair
my_dict["job"] = "Engineer"

# Changing a value
my_dict["age"] = 26

print(my_dict)
#
