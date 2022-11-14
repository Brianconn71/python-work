metre = float(input("Entre metres:"))

dist = metre * 3.28084

whole = int(dist)

inch = (dist - whole) * 12

print("feet: ", whole)
print("Inches: ", f"{inch:.2f}")


