from string import ascii_lowercase

# Input the text and convert to lowercase
text = input("Enter the text: ").lower()

# Create a list of the frequencies of the 26 letters, initialised to zero
letterFrequencies = [0] * 26
# For each character in the text
for char in text:
    # If the character is a letter
    if char.isalpha():
        #Find the index of the letter in the alphabet (use ascii_lowercase.index(character))
        letterIndex = ascii_lowercase.index(char)
        #Increase by 1 the value of the corresponding element in the frequencies list
        letterFrequencies[letterIndex] += 1
#Display the letters and their frequencies
print("Letter Frequency")
for letter,frequency in zip(ascii_lowercase, letterFrequencies):
    print(f"{letter:^5}{frequency:^9}")
#Determine and display the most frequent letter
modeLetter = max(letterFrequencies)
mode_index = letterFrequencies.index(modeLetter) 
print("\nMost frequent letter:", ascii_lowercase[mode_index])
