# Matplotlib Exercise: bar chart

# Import matplotlib here
import matplotlib.pyplot as plt

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

# create fig and ax
fig, ax = plt.subplots(figsize=(15,10))

# title
ax.set_title("Most popular linux distributions, 2022")

# setting axis labels
ax.set_ylabel("Distributions")
ax.set_xlabel("Hits per day")

# creating the bar chart
ax.barh(list(distros_dict.keys()), distros_dict.values())

# displaying the values at the end of the bar
for index, value in enumerate(distros_dict.values()):
    ax.text(value,index,str(value))

# how the plot
plt.show()

# save the figure
fig.savefig("exercise_3.png")
