marks = (78, 85, 69, 90, 85)

#1) Determine the highest and lowest marks.
Highest_Mark = max(marks)
Lowest_Mark = min(marks)

print("Highest Mark:", Highest_Mark)
print("Lowest Mark:", Lowest_Mark)

#2) Count the occurrences of the mark 85.
occurrence = marks.count(85)
print(occurrence)

#3) Calculate the average marks using the sum() and len() functions.
average = sum(marks)/ len(marks)
print(average)