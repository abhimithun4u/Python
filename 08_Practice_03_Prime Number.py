# Author: Abhishek Mukherjee
# Topic: Check whether a number is Prime or Not
num = int(input("Enter The Number:- "))
Prime = True
for i in range(2, num):
    if num % i == 0:
        Prime = False

if Prime:
    print("The number", num, "is a Prime Number")
else:
    print("The number", num, "is not a Prime Number")
