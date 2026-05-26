import random
import math

secret = random.randint(0,100)
guess_count = 0

while True:
    try:
        guess = int(input("Guess a number! "))
    except ValueError:
        print("That's not an integer, try again.")
        continue
    guess_count += 1
    #if math.floor(guess) != guess:
    #    print("That's not an integer, try again.")
    #    continue
    
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    elif guess == secret:
        print(f"You got it in {guess_count} guesses!")
        break
    
