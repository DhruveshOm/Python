# Data types in Python
age = 25              # Integer
height = 5.8          # Float
name = "Alice"        # String
is_student = True     # Boolean

# Print data types
print("Data Types:")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Name: {name} (Type: {type(name)})")
print(f"Is Student: {is_student} (Type: {type(is_student)})")

# Type Conversion
print("\nType Conversion:")
# Convert integer to float
age_float = float(age)
print(f"Age as float: {age_float} (Type: {type(age_float)})")

# Convert float to integer
height_int = int(height)
print(f"Height as integer: {height_int} (Type: {type(height_int)})")

# Convert integer to string
age_str = str(age)
print(f"Age as string: {age_str} (Type: {type(age_str)})")

# Convert string to integer
age_from_str = int(age_str)
print(f"Age from string: {age_from_str} (Type: {type(age_from_str)})")


# List, Set, Tuple, and Dictionary in Python
fruits_list = ["apple", "banana", "cherry"]  # List
unique_numbers_set = {1, 2, 3}            # Set
colors_tuple = ("red", "green", "blue")      # Tuple
person_dict = {"name": "Alice", "age": 25}   # Dictionary

# Print data types and examples
print("Data Types Examples:")
print(f"List of fruits: {fruits_list} (Type: {type(fruits_list)})")
print(f"Set of unique numbers: {unique_numbers_set} (Type: {type(unique_numbers_set)})")
print(f"Tuple of colors: {colors_tuple} (Type: {type(colors_tuple)})")
print(f"Dictionary of person: {person_dict} (Type: {type(person_dict)})")

# Type Conversion Examples
print("\nType Conversion:")
# Convert list to set
fruits_set = set(fruits_list)
print(f"List to set: {fruits_set} (Type: {type(fruits_set)})")

# Convert set to list
numbers_list = list(unique_numbers_set)
print(f"Set to list: {numbers_list} (Type: {type(numbers_list)})")

# Convert tuple to list
colors_list = list(colors_tuple)
print(f"Tuple to list: {colors_list} (Type: {type(colors_list)})")

# Convert list to tuple
fruits_tuple = tuple(fruits_list)
print(f"List to tuple: {fruits_tuple} (Type: {type(fruits_tuple)})")

# Convert dictionary keys to list
person_keys = list(person_dict.keys())
print(f"Dictionary keys to list: {person_keys} (Type: {type(person_keys)})")

# Convert dictionary values to list
person_values = list(person_dict.values())
print(f"Dictionary values to list: {person_values} (Type: {type(person_values)})")
