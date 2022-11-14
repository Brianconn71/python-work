file = '/home/briancon71/scripting/week8/alice.txt'


def get_frequencies(file_name):
    
    # empty dictionary
    new_dict = {}
    
    #open filename parameter
    with open(file_name, "r") as filename:
        #read contens as a string
        data = filename.read()
        
        #convert to lowercase
        lower_case_data = data.lower()
        
       # for loop
        for letter in lower_case_data:
            if letter.isalpha():
                data.count(letter)
                new_dict[letter]= new_dict.get(letter,0) +1
                
        # new_dict = [new_dict.get(letter,0) +1 for letter in lower_case_data if letter.isalpha()]
        return new_dict

	
# alice.txt
frequencies = get_frequencies(file)
print("Letter Frequency")
for letter, frequency  in sorted(frequencies.items()):
    print(f"   {letter:<3} {frequency:>5}")