# operators are nothing but functions that take one or more arguments and return a value
# operator are used to perform operations on variables and values
# Python supports arithmetic, comparison, logical, assignment, and other operators. 
# Understanding operators is essential for performing calculations and making decisions in your code.
# Arithametic Operators (+, -, *, /, %, //, **)
print("\n")
print("..........Basic Arithmetic Operators in Python...........")
print("*"*100)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print ("Addition : ",num1 + num2)      # Addition
print ("Subtraction : ",num1 - num2)   # Subtraction
print ("Multiplication : ",num1 * num2) # Multiplication
print ("Division : ",num1 / num2)      # Division
print ("Modulus : ",num1 % num2)       # Modulus
print ("Floor Division : ",num1 // num2) # Floor Division
print ("Exponentiation : ",num1 ** num2) # Exponentiation

print("*"*100)
print("*"*100)
# Comparison Operators (==, !=, >, <, >=, <=)
12
print("..........Comparison Operators in Python...........")
print("*"*100)
number1 = int (input("Enter first number: "))
number2 = int (input("Enter second number: "))
print("Is number1 equal to number2? :", number1 == number2)   # Equal to
print("Is number1 not equal to number2? :", number1 != number2) # Not equal to
print("Is number1 greater than number2? :", number1 > number2)  # Greater than
print("Is number1 less than number2? :", number1 < number2)     # Less than
print("Is number1 greater than or equal to number2? :", number1 >= number2) # Greater than or equal to
print("Is number1 less than or equal to number2? :", number1 <= number2)    # Less than or equal to
print("*"*100)
print("*"*100)
# Logical Operators (and, or, not)
print("..........Logical Operators in Python...........")
print("*"*100)
name = input("Enter your name :")
age = int (input("Enter your age :"))
print("Is name 'geeta' and age 21? :", name == "geeta" and age == 21)
# Logical AND
print("Is name 'geeta' or age 21? :", name == "geeta" or age == 21)
# Logical OR
print("Is not name 'geeta'? :", not name == "geeta" or not age==20)
# Logical NOT
print("*"*100)
print("*"*100)  
# Assignment Operators (=, +=, -=, *=, /=, %=, //=, **=)
print("..........Assignment Operators in Python...........")
print("*"*100)
a= int(input("enter the number 1: "))
b = int (input("Enter the number 2: "))


a += b
print("After a += b, value of a:", a) #a = a+b
a -= b
print("After a -= b, value of a:", a) #a = a-b
a *= b
print("After a *= b, value of a:", a) #a = a*b
a /= b
print("After a /= b, value of a:", a) #a = a/b
a %= b
print("After a %= b, value of a:", a) #a = a%b
a //= b
print("After a //= b, value of a:", a) #a = a//b        

a **= b
print("After a **= b, value of a:", a)  #a = a**b
print("*"*100)
print("*"*100)
# Membership Operators (in, not in) 
print("..........Membership Operators in Python...........")
print("*"*100)
name = input("Enter your name: ")
print("Is 'a' present in your name? :", 'a' in name)  # Membership 'in'
print("Is 'z' not present in your name? :", 'z' not in name)
print("Is a g in your name ", 'G' not in name) # Membership 'not in'
print("*"*100)
print("*"*100)
# Identity Operators (is, is not)
print("..........Identity Operators in Python...........")
print("*"*100)
x = int (input("Enter the number 1: "))
y = int (input("Enter the number 2: "))
print("Is x is  y? :", x is y)       # Identity 'is'
print("Is x is not y? :", x is not y) # Identity 'is not'



