colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")

#1) Combine colors and shapes to create a new tuple called art.
tuple_arts = (colors + shapes)
print(tuple_arts)

#2) Demonstrate how to repeat a tuple, specifically colors three times.
tuple_arts = (colors* 3)
print(tuple_arts)

#3) Add an art element called “Diamond” to the art tuple.
tuple_arts += ("Diamond",)
print(tuple_arts)

#4) Extract and print the middle element from the art tuple using slicing.
middle = int(len(tuple_arts) / 2)
middle_element = tuple_arts[middle]
print(middle_element)

#5) Verify if the string "square" exists within the art tuple.
check = "polygon" in tuple_arts
print(check)
