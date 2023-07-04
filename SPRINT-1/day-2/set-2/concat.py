### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

concatenated_list = []

min_length = min(len(list1), len(list2))  # Get the minimum length of the two lists

for i in range(min_length):
    concatenated_list.append(list1[i] + list2[i])

# Add any leftover items from list1 or list2
concatenated_list.extend(list1[min_length:])
concatenated_list.extend(list2[min_length:])

print(concatenated_list)
