# Atm banking system
print("*"*100)
print("...........Atm Banking System...........\n")
print("Welcome to ATM banking system\t")

account_number = "abc123"
pin = "1234"
balance = 5000

enter_pin = input("Enter your pin : ")  # user input for pin

if enter_pin ==pin:  # this is main if condition to check pin validity
    print("pin is valid..")           
    print("choose your transaction :")
    print("1.check bank balance")   #this is manu driven 
    print("2.withdraw money")
    print("3.deposit money")

    choice =int(input("Enter your choice (1-3) : "))  #choose transaction
    if choice ==1:
        print(f"Your bank balance is :{balance}") #it is show your actual balance
   
    elif choice ==2: 
        print("Withdraw money")
        amount = int(input("Enter amount to withdraw : "))  #user input for withdraw amount
        if amount <= balance:                                     #check withdraw amount is less than or equal to balance 
            balance = balance - amount
            print(f"please collect your money here :{amount}")
            print(f"Now your balance is :{balance}")
        else:
            print("Insufficient balance. ")
   
    elif choice ==3:
        print("deposit money ")
        deposit_amount =int (input("Enter the amount for deposit: "))
        if deposit_amount>0:
            balance = balance + deposit_amount
            print(f"Successfully deposited your money :{deposit_amount}")
            print(f"Now your balance is :{balance}")
        else:
            print("Make sure you enter a valid amount. minimum deposit amount is 1")

else:
    print("Invalid pin. Access Denied.")

    # -----------------------------------------------------------------------------------------

    print("*"*100)  
print("Mobile Recharge System")
plan = int(input("Enter your recharge plan amount (199/299/399):"))

if plan ==199:
    print("You have selected the 199 plan with 1.5GB/day data and unlimited calls.")
elif plan ==299:
    print("You have selected the 299 plan with 2.5GB/day data and unlimited calls.")
elif plan ==399:
    print("You have selected the 399 plan with 3.5GB/day data and unlimited calls.")
else:
    print("Invalid plan selected. Please choose a valid plan.")

# -----------------------------------------------------------------------------------------


print("*"*100)  
print("Electricity Bill Payment System")
units = int(input("Enter the number of electricity units consumed: "))
if units <= 100:
    bill = units * 5
    print(f"Your electricity bill is: {bill}")
elif units <= 200:
    bill = units * 7
    print(f"Your electricity bill is: {bill}")
else:
    bill = units * 10
    print(f"Your electricity bill is: {bill}")


        