import random

def number_guesser():
    target = random.randint(1, 50)
    attempts = 0
    guess = None

    print("Guess the number between 1 and 50")

    while guess != target:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < target:
                print("Too low")
            elif guess > target:
                print("Too high")
            else:
                print(f"Correct! You guessed it in {attempts} tries.")
        except ValueError:
            print("Enter a valid number")

number_guesser()
