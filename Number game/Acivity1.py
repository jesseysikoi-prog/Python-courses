import random
playing = True
number = str(random.randint(0,9))
print("I will generate a random number between 0 and 9. and you have to guess the number one digit at a time.")
print("The game ends when you get one hero")
while playing:
    guess = input("Give me your best guess: ")
    if number == guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("Your guess isnt quite right, try again. \n")
        