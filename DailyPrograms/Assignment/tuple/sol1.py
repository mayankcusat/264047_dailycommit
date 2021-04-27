# Write a Python program to convert a list of tuples into a dictionary
tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
result = {}
for (key, value) in tuples:

   result.setdefault(key, []).append(value)
print(result)