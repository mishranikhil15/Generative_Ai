# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"


def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]


# Initial dictionary
people = {}

# Adding a new name-age pair
add_person(people, "John", 25)
print(people)

# Updating the age of a name
update_age(people, "John", 26)
print(people)

# Deleting a name from the dictionary
delete_person(people, "John")
print(people)
