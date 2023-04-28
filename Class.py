# Nested Loops
# Nested Loops means adding one loop inside another loop

# Syntax example of nested Loops

# print("Here are your coordinates")
# for x in range(4):                    # Outer Loop
#   for y in range(5):                  # First Inner loop
#       for z in range(6):              # Second Inner Loop
#           print(f'({x}, {y}, {z})')


# Loops will work from outer loop to inner loops
# it will occur iteration wise

# Code to write letter 'R'

# print('xxxx')
# print('x  x')
# print('xxxx')
# print('x')
# print('x x')
# print('x  x')

# Write letter 'R' using Nested Loop

# numbers = [4,4,4,1,3,4]
# for x_count in numbers:
#    output = ''
#    for count in range(x_count):
#        for count2 in range(x_count , 2):
#            for count3 in range(x_count):
#                for count4 in range(x_count):
#                    for count5 in range(x_count , 1):
#                        for count6 in range(x_count , 2):
#                            output += 'x'
#    print(output)

# str="";
# for Row in range(0,7):
#    for Col in range(0,7):
#        if (Col == 1 or ((Row == 0 or Row == 3) and Col > 1 and Col < 5) or (Col == 5 and Row != 0 and Row < 3) or (Col == Row - 1 and Row > 2)):
#           str=str+"*"
#        else:
#            str=str+" "
#    str=str+"\n"
# 1print(str);

# Example of Dominos number using nested for loop
# for left in range(8):
#    for right in range(left, 7):
#        print("[" + str(left) + "|" + str(right) + "]", end=" ")
#    print()

# Example of team match fixtures
# teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:
#        if home_team != away_team:
#            print(home_team + " vs " + away_team)





# Lists in Python

# Lists store values and we can access it

# 2D Lists
# These are extremely powerful and they have a lot of applications in data science and machine learning
# Prime example is mathematical matrix

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]                           # This is a 2D List, each item in the outer list is in an inner list

# print(matrix[2][0])         # Here 2 is a outer list and 0 is the index position of the number in the inner list

# for row in matrix
# for item in row:
# print(item)                 # Here we can use for loop to get the rows of the matrix in an 'item' variable

# List Methods/List Functions
# these are the operations we can perform on the list

# Example Define list of numbers

# numbers = [5, 2, 1, 7, 4]
# numbers.append(14)            # Append function adds the object at the end
# print(numbers)

# numbers.insert(3, 6)          # insert function inserts the object, we need to add the index where we need to add the object then the object
# print(numbers)

# pop function removes the object from the list
# index function tells the position of the object
# count function tells the occurence of the object
# copy function copies the list

# Exercise - delete a duplicate value from the list

# numbers = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10]
# unique = []                                       # We will make a seperate empty list
# for number in numbers:                            # apply for loop
#   if number not in unique:                         # this if condition states that if do not have the value in unique then we will need to add it
#       unique.append(number)
# print(unique)

# Exercise to delete inserted duplicate value from the list

digits = [int(input("Enter the numbers - "))]
print(digits)
digits_2 = []
for number in digits:
    if number not in digits_2:
        digits_2.append(digits)
print(digits_2)

