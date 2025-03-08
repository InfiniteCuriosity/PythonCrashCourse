# 3.1 What is a list?
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list
# Pull the first item in our list:

bicycles[0]

# Use methods to format the elements in the output:

print(bicycles[0].upper())
print(bicycles[0].title())
print(bicycles[0].lower())

# Index positions start at 0, not 1

# to get the 2nd and 4th items in our list:

print(bicycles[1]) # 2nd item on the list
print(bicycles[3]) # 4th item on the list

# special Python code to access the last item in a list
bicycles[-1]

# Using individual values in a list
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# Adding elements to the end of a list
# use the .append method

names.append("Russ")
print(names)

# Start with an empty list, and add the elements 'honda', 'yamaha', and 'suzuki'
empty_list = []
empty_list.append('honda')
empty_list.append('suzuki')
empty_list.append('yamaha')
print(empty_list)

# Inserting elements into a list
empty_list.insert(0, 'Harley Davidson')
print(empty_list)

# Removing items from a list
# uses the del statement

del(empty_list[0])
print(empty_list)

# How to remove the 2nd item in the list
del(empty_list[1])
print(empty_list)

# removing items using the pop method
# The pop item lets me remove the last item from a list, and lets me work with it after removing it

popped_empty_list = empty_list.pop()
print(popped_empty_list) # Yamaha
print(empty_list) # honda

# popping items from any location in a list

# Include the idex of the item I want to remove

empty_list.append('Harley Davidson')
empty_list.append('Suzuki')
print(empty_list)

first_owned = empty_list.pop(0)
print(f"The first motorcyele I owned was a", first_owned)

# Removing an item by its value
print(empty_list)

empty_list.remove('Suzuki')
print(empty_list)

# Let's remove a value and print the reason we are removing it

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive) # no single or double quote marks
print(motorcycles) # it works fine

## Organizing a list
# Sorting a list permanently with the sort() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Temp sorting of a list
print(sorted(cars))
print("Here is the original list")
print(cars)

# To do this in reverse order, use the reverse() method
cars.reverse()
print(cars)

# finding the length of a list
len(cars)