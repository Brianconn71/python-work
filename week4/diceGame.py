from random import randint

evens = 0
rolls = 0

while rolls < 5:
    
    numberRolled = randint(1, 6)
    
    print("You rolled: ", numberRolled)
    
    if numberRolled % 2 == 0:
        evens += 1
    
    rolls += 1
else:
    print(f"You rolled {evens} even numbers")
    if evens >= 3:
        print("You win!")
    else:
        print("You lose")
