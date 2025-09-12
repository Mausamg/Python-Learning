#tuples in python
# 1. Creating tuples
my_tuple = (10, 20, 30)
mixed_tuple = ("apple", 3.14, True)

print("First element:", my_tuple[0]) 
print("Slice:", my_tuple[1:3])        


# 4. Tuple concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print("Concatenated tuple:", combined)  

# 5. Tuple unpacking
x, y, z = my_tuple
print("Unpacked values:", x, y, z)  

# 6. Tuple methods: count and index
sample = (1, 2, 2, 3, 2)
print("Count of 2:", sample.count(2))    
print("Index of 3:", sample.index(3))   

# 7. Single-item tuple
single_item = (5,)
not_a_tuple = (5)
print("Single item tuple:", single_item)  
print("Not a tuple:", type(not_a_tuple))  

locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print("Location at (40.7128, -74.0060):", locations[(40.7128, -74.0060)])
