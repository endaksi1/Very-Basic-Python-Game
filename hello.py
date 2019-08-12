

import random

number = random.randint(1, 10)
tries = 1


uname = input("Hello, What is your username?")

print("Hello ", uname + ".", )

question = input("would you like to play a game? [Yes/No] ")
if question == "No":
    print("oh..okay")

if question == "yes":
        print("Im thinking of a number between 1 and 10")
        guess =int(input("Have a guess."))
        if guess > number:
            print("Guess lower...")
        if guess < number:
            print("Guess higher...")
        while guess != number:
            tries += 1
            guess = int(input("Try again: "))
        if guess == number:
            print("Correct! Well Done! The number was ", number, \
                "and it only took ", tries, "tries!")