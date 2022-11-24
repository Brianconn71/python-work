import re

def read_errors():
    # open the file for reading
    with open("/home/bconnolly/python-work/regex/error.log", "r") as log_file:

        #read the entire file
        read_logs = log_file.read()

        # search for all instances and add to list
        missing_files = re.findall("File does not exist\:\s(\/\w+\/\w+\/\w+\/\w+\/\w+\.\w+)",read_logs)

        #get length of list
        length_of_list = len(missing_files)

        #set of missing files list
        set_missing_files = len(set(missing_files))

        # print number of missing files
        print(f"Number of missing file errors: {length_of_list}")

        #print number of unique missing files
        print(f"Number of unique missing files: {set_missing_files}")

if __name__ == "__main__":
    read_errors()

