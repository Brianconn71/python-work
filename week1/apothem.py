from math import tan, pi

sideLength = float(input("Enter the side length: "))
numOfSides = int(input("Enter the number of sides: "))


pies = pi / numOfSides

tanned = tan(pies)

ht = 2 * tanned

apothem = sideLength / ht

print(f"The apothem is {apothem:.2f}")