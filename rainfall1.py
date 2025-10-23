rainfall_data = {120, 150, 180, 120, 90, 110, 130}

# 1. How many rainfall values are in the set?
print("Number of rainfall values:", len(rainfall_data))

# 2. Can you directly change the value of an item in a set?
try:
    rainfall_data[0] = 200
except TypeError as e:
    print("Error:", e)

# 3. Check if 150 is present inside rainfall_data.
print("Is 150 present?", 150 in rainfall_data)

# 4. Convert the set to a list.
rainfall_list = list(rainfall_data)
print("Converted to list:", rainfall_list)

# 5. Print every rainfall value by traversing through the set.
print("Rainfall values:")
for value in rainfall_data:
    print(value)

# 6. Remove the value 120 from the above set.
rainfall_data.remove(120)
print("After removing 120:", rainfall_data)

# 7. Add the value 110 to the above set and observe changes.
rainfall_data.add(110)
print("After adding 110 again:", rainfall_data)
print("Note: 110 does not appear twice because sets store only unique values.\n")
