from curses.ascii import isalnum


variableName = input("Enter the variable name: ")

underline = "_"
validVariableName = ""

for character in variableName:
    if character.isalnum() or character == underline:
        validVariableName += character
        
    else:
        print("Invalid character ", character)
        break
else:
    print("Valid variable name")