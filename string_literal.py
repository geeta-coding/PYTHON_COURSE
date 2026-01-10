# string is most important in programming
new_string = "Hello, World!"
print(new_string)
another_string = 'Python is fun!'
print(another_string)
multi_line_string = """This is a string
that spans multiple lines."""
print(multi_line_string)

# string contatenation
User_name = input("Enter your name: ")
user_greeting = "Hello, " + User_name + "!"

print(user_greeting)

# string repetition
long_yes = "Yes! " * 5
print(long_yes)

# string indexing
message = "I LOVE PYTHON PROGRAMMING"
access_char = message[7]
access_char2 = message[0]

print("Character at index 7:", access_char)
print("Character at index 0:", access_char2)

# string slicing
sliced_string = message[2:6]
print("Sliced string (index 2 to 5):", sliced_string)
sliced_string2 = message[:4]

print("Sliced string (start to index 3):", sliced_string2)
sliced_string3 = message[10:]

print("Sliced string (index 10 to end):", sliced_string3)
sliced_string4 = message[:]

print("Sliced string (entire string):", sliced_string4)
sliced_string5 = message[-11:-1]

print("Sliced string (negative indices -11 to -2):", sliced_string5)
sliced_string6 = message[-1:-12:-1]

print("Sliced string (negative indices -1 to -11, step -1):", sliced_string6)
sliced_string7 = message[::2]

print("Sliced string (every second character):", sliced_string7)
sliced_string8 = message[::-1]

print("Sliced string (reversed):", sliced_string8)
sliced_string9 = message[5:15:3]

print("Sliced string (index 5 to 14, step 3):", sliced_string9)
sliced_string10 = message[-5::-2]

print("Sliced string (from index -5 to start, step -2):", sliced_string10)

# string methods
original_string = "  Hello, Python Programmers!  "
upper_string = original_string.upper()
print("Uppercase:", upper_string)


lower_string = original_string.lower()
print("Lowercase:", lower_string)

stripped_string = original_string.strip()
print("Stripped:", stripped_string)

replaced_string = original_string.replace("Python", "Java")
print("Replaced:", replaced_string)

split_string = original_string.split(",")
print("Split:", split_string)

joined_string = " ".join(["Join", "these", "words"])
print("Joined:", joined_string)

find_index = original_string.find("Python")
print("Index of 'Python':", find_index)

count_occurrences = original_string.count("o")
print("Occurrences of 'o':", count_occurrences)

starts_with = original_string.startswith("  Hello")
print("Starts with '  Hello':", starts_with)

ends_with = original_string.endswith("!  ")
print("Ends with '!  ':", ends_with)

capitalized_string = original_string.capitalize()
print("Capitalized:", capitalized_string)

title_string = original_string.title()
print("Title Case:", title_string)

centered_string = original_string.center(40, '*')
print("Centered:", centered_string)

# formatted strings
name = "Alice"
age = 30

formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string2)

formatted_string3 = "My name is %s and I am %d years old." % (name, age)
print(formatted_string3)

formatted_string4 = "My name is {0} and I am {1} years old.".format(name, age)
print(formatted_string4)

formatted_string5 = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(formatted_string5)

formatted_string6 = f"My name is {name.upper()} and I will be {age + 1} next year."
print(formatted_string6)

formatted_string7 = f"My name is {name:<4} and I am {age:03} years old."
print(formatted_string7)
