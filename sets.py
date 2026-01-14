# num = {1,2,45,34,2,2}
# # fruit ={
# #     "name" : "Geeta",
# #     "age" : 20,
#     # "marks":95
# # }
# # print(type(fruit))
# print(type(num))
# print(num)

# # sets are a unique method and also it is a immutable this not change when declare and also set() is used for
# # set is defined in { } curly braces and also print shuffuling the data 
# num = {1, 2, 45, 34, 2, 2}
# print(type(num))
# print(num)

print("---------------Voter System---------------")
print()

voted_users = set()
voter_a = set()
voter_b = set()

while True:
    print("\n1. Vote")
    print("2. View Result")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        voter_id = input("Enter Your Id : ")

        if voter_id in voted_users:
            print("❌ Only one vote allowed")
        else:
            print("Vote For >>>>>>>>>>\n")
            print("A: BJP")
            print("B: Other")

            vote = input("Enter your vote (A/B): ").upper()

            if vote == "A":
                voter_a.add(voter_id)
                voted_users.add(voter_id)
                print("✅ Vote cast for Candidate A")

            elif vote == "B":
                voter_b.add(voter_id)
                voted_users.add(voter_id)
                print("✅ Vote cast for Candidate B")

            else:
                print("❌ Invalid vote")

    elif choice == "2":
        print("\n--- Results ---")
        print("Candidate A votes:", len(voter_a))
        print("Candidate B votes:", len(voter_b))

    elif choice == "3":
        print("Exiting Voting System...")
        break

    else:
        print("Invalid choice")
