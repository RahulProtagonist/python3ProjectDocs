# Dictionary Program to convert entered phone number into text

phone = input("Enter the phone number: ")
Number_digit = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",                        # This will be our dictionary to convert the digits into letters
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "10" : "Ten"
}

output = ""
for dg in phone:
    output += Number_digit.get(dg)
print("Entered Digits in words are " + f"{output}")