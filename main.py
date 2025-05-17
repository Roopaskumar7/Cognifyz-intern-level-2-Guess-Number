import random

# Set the range for the random number
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Generate a random number between lower and upper bounds
secret_number = random.randint(lower, upper)

print(f"\nI'm thinking of a number between {lower} and {upper}. Can you guess what it is?")

# Loop until the user guesses the number
while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        break
