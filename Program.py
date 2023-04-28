# Weight Converter Program

# weight = int(input('Enter your weight - '))
# unit = input('(L) for pounds or (K) for kilograms - ')
# if unit.upper() == "L":                         # we used upper function so that weight unit input is not case sensitive
#    converted = weight * 0.45
#    print(f"you are {converted} Kilograms")
# else:
#    converted = weight / 0.45
#     print(f"you are {converted} pounds")


# While Loops

# While loops is used to execute a block of code multiple times
# Syntax example of while loop
# i = 1
# while i <= 29 :
#    print(i)
#     i = i +2
# print("Done, Finished that's it.")

# Guess Game Sample Code

# guess_num = 4
# guess_count = 0
# guess_limit = 4
# while guess_count < guess_limit:
#     guess_data = int(input('Guess: '))
#    guess_count +=1
#    if guess_data == guess_num:
#        print("Winner")
#        break                               # Break statement terminates the loop
#    else:                                   # While statement also has an statement to execute the next code
#        print("You Lose")

# Guess the sample name

# guess_value = 'Tree'
# guess_count = 0
# guess_limit = 4
# while guess_count < guess_limit:
#    print('Hint, this gives us fruits')
#    guess_data = input('Guess the word: ')
#     guess_count += 1
#    if guess_data == guess_value:
#         print('Correct Guess')
#        break
#    elif guess_data != guess_value:
#        print('Wrong Guess, try again')

#    else:
#        print('Wrong Guess')

# For Loop
# For Loops are used to iterate items over collection like a string

# Example of for loops

# for objects in ['python']: # [] this will print the value in variable in a line
#   print(object)               # Normal quotes will print value in variable in each row

# Range function in a loop
# this is used when we need to print large values

# for item in range(2, 38):
#   print(item)
# print("Here's your list")

# total bill of shopping cart

# prices = [10, 20, 30]
# total = 0
# for price in prices:
# total += price
# print(f"Total: {Total}")

# Make a basic POS Calculator for entered items

# total_bill = 0
# print("Enter the items you want to bill:  ")
# billed_items = int(input())
# print("Enter the price of " + str(billed_items) +  " items")
# for idd_value_itm in range(billed_items):         # here we need to assign a unique variable to store the values in range
#    amount = int(input())
#    total_bill = total_bill+amount
# print("Total bill of "  + str(billed_items) + " Items is "  + str(total_bill))


