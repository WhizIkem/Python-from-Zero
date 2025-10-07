# dictionaries are key-value pairs

dogs = {"shasha": 5, "browny": 3, "tommy": 4}

print(dogs)

# accessing a value by key
print(dogs["browny"])

# adding a new key-value pair
dogs["max"] = 2
print(dogs)

# deleting a key-value pair
del dogs["tommy"]
print(dogs)

# length of the dictionary
print(len(dogs))