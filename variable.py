# --------------------------------------------------
# Declaring variables in Python
# Always use meaningful variable names
# --------------------------------------------------

a = "city"                 # Non-descriptive variable name (not recommended)
city_name = "Pune"         # Descriptive variable name
user_name = "Geeta Raut"
user_password = 1234       # Descriptive variable name

print(city_name, user_name, user_password)

# --------------------------------------------------
# Python Variable Naming Rules:
# 1. Must start with a letter or underscore
# 2. Can contain letters, digits, underscores
# 3. Case-sensitive
# --------------------------------------------------

# --------------------------------------------------
# Taking input from the user
# input() always returns string data
# --------------------------------------------------

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

print("Hello,", user_name)
print("You are", user_age, "years old.")

# Using f-string for formatted output
print(f"Hello, {user_name}. You are {user_age} years old.")

# --------------------------------------------------
# Type Casting Example
# Converting string input into integer
# --------------------------------------------------

number = input("Enter a number: ")
print("Type before type casting:", type(number))

number = int(number)
print("Type after type casting:", type(number))

# --------------------------------------------------
# Addition of two numbers after type casting
# --------------------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}.")

# --------------------------------------------------
# Real-world example: BMI Calculator
# --------------------------------------------------

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}.")
