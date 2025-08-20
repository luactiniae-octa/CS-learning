import random

# Simple Number Guessing Game - Beginner Version
# This is the most basic version to help you understand the core concepts

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10...")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 0

# Keep asking for guesses until they get it right
while True:
    # Get the player's guess
    guess = int(input("What's your guess? "))
    attempts = attempts + 1
    
    # Check if the guess is correct
    if guess == secret_number:
        print(f"🎉 Congratulations! You got it in {attempts} tries!")
        break
    elif guess < secret_number:
        print("📈 Too low! Try again.")
    else:
        print("📉 Too high! Try again.")

print("Thanks for playing! 👋")
