# Dictionary method: https://www.geeksforgeeks.org/python-dictionary/

# 1. fromkeys(seq,value):- This method is used to declare a new dictionary from the sequence mentioned in its arguments.
# 2. update(dic):- This function is used to update the dictionary to add other dictionary keys.
# 3. has_key():- This function returns true if specified key is present in the dictionary, else returns false.
# 4. get(key, def_val) :- This function return the key value associated with the key mentioned in arguments. If key is not present, the default value is returned.
# 5. setdefault(key, def_value):- This function also searches for a key and displays its value like get() but, it creates new key with def_value if key is not present.
# 6. values(): -  This function returns a list of all the values available in a given dictionary.
# 7. keys(): - Returns list of dictionary dict’s keys
# 8. items(): - Returns a list of dict’s (key, value) tuple pairs


# 1
numbers = [1, 2, 3, 4, 5]

new_dict1 = dict.fromkeys(numbers, 0)
# using dict. comprehension
new_dict2 = {i: 0 for i in numbers}

print(f"New dict 1: {new_dict1}")
print(f"New dict 2: {new_dict2}")

# using fromkeys() to convert sequence to dict 
res_dict2 = {key: list(numbers) for key in numbers}

print(f"The newly created dict with list values: {str(res_dict2)}")

# 5
# Method has two cases: 1) if the key is in dictionary 2) when key is not in the dictionary
dict_names = {'A': 'Anna', 'B': 'Bob', 'C': 'Charly'}

third_value = dict_names.setdefault('C')
print(f"Dictionary: {dict_names}")
# Method returns the value of a key
print(f"Third_value: {third_value}")

fourth_value = dict_names.setdefault('D', 'Dima')
print(f"Dictionary: {dict_names}")
# Set new (key, value) to the dictionary
print(f"Fourth_value: {fourth_value}")
