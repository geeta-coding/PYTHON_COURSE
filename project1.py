# LOGIN VALIDATION SYSTEM
print("*"*100)
print("Login Validation System")
username = "Main Admin"
password = "Admin@1234"

input_username = input("Enter the username : ")
user_password = input("Enter the password : ")

validation = (username == input_username) and (password == user_password)
print(validation)

print("Access Granted" if validation else "Access Denied")
# --------------------------------------------------------------------------------------

print("*"*100)
print("Form validation system")
name = "admin"
email = "geeta@gmail.com"
passwor= "Geeta123"

Name = input("Enter your name : ")
Email = input("Enter your Email :")
password_1 = input("Enter your password :")

form_fillter = (name == Name ) and (email == Email) and (passwor == password_1)
print("Valid form" if form_fillter else "Invalid form")

# -----------------------------------------------------------------------------------------
print("*"*100)

print("Login Existing User System")
loggeed_username = True
existing_password = False
access = loggeed_username and  existing_password
print("Access Granted" if access else "Access Denied")
# -----------------------------------------------------------------------------------------
print("*"*100)


