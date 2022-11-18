# Matplotlib Exercise: bar chart

# Import matplotlib here

# Create an empty dictionary 
# (key is the Linux Distribution name, value is the number of Hits per Day
distros_dict = {}

# open the data file
with open("distrowatch_2021.csv") as weather_file:
    _ = weather_file.readline() # column headers on first line of file
    
    for line in weather_file:
        distro, hits_per_day  = line.split(",")
        # insert the key,value pair into the dictionary
        distros_dict[distro] = int(hits_per_day)
        
# Add code for the Bar Chart here

