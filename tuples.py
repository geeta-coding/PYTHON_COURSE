# tuples are immutable method
# tuples are similar to the list it is cretae using ()
# tup = (1,2,3,"toy","name",80)
# print(type(tup),tup)
# print(tup[1])
# print(tup[2])
# tup[1]=50  --------we co=annot change the values in that tuples 
# if "toy" in tup:
#     print("YES!! THIS IS IN A TUPLES")
# else:
#     print("NO !!IT IS NOT IN TUPLES")

# ----------------------------------------------------------------------------------------------------------------

print("-------------------\t\t\t real world project using tuples\t\t\t------------------------")
print()


students = []   # list to store multiple student tuples

while True:
    print("1. Add student details")
    print("2. View student details")
    print("3. Exit the program")

    user_choice = int(input("Enter your choice (1-3): "))

    if user_choice == 1:
        roll = int(input("Enter the roll no: "))
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))

        sgpa = (marks / 500) * 10   # correct SGPA calculation

        student = (roll, name, marks, sgpa)  # tuple
        students.append(student)             # add tuple to list

        print("Student added successfully!\n")

    elif user_choice == 2:
        if not students:
            print("No student records found!\n")
        else:
            print("\nStudent Details:")
            for s in students:
                print("Roll:", s[0],
                      "Name:", s[1],
                      "Marks:", s[2],
                      "SGPA:", round(s[3], 2))
            print()

    else:
        print("Exiting program... Thank you!")
        break
        

