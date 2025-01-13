# Python Variable Assignments Practice

# Practice: Assign your own values to variables below and print their types
# Example:
# my_var = "Your value here"
# print("My Variable:", my_var, "Type:", type(my_var))

# Assigning different data types to variables
integer_var = ___
float_var = ___
string_var = ___
boolean_var = ___
list_var = ___
tuple_var = ___
set_var = ___
dict_var = ___


# Grabbing values from a list, tuple, and dictionary and modifying the contents

# List example: fill in the blanks with your values
my_list = [___, ___, ___, ___, ___, ___, ___, ___, ___]
print("Original List:", my_list)

#modify the 3rd element of the list
my_list[___] = ___  # Modify the ___ element
print("Modified List:", my_list)

# Tuple example: fill in the blanks with your values
my_tuple = (___, ___, ___, ___, ___, ___, ___, ___, ___)
print("Original Tuple:", my_tuple)

# Tuples are immutable, so we need to convert it to a list to modify it
temp_list = list(my_tuple)

#modify the 2nd entry in this tuple
temp_list[___] = ___  # Modify the ___ element
my_tuple = tuple(temp_list)

print("Modified Tuple:", my_tuple)

# Dictionary example: fill in the key-value pair for this dictionary
my_dict = {'': ___, '': ___, '': ___}
print("Original Dictionary:", my_dict)

#modify the value for the second key to be the value of the first key
my_dict['___'] = ___  # Modify the value for key '___'
print("Modified Dictionary:", my_dict)