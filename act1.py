fruits = ("apple", "banana", "cherry", "mango", "banana")

# #1) Determine the length of the fruits tuple.
# print(len(fruits))

# #2) Identify the index of the initial occurrence of "banana".
# element = "banana"
# print(fruits.index(element))

# #3) Attempt to modify "cherry" to "grape" within the tuple. 
# #Explain the outcome and the reason behind it.

# change = list(fruits)
# change[2] = "grape"
# fruits = tuple(change)

# print(fruits)

# #4) Transform the tuple into a list, make a modification, and then convert it back to a tuple.
# list_ = list(fruits)
# print(list_)
# tuple_ = tuple(list_)
# print(tuple_)