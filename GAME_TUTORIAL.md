# Building Your First Interactive Game: Number Guessing Game

## 🎯 What We'll Build
An interactive number guessing game where:
- The computer picks a random number between 1-100
- The player tries to guess it
- The game provides hints ("too high" or "too low")
- Tracks the number of attempts
- Asks if the player wants to play again

## 🎓 What You'll Learn
- Variables and data types
- User input and output
- Random number generation
- Loops (while, for)
- Conditional statements (if/else)
- Functions
- Basic game logic

## 📋 Prerequisites
- Basic understanding of Python syntax
- Python installed on your computer
- A text editor or IDE (VS Code, PyCharm, or even Notepad++)

---

## Step 1: Setting Up the Project Structure

### 1.1 Create the Game File
Create a new file called `number_guessing_game.py`

### 1.2 Plan the Game Flow
```
1. Welcome the player
2. Generate a random number
3. Ask for player's guess
4. Compare guess with the target number
5. Provide feedback (higher/lower/correct)
6. Track attempts
7. Repeat until correct
8. Ask to play again
```

---

## Step 2: Import Required Libraries

```python
import random
```

**What this does:**
- `random` module helps us generate random numbers
- We'll use `random.randint()` to pick a number between 1-100

---

## Step 3: Create the Main Game Function

### 3.1 Start with the basic structure:
```python
def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    # Generate random number
    target_number = random.randint(1, 100)
    attempts = 0
    
    # Game loop will go here
```

**Key Concepts:**
- **Function**: A reusable block of code
- **Variables**: Store data (`target_number`, `attempts`)
- **Comments**: Explain what the code does

### 3.2 Add the Game Loop
```python
def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < target_number:
                print("📈 Too low! Try a higher number.")
            elif guess > target_number:
                print("📉 Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
                
        except ValueError:
            print("❌ Please enter a valid number!")
```

**New Concepts:**
- **While loop**: Repeats code until a condition is met
- **Try/except**: Handles errors (like non-numeric input)
- **Input validation**: Makes sure the player enters a number
- **String formatting**: `f"text {variable}"`

---

## Step 4: Add Input Validation and Improvements

### 4.1 Validate Number Range
```python
def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❌ Please enter a number between 1 and 100!")
        except ValueError:
            print("❌ Please enter a valid number!")
```

**Why this helps:**
- Separates input validation into its own function
- Ensures guesses are in the valid range
- Makes code more organized and reusable

### 4.2 Update the main game function:
```python
def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Add difficulty
    
    while attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1
        
        if guess < target_number:
            print("📈 Too low! Try a higher number.")
        elif guess > target_number:
            print("📉 Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            return True  # Player won
        
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
    
    print(f"💔 Game over! The number was {target_number}")
    return False  # Player lost
```

---

## Step 5: Add Difficulty Levels

### 5.1 Create difficulty selection:
```python
def choose_difficulty():
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
```

### 5.2 Update the game function to use difficulty:
```python
def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    
    max_number, max_attempts = choose_difficulty()
    target_number = random.randint(1, max_number)
    attempts = 0
    
    print(f"I'm thinking of a number between 1 and {max_number}...")
    print(f"You have {max_attempts} attempts to guess it!")
    
    # Rest of the game logic...
```

---

## Step 6: Add Play Again Feature

### 6.1 Create the main game loop:
```python
def main():
    print("🎲 Number Guessing Game")
    print("=" * 30)
    
    while True:
        won = play_game()
        
        # Show statistics
        if won:
            print("🏆 You're getting good at this!")
        else:
            print("🎯 Better luck next time!")
        
        # Ask to play again
        while True:
            play_again = input("\n🔄 Would you like to play again? (y/n): ").lower()
            if play_again in ['y', 'yes']:
                print("\n" + "="*50)
                break
            elif play_again in ['n', 'no']:
                print("👋 Thanks for playing! Goodbye!")
                return
            else:
                print("❌ Please enter 'y' for yes or 'n' for no")

# Start the game
if __name__ == "__main__":
    main()
```

---

## Step 7: Add Advanced Features (Optional)

### 7.1 Score Tracking:
```python
class GameStats:
    def __init__(self):
        self.games_played = 0
        self.games_won = 0
        self.total_attempts = 0
        self.best_score = float('inf')
    
    def update_stats(self, won, attempts):
        self.games_played += 1
        self.total_attempts += attempts
        if won:
            self.games_won += 1
            self.best_score = min(self.best_score, attempts)
    
    def show_stats(self):
        if self.games_played > 0:
            win_rate = (self.games_won / self.games_played) * 100
            avg_attempts = self.total_attempts / self.games_played
            print(f"\n📊 Your Statistics:")
            print(f"Games played: {self.games_played}")
            print(f"Win rate: {win_rate:.1f}%")
            print(f"Average attempts: {avg_attempts:.1f}")
            if self.best_score != float('inf'):
                print(f"Best score: {self.best_score} attempts")
```

### 7.2 Hints System:
```python
def give_hint(target_number, attempts):
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
```

---

## Step 8: Testing Your Game

### 8.1 Test Cases to Try:
1. **Valid inputs**: Numbers within range
2. **Invalid inputs**: Letters, symbols, numbers outside range
3. **Edge cases**: Minimum (1) and maximum numbers
4. **Different difficulties**: Test all three levels
5. **Play again feature**: Test 'y', 'n', and invalid responses

### 8.2 Common Issues and Solutions:

**Problem**: Game crashes with non-numeric input
**Solution**: Use try/except blocks

**Problem**: Infinite loop
**Solution**: Make sure your while loop has a proper exit condition

**Problem**: Random number not changing
**Solution**: Make sure `random.randint()` is called inside the game function

---

## Step 9: Enhancements You Can Add

### 9.1 Beginner Enhancements:
- Add ASCII art for the title
- Use different emojis for different ranges
- Add a "give up" option
- Show how close the guess was (within 10, within 5, etc.)

### 9.2 Intermediate Enhancements:
- Save high scores to a file
- Add a timer to track how long each game takes
- Create different game modes (reverse guessing, multiple numbers)
- Add sound effects (using libraries like `pygame`)

### 9.3 Advanced Enhancements:
- Create a GUI version using `tkinter`
- Add multiplayer functionality
- Create difficulty that adapts to player performance
- Add achievements system

---

## Complete Code Structure

Your final project should have these files:
- `number_guessing_game.py` - Main game file
- `game_stats.py` - Statistics tracking (optional)
- `README.md` - Instructions for running the game

---

## 🎯 Learning Outcomes

After completing this project, you'll understand:
- **Variables and Data Types**: Numbers, strings, booleans
- **Control Flow**: if/else statements, while/for loops
- **Functions**: Creating reusable code blocks
- **Error Handling**: try/except blocks
- **User Input/Output**: Getting input, formatting output
- **Random Numbers**: Generating random values
- **Code Organization**: Separating concerns into functions
- **Testing**: How to test different scenarios

---

## 🚀 Next Steps

Once you've built this game, try:
1. **Rock, Paper, Scissors** - Multiple choice game
2. **Text Adventure** - Story-based game with choices
3. **Hangman** - Word guessing with graphics
4. **Tic-Tac-Toe** - Two-player strategy game
5. **Simple Calculator** - Mathematical operations

Remember: The best way to learn programming is by building projects and experimenting with the code. Don't be afraid to break things - that's how you learn!

---

## 📚 Additional Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python Games for Beginners](https://realpython.com/python-games/)

Happy coding! 🚀
