cost = float(input("Enter the cost of the meal: "))
service = float(input("Enter the service charge: "))
tip = float(input("Enter the tip: "))

billTotal = cost * (1 + (service / 100)) + tip

print(f"The total bill is {billTotal:.2f} Euro")