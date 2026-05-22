# 1. Accept two number and print the greatest between them 

first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number :"))
if first_number > second_number:
    print("First number is the greatest number :", first_number)
elif first_number == second_number:
    print("Both numbers are equal !")
else:
    print("Second number is the greatest number :", second_number)