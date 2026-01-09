students = int(input("Enter number of students: "))
present = 0

for i in range(1, students + 1):
    status = input(f"Student {i} (P/A): ").upper()
    if status == "P":
        present += 1

print("Total Present:", present)
print("Total Absent:", students - present)

# banking system
balance = 5000

while balance > 0:
    print("Balance:", balance)
    withdraw = int(input("Enter amount (0 to exit): "))

    if withdraw == 0:
        break
    elif withdraw > balance:
        print("Insufficient balance")
    else:
        balance -= withdraw
        print("Withdraw successful")

print("Thank you for using ATM")

# password validation
print("Welcome to Password Validator")
password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special characters:", special)

if upper >= 1 and lower >= 1 and digit >= 1 and special >= 1 and len(password) >= 8:
    print("Password Strength: STRONG ")
else:
    print("Password Strength: WEAK ")
