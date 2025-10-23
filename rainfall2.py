rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}

# 1. Print all unique rainfall measurements for Chennai and Madurai.
unique_CM = rainfall_chennai.union(rainfall_madurai)
print("Unique rainfall (Chennai + Madurai):", unique_CM)

# 2. Merge all three readings using update() and union().
merged_update = rainfall_chennai.copy()
merged_update.update(rainfall_madurai, rainfall_coimbatore)
print("Merged using update():", merged_update)

merged_union = rainfall_chennai.union(rainfall_madurai, rainfall_coimbatore)
print("Merged using union():", merged_union)

# 3. Common Rainfall: Identify rainfall values present in all three cities.
common_rainfall = rainfall_chennai.intersection(rainfall_madurai, rainfall_coimbatore)
print("Common rainfall in all three:", common_rainfall)

# 4. Unique Chennai Rainfall: Determine unique rainfall values observed exclusively in Chennai.
unique_chennai = rainfall_chennai - rainfall_madurai - rainfall_coimbatore
print("Unique rainfall in Chennai:", unique_chennai)

# 5. Rainfall in at least Two Cities: Find rainfall values recorded in a minimum of two cities.
at_least_two = (rainfall_chennai & rainfall_madurai) | \
               (rainfall_madurai & rainfall_coimbatore) | \
               (rainfall_chennai & rainfall_coimbatore)
print("Rainfall in at least two cities:", at_least_two)

# 6. Create a new set where every rainfall value is increased by 10.
increased_rainfall = {value + 10 for value in rainfall_chennai}
print("Rainfall values increased by 10:", increased_rainfall)