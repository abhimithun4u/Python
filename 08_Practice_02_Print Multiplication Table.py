# Author: Abhishek Mukherjee
# Topic: Print multiplication table using for loop
num = int(input("Enter the Number:-  "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
