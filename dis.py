# dictionary is a immutable method that means when user store a data in key value pair then users canntot change its properties
# creating dictionary 
# empty = {}
# also = dict()  #we can also create a dictionary like that

# user = {
#     "name" : "geeta" , "age" : 20 , "city": "pune"
# }
# print(user)
# user_2 = dict(name = "geeta" , age = 20 , city = "mumbai")
# print(user_2)

# print(user.keys(),user.values())
print("-------------------------billing software using python-----------------------")
print()
bill = {}

while True:
    print("\n--- Billing Software ---")
    print("1. Add Item")
    print("2. View Current Bill")
    print("3. Calculate Total & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter Item Name: ")
        price = float(input(f"Enter Price of {item}: "))
        qty = int(input(f"Enter Quantity of {item}: "))
        total = price * qty
        bill[item] = {"price": price, "quantity": qty, "total": total}
        print(f"✅ {item} added to bill.")

    elif choice == "2":
        if not bill:
            print("❌ No items in bill")
        else:
            print("\n--- Current Bill ---")
            for item, data in bill.items():
                print(f"{item}: {data['quantity']} x {data['price']} = {data['total']}")

    elif choice == "3":
        if not bill:
            print("❌ Bill is empty. Exiting...")
            break
        grand_total = sum(data["total"] for data in bill.values())
        print("\n--- Final Bill ---")
        for item, data in bill.items():
            print(f"{item}: {data['quantity']} x {data['price']} = {data['total']}")
        print(f"\n💰 Grand Total: {grand_total}")
        print("👋 Thank you for shopping!")
        break

    else:
        print("❌ Invalid choice")

