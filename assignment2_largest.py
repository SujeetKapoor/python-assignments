# PRN      : 1272261997
# Name     : Sujeet Kapoor
# Division : 9
# Branch   : CSE (AI-DS)
# Subject  : Python
# Assignment 2 : Find the largest of three numbers


# Take three numbers from the user
num1 = float(input("Enter the first number  : "))
num2 = float(input("Enter the second number : "))
num3 = float(input("Enter the third number  : "))

# Compare them to find the largest
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("\nThe largest number is:", largest)
