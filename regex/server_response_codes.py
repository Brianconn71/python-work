import re

#program to read access logs
def log_errors():

    # open file for reading
    with open("/home/bconnolly/python-work/regex/access.log", "r") as log_files:
        
        #create dictionary
        status_codes_dict = {}

        # loop through lines in log
        for line in log_files:
            y = re.search("HTTP\/\d\.\d\"\s(\d{3})", line)
            file_size = int(y.group(1))
            status_codes_dict[y.group(1)] = status_codes_dict.get(y,0) + file_size
        print(status_codes_dict)

if __name__ == "__main__":
    log_errors()