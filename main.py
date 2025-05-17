import random
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
secret_number = random.randint(lower, upper)
print(f"\nI'm thinking of a number between {lower} and {upper}. Can you guess what it is?")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        break
