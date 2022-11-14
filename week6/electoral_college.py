filename = input("Enter the filename: ")

# try to correctly read file
try:
    #initialize lists
    number_of_electors = []
    states = []
    population = []
    #try to open file
    with open(filename, "r") as electoral_data:
        #headers
        header = electoral_data.readline()

        # Loop through the file line by line
        for line in electoral_data:
            try:
                # try to split data into three variables
                state, population, electors = line.split(",")
                try:
                    # try to add correct data to electors
                    number_of_electors.append(int(electors))
                except ValueError:
                    print(f"Invalid or missing number of electors for {state}")
            except ValueError:
                print(f"Line has invalid format: {line}")

    # getting the mean value          
    mean = sum(number_of_electors) / len(number_of_electors)
    print(f"Mean electors per State/District: {mean:.1f}")

    # getting the median value
    sorted_list = sorted(number_of_electors)
    middle = int(len(number_of_electors) / 2)
    if len(sorted_list) % 2 == 1:
        median = sorted_list[middle]
    else:
        meidan = (sorted_list[middle-1] + sorted_list[middle]/2)
    print(f"Median electors per State/District: {median:.1f}")

    # getting the mode value
    unique_values = sorted(set(number_of_electors))
    times_appearing = [number_of_electors.count(value) for value in unique_values]
    max_value = max(times_appearing)
    index_of_max = times_appearing.index(max_value)
    mode = unique_values[index_of_max]
    print(f"Mode of electors per State/District: {mode}")

# File not found error being caught here
except FileNotFoundError as e:
    print(f"Unable to open the file {filename}")