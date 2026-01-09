# this is looping or control flow in python
# lopps are uesd to repate a block of code multiple time and also reduce a code redundancy
# there are two types of loops in python
# 1. for loop
# 2. while loop
print("for loop example")
# for loop
for i in range(5):
    print("hello ") # this will print hello 5 times

for i in range (1,10,2): # starting index 1 to 10 with step 2
    print(i) # this will print odd numbers between 1 and 10

for i in "python": # iterating through a string
    print(i) # this will print each character of the string python

for i in range(100,200):
    print(i)

print("while loop example")
# while loop
count =  0
while count < 5:
    print("hello world") # this will print hello world 5 times
    count += 1 # incrementing the count variable to avoid infinite loop

# also we use infinite loop using while loop
# while True:
#     print("infinite loop") # this will print infinite loop forever
# to break the infinite loop we can use break statement
print("break statement example")
count = 0
while True:
    print("hello infinite loop")
    count += 1
    if count == 5:
        break # this will break the loop when count is 5
print("loop ended")

