# Introduce variables in Python

# message = "Hello Python world!"
# print(message) # runs successfully
#
# message = "Hello Python Crash Course world!"
# print(message) # runs successfully

# An example of a mistake
# message = "Hello Python Crash Course world"
# # print(mesage) wrong
# print(message) #runs successfully

# 2.1 Strings

# Change case in a String with Methods

# name = "ada lovelace"
# print(name.title()) # title case
# print(name.lower())
# print(name.upper())

# 2.2 Variables in strings using f-strings
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)

# compose complete messages using the information associated with a variable:
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(f"Hello, {full_name.title()}!")

# use f-strings to compose a message and then assign the entire message to a variable:
# first_name = "ada"
# last_name = "lovelace"
# fullname = f"{first_name} {last_name}"
# message = f"Hello, {fullname.title()}"
# print(message)

# Adding white space to strings with Tabs or Newlines
# use whitespace to organize my output so it's easier for users to read

# to add a tab to my text use\t
# print("Python")
# print("\tPython") # adds four blank spaces

# to add a newline
# print("Languages: \nPython\nC\nJavaScript")

# combine tabs and newlines
#print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 2.3 Stripping whitespace
# use the rstrip method to eliminate whitespace

# favorite_language = "python "
# favorite_language # includes the white space
# favorite_language.rstrip() # eliminates the white space in printout
# favorite_language # white space is still in the variable

# To remove whitespace permanently
# favorite_language = "python "
# favorite_language = favorite_language.rstrip()
# favorite_language

# left strip
# favorite_language = " python"
# favorite_language = favorite_language.lstrip()
# favorite_language

# all strip
# favorite_language = " python "
# favorite_language = favorite_language.strip()
# favorite_language

# 2.4 Removing prefixes

# nostarch_url = 'https://nostarch.com'
# nostarch_url.removeprefix('https://')

#3.5 Avoiding syntax errors with strings

# Here's how to use single and double quotes correctly in Python
# message = "One of Python's strngths is its diverse community"
# print(message) # no problem with double quotes

# problems with single quote marks
#message = 'One of Python's strenghts is its diverse community''

# Numbers
# Integers
# 2+3
# 3/2
#
# 3**2
# 25**0.5
#

# floats
# any number with a decimal is a float in Python. The decimal point can appear in any position in a number.
0.1+0.1

0.2 + 0.1

3 * 0.1

# The ratio of any two numbers is ALWAYS a float
4/2

#If integers and floats are combined, the result is always a float
1 + 2.0

# Multiple assignments at once
x, y, z = 5, 6, 7
print(x)
print(y)
print(z)

# Constants
# If you want to treat a variable as a constant, put the name in all capital letters
MAX_CONNECTIONS = 5000
