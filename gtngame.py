import random

randNum = random.randint(1, 100)
guesses = 0

for i in range(1, 8):
    guesses = guesses + 1
    print("Guess a number 1-100! \n")
    guess = input()
    guess = int(guess)

    if guess > randNum:
        print("Your guess is too high")

    elif guess < randNum:
        print("Your guess is too low")

    elif guess == randNum:
        print("You found it! \n")
        print("You needed " + str(guesses) + " tries")

