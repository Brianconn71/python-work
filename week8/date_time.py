import datetime

#takes input from user
input = input("Enter a date in the form dd/mm/yyyy: ")

# creates datetime object
input_date = datetime.datetime.strptime(input, "%d/%m/%Y")

#returns day of the week from input date
day = datetime.datetime.strftime(input_date,"%A")

print("Day of the week:", day)