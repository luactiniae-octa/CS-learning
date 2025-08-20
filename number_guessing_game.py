import random

def get_valid_guess(max_number):
    """Get a valid guess from the player within the specified range."""
    while True:
        try:
            guess = int(input(f"Enter your guess (1-{max_number}): "))
            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"❌ Please enter a number between 1 and {max_number}!")
        except ValueError:
            print("❌ Please enter a valid number!")

def choose_difficulty():
    """Let the player choose difficulty level."""
    print("\n🎚️  Choose difficulty level:")
    print("1. Easy (1-50, 8 attempts)")
    print("2. Medium (1-100, 7 attempts)")  
    print("3. Hard (1-200, 6 attempts)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                return 50, 8
            elif choice == 2:
                return 100, 7
            elif choice == 3:
                return 200, 6
            else:
                print("❌ Please choose 1, 2, or 3!")
        except ValueError:
            print("❌ Please enter a valid number!")

def give_hint(target_number, attempts):
    """Provide hints based on the number of attempts."""
    if attempts == 3:
        if target_number % 2 == 0:
            print("💡 Hint: The number is even!")
        else:
            print("💡 Hint: The number is odd!")
    elif attempts == 5:
        if target_number % 5 == 0:
            print("💡 Hint: The number is divisible by 5!")
        elif target_number % 3 == 0:
            print("💡 Hint: The number is divisible by 3!")
        else:
            print("💡 Hint: The number is not divisible by 3 or 5!")

def play_game():
    """Main game logic."""
    print("🎮 Welcome to the Number Guessing Game!")
    
    max_number, max_attempts = choose_difficulty()
    target_number = random.randint(1, max_number)
    attempts = 0
    
    print(f"\nI'm thinking of a number between 1 and {max_number}...")
    print(f"You have {max_attempts} attempts to guess it!")
    print("Good luck! 🍀")
    
    while attempts < max_attempts:
        guess = get_valid_guess(max_number)
        attempts += 1
        
        if guess < target_number:
            print("📈 Too low! Try a higher number.")
        elif guess > target_number:
            print("📉 Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            
            # Give performance feedback
            if attempts == 1:
                print("🏆 INCREDIBLE! First try!")
            elif attempts <= 3:
                print("🌟 Excellent guessing!")
            elif attempts <= max_attempts // 2:
                print("👍 Good job!")
            else:
                print("😅 That was close!")
            
            return True  # Player won
        
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
            give_hint(target_number, attempts)
        
    print(f"💔 Game over! The number was {target_number}")
    print("Don't give up - try again! 💪")
    return False  # Player lost

def main():
    """Main game loop with play again feature."""
    print("🎲 NUMBER GUESSING GAME")
    print("=" * 30)
    print("Test your guessing skills!")
    
    games_played = 0
    games_won = 0
    
    while True:
        games_played += 1
        won = play_game()
        
        if won:
            games_won += 1
        
        # Show statistics
        win_rate = (games_won / games_played) * 100
        print(f"\n📊 Session Stats: {games_won}/{games_played} wins ({win_rate:.1f}%)")
        
        # Ask to play again
        while True:
            play_again = input("\n🔄 Would you like to play again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                print("\n" + "="*50)
                break
            elif play_again in ['n', 'no']:
                print(f"\n👋 Thanks for playing!")
                if games_played > 1:
                    print(f"Final stats: {games_won}/{games_played} games won!")
                    if games_won == games_played:
                        print("🏆 Perfect record! You're a guessing champion!")
                    elif games_won >= games_played // 2:
                        print("🎯 Great performance!")
                print("Goodbye! 🌟")
                return
            else:
                print("❌ Please enter 'y' for yes or 'n' for no")

# Start the game when the script is run directly
if __name__ == "__main__":
    main()
