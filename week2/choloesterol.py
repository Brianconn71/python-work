ch = float(input("Enter your cholesterol"))

if ch >= 0 and ch <= 5:
    print("Normal")
elif ch > 5 and ch <= 6.4:
    print("Ehh")
elif ch > 6.4 and ch <=7.8:
    print("Woooow")
elif ch > 7.8:
    print("Jeez")