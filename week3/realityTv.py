age = int(input("Enter your age: "))
maritalStatus = input("Enter your marital status: ").lower()

if 18 <= age <= 35:
    if maritalStatus == "single":
        print("You are suitable for the TV show")
    elif maritalStatus == "married":
        print("You are not suitable for the TV show") 
else:
    print("You are not suitable for the TV show")
