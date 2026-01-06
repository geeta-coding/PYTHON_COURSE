# declaring variables in Python.always use meaningful variable names that reflect the purpose of the variable.
a= "city"#  this is non- descriptive variable name
city_name = "Pune"
user = "geeta raut"
user_password = 1234 # this is descriptive variable name
print(city_name, user, user_password)

# Python variable naming rules:
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# 2. The rest of the variable name can contain letters, digits (0-9), or underscores.
# 3. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
# ***********************************************************************************************************
# in python we use a input() function to take input from the user.
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello,", user_name)
print("You are", user_age, "years old.")

#  also we can use a f-string to format the output it is used to embed expressions inside string literals, using curly braces {}.

print(f"Hello, {user_name}. You are {user_age} years old.")
# now you try it yourself
#for example take a input from customers  for their name , favorite dish and the price of the dish and print it using f-string
# dish_name = input("Enter your favorite dish: ")
# dish_price = input("Enter the price of the dish: ")
# print(f"Your favorite dish is {dish_name} and it costs {dish_price}.")
# *****************************************************************************************************

# in python there is  type casting is also possible it is used to convert one data type to another.
a = input("Enter a number: ") # by default input() function takes input as a string
print("Type of a before type casting:", type(a))       
a = int(a) # type casting string to integer
print("Type of a after type casting:", type(a))

# now you try it yourself
# in python it is work properly the calucluation of two numbers after type casting
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num1 = float(num1) # type casting string to float
num2 = float(num2) # type casting string to float
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}.")
# *****************************************************************************************************

# also  we can  convert the data type when we need it in input() function
height = float(input("Enter your height in meters: ")) # type casting input to float
weight = float(input("Enter your weight in kilograms: ")) # type casting input to float
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}.")
# BMI (Body Mass Index) is a measure of body fat based on height and weight.

