#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to visualise Earthquake data from a csv file
Example of: Visualisation with Matplotlib

@author: cormac
"""
import datetime

import matplotlib.pyplot as plt

# the dictionary will contain
# as key: a datetime object representing the date and time of the earthquake
# as value: the magnitude of the corresponding earthquake
earthquakes = {}

# open the file (deliberately leaving out exception handling)
with open("earthquakes_2019.csv") as data_file:
    _ = data_file.readline() # discard the headers
    
    for line in data_file:
        #split the line into 5 variables
        # maxsplit leaves the last column in a single variable
        # this avoids the complication of the place containing commas
        time_string, latitude, longitude, magnitude, place = line.split(",",maxsplit=4)
        
        when = datetime.datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        # insert into the dictionary
        earthquakes[when] = float(magnitude)

# visualisations
#creating the figure and the axes
fig, axs = plt.subplots(1,3, figsize=(15,10))

# setting subtitle
fig.suptitle("Earthquake magnitude visualisations")

# title of the histogram
axs[0].set_title("Histogram")

# setting the axis labels
axs[0].set_xlabel("Magnitude")
axs[0].set_ylabel("Frequency")

#loop through earthquake items and appaend magnitudes to a list.
magnitudes = []
for date, mag in earthquakes.items():
    magnitudes.append(mag)
#bins for histogram
bins = range(0, int(max(magnitudes)) + 2)

#xticks
axs[0].set_xticks(bins)

# display histogram
axs[0].hist(magnitudes,bins, ec="black")

# setting the title
axs[1].set_title("Box Plot")

# boxplot
axs[1].set_ylabel("Magnitudes")

# boxplot
axs[1].boxplot(magnitudes, showmeans=True, meanline=True)

# # violin plot
#set the title
axs[2].set_title("Violin Plot")

# y axis label
axs[2].set_ylabel("Magnitudes")

# display the violin plot
axs[2].violinplot(magnitudes, showmeans=True)

# show the figure
plt.show()

# save the figure
fig.savefig("exercise_1.png")