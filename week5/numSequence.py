from audioop import avg


numbersList = input("Enter a series of numbers, separated by spaces: ")

listOfNumbers = [int(numInput) for numInput in numbersList.split()]

numOfValues = len(listOfNumbers)
print(f"Number of values: {numOfValues}")

total = sum(listOfNumbers)
print(f"Total: {total}")

mean = total / numOfValues
print(f"Mean: {mean:.1f}")

max = max(listOfNumbers)
print(f"Maximum: {max}")

min = min(listOfNumbers)
print(f"Minimum: {min}")