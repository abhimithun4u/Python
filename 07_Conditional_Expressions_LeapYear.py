# Author: Abhishek Mukherjee
# Conditional Expressions : if, elif, else to calculate leap year

num = int(input("Enter the Year: "))
if num % 4 == 0 and num % 400 == 0:
    print("The year ", num, " is a leap year!")
elif num % 100 == 0 and num % 400 == 0:
    print("The year ", num, " is a leap year!")
else:
    print("The year ", num, " is a not a leap year!")
