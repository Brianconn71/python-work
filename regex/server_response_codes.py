import re

#program to read access logs
def log_errors():

    # open file for reading
    with open("/home/briancon71/scripting/regex/access.log", "r") as log_files:
        
        #create empty dictionary
        status_codes_dict = {}
        # create list to store all found codes in
        list_of_codes =[]
        
        # compile the regex
        regex = re.compile(".*?HTTP\/\d\.\d\"\s(\d{3})")

        # loop through lines in log
        for line in log_files:
            # search for regex matches in the lines of code
            match = re.search(regex, line)
            # turn the string into an int for code number
            code_number = int(match.group(1))
            # add newly found code to the list of codes
            list_of_codes.append(code_number)
        
        # find unique values in the list
        uniques = set(list_of_codes)
        # loop through all the found codes
        for code in list_of_codes:
            # if the code is in the unique code list
            if code in uniques:
                # add to the dictionary and update number of occurances
                status_codes_dict[code] = status_codes_dict.get(code,0) + 1
    
    # print headers
    print("Code \t Frequency")
    # loop through codes dictionary
    for status_code in sorted(status_codes_dict):
        # print the code along side number of occurances
        print(f"{status_code} \t {status_codes_dict[status_code]:>4}")

if __name__ == "__main__":
    log_errors()