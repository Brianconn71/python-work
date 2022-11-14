import datetime

filename = '/home/briancon71/scripting/week8/earthquakes_2021.csv'

earthquakes = {}

with open(filename, 'r') as file:
    
    headers = file.readline()
    
    for line in file:
        date_string, latitude, longitude, depth, magnitude = line.split(',')
        
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        earthquakes.update({date_object: float(magnitude)})
    
    num_of_eartquakes = len(earthquakes)
    print(f"Number of earthquakes: {num_of_eartquakes}")

    strongest_eartquake = max(earthquakes, key=earthquakes.get)
    c = max(earthquakes.values())
    print(f"Largest earthquake:" , strongest_eartquake, "with magnitude" , c )
    
    most_recent_earthquake = max(earthquakes)
    most_recent_earthquake_value = earthquakes.get(max(earthquakes))
    print(f"Most recent earthquake: {most_recent_earthquake} with magnitude {most_recent_earthquake_value}")
    
    least_recent_earthquake = min(earthquakes)
    least_recent_earthquake_value = earthquakes.get(min(earthquakes))
    print(f"Least recent earthquake: {least_recent_earthquake} with magnitude {least_recent_earthquake_value}")
    
    time_difference = max(earthquakes) - min(earthquakes)
    print(f"Time difference: {time_difference}")
