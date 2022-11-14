
    
menu = input("[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()
    
contacts = ["087 1234567", "090 9876543", "090 6468000", "112"]

while menu != "q":    
    if menu == "p":
        print("Numbers in your contacts list")
        for num in range(len(contacts)):
            print(f"{num:^5}: {contacts[num]}")
    elif menu == "c":
        checkNum = input("Enter the number: ")
        if checkNum in contacts:
            print(f"Number {checkNum} is in the list")
        else:
            print(f"Number {checkNum} is not in the list")
    elif menu == "a":
        newNum = input("Enter new number: ")
        contacts.append(newNum)
        print(f"Added {newNum} to the list")
    elif menu == "e":
        editNum = input("Enter number to edit: ")
        changedNum = input("Enter the new number: ")
        newContactList = []
        for i, num in enumerate(contacts):
            if editNum == num:
                contacts[i] = changedNum
        print(f"Replaced {editNum} with {changedNum}")
    elif menu == "d":
        deleteNum = input("Enter number to delete: ")
        contacts.remove(deleteNum)
        print(f"Removed {deleteNum} from the list")
    menu = input("\n[P]rint list [C]heck number [A]dd number [E]dit number [D]elete number [Q]uit: ").lower()
