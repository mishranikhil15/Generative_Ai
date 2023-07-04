### **Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

tuple1 = (11, [22, 33], 44, 55)

modified_list = list(tuple1)  # Convert the tuple to a list
modified_list[1][0] = 222  # Modify the first item of the list
modified_tuple = tuple(modified_list)  # Convert the list back to a tuple

print(modified_tuple)
