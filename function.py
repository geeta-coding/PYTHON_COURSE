# funtion is a block of code and it is use for reusable a code and not nesscary for the repition a logic
# function is defined satring with def keyword
# for example
print("----------------   Function basic   ---------------")

# def greet():
#     print("good morning")

# name = input("enter your name: ")
# print(f"your name is {name} ")
# greet()

# def greet(name):
#     print(f"your good name is {name}")

# greet("Geeta")

# def add (a,b):
#     return a+b

# print(add(20,2))

# print("----------------   default Paramenters   ---------------")

# print()
# def greet(name,greet = "Welcome"):
#     return f"{name} {greet}"

# print(greet("geeta","good night"))

# print("----------------   multiple default   ---------------")
# print()

# def profile(name,age=18,country="india"):
#     return {
#         "name":name,
#         "age" : age,
#         "country": country
#     }

# result = profile("geeta",21)
# print(result)

# lambda function that means anonyms function
# this is a single line function
# squre = lambda x: x*x
# print(squre(2))

# add = lambda a,b: a+b
# print(add(20,30))

print("Real World project using function ")
print()

def login(username,password):
    if username=="admin" and password ==1234:
        print("Login sussfully completed")
    else:
        print("Login Failed")

login("admin",1234)


print("----------  Withdrawl ---------------")
print()
def bank(balance,amount):
    if balance>=amount:
        balance -=amount
        print("WITHDRAWAL COMPLETED")
    else:
        print("insuffient balance")

bank(200,200)