numOfCopies = int(input("Enter number of copies: "))

if 1 <= numOfCopies <= 50:
    cost = numOfCopies * .11
    print(f"Cost is {cost:.2f}")
elif 51 <= numOfCopies <= 100:
    cost = numOfCopies * .10
    print(f"Cost is {cost:.2f}")
elif 101 <= numOfCopies <= 1000:
    cost = numOfCopies * .09
    print(f"Cost is {cost:.2f}")
elif numOfCopies > 1000:
    cost = numOfCopies * .08
    print(f"Cost is {cost:.2f}")