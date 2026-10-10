import random
secretNumber = random.randint (1,100)
attempts = 0
print("Welcome to the Number Guessing Game!")
print()
userGuess = int(input("Guess a number between 1 and 100: "))
attempts += 1
while userGuess != secretNumber:
    if userGuess < secretNumber:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")
    userGuess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

print("Congratulations, you guessed the correct number!")
print(f"It took you {attempts} attempt(s).")