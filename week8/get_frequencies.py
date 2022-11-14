file = '/home/briancon71/python-work/week8/wordlist.txt'


def get_frequencies(file_name):
    
    # empty dictionary
    new_dict = {}
    
    #open filename parameter
    with open(file_name, "r") as filename:
        #read contens as a string
        data = filename.read()
        
        #convert to lowercase
        lower_case_data = data.lower()

        #only english language alphabet characters
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
        
       # for loop
        for letter in lower_case_data:
            if letter.lower() in alphabet:
                new_dict[letter]= new_dict.get(letter,0) +1
                
        # new_dict = [new_dict.get(letter,0) +1 for letter in lower_case_data if letter.isalpha()]
        return new_dict

frequencies = get_frequencies(file)
print("Letter Frequency")
for letter, frequency  in sorted(frequencies.items()):
    print(f"   {letter:<3} {frequency:>5}")