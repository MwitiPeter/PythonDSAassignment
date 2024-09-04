# Initialize an empty list
my_list = []

# Append multiple elements at once (use `extend` instead)
my_list.extend([10, 20, 30, 40])
print(my_list)  

# Modify an element at index 1
my_list[1] = 15
print(my_list)  

# Extend the list with another list
another_list = [50, 60, 70]
my_list.extend(another_list)
print(my_list)  

# Sort the list in ascending order
my_list.sort()
print(my_list)  

# Find the index of a specific value
number = 30
print(my_list.index(number)) 
