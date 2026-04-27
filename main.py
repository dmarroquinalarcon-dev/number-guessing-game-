import random

secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You got it in " + str(attempts) + " attempts!")
        break
