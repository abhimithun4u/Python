# Author: Abhishek Mukherjee
# Find string in a list

names = ["Abhishek","Arnab","Rohit","Mandy","Priya","Saanvi"]
namelist = [x.lower() for x in names]
# print(namelist)
name = input("Enter the name to search :-  ").lower()
# print(name)
if name in namelist:
    print("The Name is available!")
else:
    print("The Name is not available! ")