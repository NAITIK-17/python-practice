import random

turns = 10
num = random.randint(1, 100)
while(turns > 0):
    print(f"Turns Remaining: {turns}")
    player_guess = int(input('Your Guess: '))
    if player_guess > (num + 10):
        print("too high")
    elif player_guess < (num - 10):
        print("too low")
    elif player_guess > num:
        print("high")
    elif player_guess < num:
        print("low")
    else:
        print("You won")
        break
    turns -= 1
else:
    print(f"\nYour Guess: {player_guess}")
    print(f"Num: {num}")

