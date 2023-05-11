#ramdom library call
import random
magic_number = random.randint(1, 100)

#Guess Part
guess = 0
try_number = 0
keeping_word = "yes"

while keeping_word.lower() == "yes":
    while magic_number != guess:
        guess = int(input("\nWhat is your guess? "))
        if magic_number > guess:
            print("Higher")
        elif magic_number < guess:
            print("Lower")
        else:
         print("You guessed it!\n")
        try_number = try_number + 1

    #Displaying the numbers of tests
    print(f"Number of tests: {try_number}")
    keeping_word = input("Do you want to play again?: ")
    magic_number = random.randint(1, 100)

print("\nGame Over My Friend 😎!")  