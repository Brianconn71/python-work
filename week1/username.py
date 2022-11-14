fullName = input("Enter your first and last names, separated by a space: ")

firstName, lastName = fullName.split()
userName = firstName.lower() + lastName[0].lower()

print("Your username is:", userName)