# real world project using lists , loop and conditional statements
# project: simple todo list application
todo_list=[]
def display_menu():
    print("\nTodo List Application")
    print("1. View Todo List")
    print("2. Add Todo Item")
    print("3. Remove Todo Item")
    print("4. Exit")
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        print("Todo List:")
        for index, item in enumerate(todo_list):
            print(f"{index + 1}. {item}")
    elif choice == "2":
        new_item = input("Enter a new todo item: ")
        todo_list.append(new_item)
        print(f"Added todo item: {new_item}")
    elif choice == "3":
        item_number = int(input("Enter the item number to remove: "))
        if 1 <= item_number <= len(todo_list):
            removed_item = todo_list.pop(item_number - 1)
            print(f"Removed todo item: {removed_item}")
        else:
            print("Invalid item number.")
    elif choice == "4":
        print("Exiting Todo List Application.")
        break
    else:
        print("Invalid choice. Please try again.")

# grocery shopping list application
grocery_list = []

def display_grocery_menu():
    print("\nGrocery Shopping List Application")
    print("1. View Grocery List")
    print("2. Add Grocery Item")
    print("3. Remove Grocery Item")
    print("4. Exit")

while True:
    display_grocery_menu()
    choice = input("Enter your chioce(1-4):")

    if choice =="1":
        print("grocery list: ")
        for index, items in enumerate(grocery_list):
            print(f"{index + 1}. {items}")
    elif choice =="2":
        new_item = input("Enter the grocery item to add:")
        grocery_list.append(new_item)
        print(f"Added grocery item:{new_item}")
    elif choice =="3":
        item_number = int(input("Enter the item number to 4" \
        "remove: "))
        if 1 <= item_number <= len(grocery_list):
            removed_item = grocery_list.pop(item_number - 1)
            print(f"Removed grocery item: {removed_item}")
    elif choice =="4":
        print("Exiting Grocery Shopping List Application.")
        break

    else:
        print("Invalid item number.")


