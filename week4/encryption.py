from string import ascii_lowercase


message = input("Enter a message to encipher: ").lower()

cipher = ""

for letter in message:
    if letter.isalnum():
        letterIndex = ascii_lowercase.find(letter)
        addthirteen = (letterIndex + 13) % 26
        newLetter = ascii_lowercase[addthirteen]
        cipher += newLetter
    else:
        cipher += letter
print("The enciphered message is: ", cipher)