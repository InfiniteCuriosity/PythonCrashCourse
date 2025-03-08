# Store the names of a few of your friends in a list called names. Print each friend's name, one at a time

names = ["John", "Paul", "George", "Ringo"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-4 Guest List - make a list of 3-4 people I'd like to ask to dinner, then print a message to each person

list_of_guests = ['DaVinci', 'Jesus', 'mom']
message = ['What made you so creative', 'What would you like to tell the world', 'Thank you!']
print(list_of_guests[0], message[0])
print(list_of_guests[1], message[1])
print(list_of_guests[2], message[2])

# Changing guest list = someone can't make it, need to invite someone else

list_of_guests.pop(0)
list_of_guests.append('St. Paul')
list_of_guests
message.pop(0)
message.append('You wrote a lot')
message.append('a message')

print(list_of_guests[0], message[0])
print(list_of_guests[1], message[1])
print(list_of_guests[2], message[2])

#Bigger dinner table, need to invite more people
# Start with the list of people. Add a print() command to let people know I found a bigger table
message = "I have a bigger table"
print(f"{list_of_guests} {message}")

# use insert to add one new guest to the beginning of the list
list_of_guests.insert(0, "Idunno")
print(list_of_guests)
list_of_guests.insert(2, "Idunno2")
list_of_guests
list_of_guests.insert(4, "Idunno3")
list_of_guests

# Add a line that I can only have two people at the table, sorry about that
sorry_message = "I can only have two people, sorry about that"
list_of_guests.pop(0)
print(list_of_guests[0], sorry_message)

