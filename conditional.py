# condtional statements in Python
# conditional statements are used to perform different actions based on different conditions.
# The most common conditional statements are if, elif, and else.
# Example of if statement
age = int(input("Enter your age :"))

if age >= 18:
    print("you can drive a car")
else:
    print ("you can not drive a car")

# elif satatement
Marks = int(input("Enter your marks :"))
if Marks >=90:
    print("A grade")
elif Marks >=75:
    print("B grade")
elif Marks >=60:
    print("C grade")
elif Marks >=45:
    print("D grade")
else:
    print("Fail")
    print("study hard")
# nested if statement
num = int(input("Enter a number :"))
if num >=0:
    if num ==0:
        print("The number is zero")
    elif num >0:
        print("The number is positive")
    else:
        print("The number is negative")
else :
    print("existing......")

# conditional expression (ternary operator)
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
max_num = a if a > b else b
print("The maximum number is :", max_num)

# we are use a independentation we cannot use a {} brackets in python
# instead of that we use indentation to define a block of code
# indentation is very important in python

