import random
import json
import time
from datetime import datetime

class GameStats:
    """Class to track and manage game statistics."""
    
    def __init__(self, filename="game_stats.json"):
        self.filename = filename
        self.games_played = 0
        self.games_won = 0
        self.total_attempts = 0
        self.best_score = float('inf')
        self.total_time = 0
        self.difficulty_stats = {"easy": 0, "medium": 0, "hard": 0}
        self.load_stats()
    
    def load_stats(self):
        """Load statistics from file."""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.games_played = data.get('games_played', 0)
                self.games_won = data.get('games_won', 0)
                self.total_attempts = data.get('total_attempts', 0)
                self.best_score = data.get('best_score', float('inf'))
                self.total_time = data.get('total_time', 0)
                self.difficulty_stats = data.get('difficulty_stats', {"easy": 0, "medium": 0, "hard": 0})
        except (FileNotFoundError, json.JSONDecodeError):
            # File doesn't exist or is corrupted, start fresh
            pass
    
    def save_stats(self):
        """Save statistics to file."""
        data = {
            'games_played': self.games_played,
            'games_won': self.games_won,
            'total_attempts': self.total_attempts,
            'best_score': self.best_score if self.best_score != float('inf') else None,
            'total_time': self.total_time,
            'difficulty_stats': self.difficulty_stats,
            'last_played': datetime.now().isoformat()
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def update_stats(self, won, attempts, game_time, difficulty):
        """Update statistics after a game."""
        self.games_played += 1
        self.total_attempts += attempts
        self.total_time += game_time
        self.difficulty_stats[difficulty] += 1
        
        if won:
            self.games_won += 1
            self.best_score = min(self.best_score, attempts)
        
        self.save_stats()
    
    def show_stats(self):
        """Display comprehensive statistics."""
        if self.games_played == 0:
            print("📊 No games played yet!")
            return
        
        win_rate = (self.games_won / self.games_played) * 100
        avg_attempts = self.total_attempts / self.games_played
        avg_time = self.total_time / self.games_played
        
        print(f"\n📊 Your All-Time Statistics:")
        print("=" * 40)
        print(f"🎮 Games played: {self.games_played}")
        print(f"🏆 Games won: {self.games_won}")
        print(f"📈 Win rate: {win_rate:.1f}%")
        print(f"🎯 Average attempts: {avg_attempts:.1f}")
        print(f"⏱️  Average time: {avg_time:.1f} seconds")
        
        if self.best_score != float('inf'):
            print(f"🌟 Best score: {self.best_score} attempts")
        
        print(f"\n🎚️  Difficulty Breakdown:")
        for difficulty, count in self.difficulty_stats.items():
            if count > 0:
                percentage = (count / self.games_played) * 100
                print(f"   {difficulty.capitalize()}: {count} games ({percentage:.1f}%)")

class NumberGuessingGame:
    """Advanced Number Guessing Game with full features."""
    
    def __init__(self):
        self.stats = GameStats()
        self.difficulties = {
            1: {"name": "easy", "range": 50, "attempts": 10},
            2: {"name": "medium", "range": 100, "attempts": 8},
            3: {"name": "hard", "range": 200, "attempts": 6}
        }
    
    def get_valid_input(self, prompt, valid_range=None, input_type=int):
        """Get valid input with error handling."""
        while True:
            try:
                value = input_type(input(prompt))
                if valid_range and not (valid_range[0] <= value <= valid_range[1]):
                    print(f"❌ Please enter a number between {valid_range[0]} and {valid_range[1]}!")
                    continue
                return value
            except ValueError:
                print(f"❌ Please enter a valid {input_type.__name__}!")
    
    def choose_difficulty(self):
        """Let player choose difficulty level."""
        print("\n🎚️  Choose your challenge:")
        for key, diff in self.difficulties.items():
            print(f"{key}. {diff['name'].capitalize()} (1-{diff['range']}, {diff['attempts']} attempts)")
        
        choice = self.get_valid_input("Enter your choice (1-3): ", (1, 3))
        return self.difficulties[choice]
    
    def give_smart_hint(self, target_number, attempts, max_number):
        """Provide intelligent hints based on game state."""
        hints = []
        
        if attempts == 3:
            if target_number % 2 == 0:
                hints.append("The number is even!")
            else:
                hints.append("The number is odd!")
        
        if attempts == 5:
            if target_number <= max_number // 4:
                hints.append("The number is in the lowest quarter!")
            elif target_number >= 3 * max_number // 4:
                hints.append("The number is in the highest quarter!")
            else:
                hints.append("The number is somewhere in the middle range!")
        
        if attempts >= 6:
            if target_number % 5 == 0:
                hints.append("The number is divisible by 5!")
            elif target_number % 10 == 1:
                hints.append("The number ends in 1!")
        
        if hints:
            print(f"💡 Hint: {hints[-1]}")
    
    def get_performance_message(self, attempts, max_attempts):
        """Get performance message based on attempts used."""
        ratio = attempts / max_attempts
        
        if attempts == 1:
            return "🎯 UNBELIEVABLE! One shot, one kill!"
        elif ratio <= 0.25:
            return "🏆 PHENOMENAL! You're a guessing genius!"
        elif ratio <= 0.5:
            return "⭐ EXCELLENT! Great intuition!"
        elif ratio <= 0.75:
            return "👍 GOOD JOB! Solid performance!"
        else:
            return "😅 CLOSE CALL! That was intense!"
    
    def play_single_game(self):
        """Play one game and return results."""
        print("🎮 Starting new game...")
        
        difficulty = self.choose_difficulty()
        target_number = random.randint(1, difficulty["range"])
        attempts = 0
        start_time = time.time()
        
        print(f"\n🔢 I'm thinking of a number between 1 and {difficulty['range']}...")
        print(f"🎯 You have {difficulty['attempts']} attempts to guess it!")
        print("🚀 Let's begin!\n")
        
        while attempts < difficulty["attempts"]:
            guess = self.get_valid_input(
                f"Enter your guess (1-{difficulty['range']}): ",
                (1, difficulty["range"])
            )
            attempts += 1
            
            if guess == target_number:
                game_time = time.time() - start_time
                print(f"\n🎉 CONGRATULATIONS! You found it in {attempts} attempts!")
                print(self.get_performance_message(attempts, difficulty["attempts"]))
                print(f"⏱️  Time taken: {game_time:.1f} seconds")
                
                self.stats.update_stats(True, attempts, game_time, difficulty["name"])
                return True
            
            elif guess < target_number:
                print("📈 Too low! Aim higher!")
            else:
                print("📉 Too high! Go lower!")
            
            remaining = difficulty["attempts"] - attempts
            if remaining > 0:
                print(f"🔄 Attempts remaining: {remaining}")
                self.give_smart_hint(target_number, attempts, difficulty["range"])
                print()
        
        game_time = time.time() - start_time
        print(f"\n💔 Game Over! The number was {target_number}")
        print("🎯 Don't worry, every expert was once a beginner!")
        
        self.stats.update_stats(False, attempts, game_time, difficulty["name"])
        return False
    
    def show_menu(self):
        """Display main menu options."""
        print("\n🎮 MAIN MENU")
        print("=" * 20)
        print("1. 🎯 Play Game")
        print("2. 📊 View Statistics") 
        print("3. 🗑️  Reset Statistics")
        print("4. 👋 Quit")
    
    def reset_stats_confirm(self):
        """Confirm and reset statistics."""
        confirm = input("\n⚠️  Are you sure you want to reset all statistics? (yes/no): ").lower()
        if confirm in ['yes', 'y']:
            self.stats = GameStats()  # Create fresh stats
            print("✅ Statistics reset successfully!")
        else:
            print("❌ Reset cancelled.")
    
    def run(self):
        """Main game loop with menu system."""
        print("🎲 ADVANCED NUMBER GUESSING GAME")
        print("=" * 40)
        print("🌟 Welcome to the ultimate guessing challenge!")
        
        while True:
            self.show_menu()
            choice = self.get_valid_input("\nSelect an option (1-4): ", (1, 4))
            
            if choice == 1:
                # Play game
                print("\n" + "="*50)
                won = self.play_single_game()
                
                if self.stats.games_played > 0:
                    win_rate = (self.stats.games_won / self.stats.games_played) * 100
                    print(f"\n📈 Session Progress: {self.stats.games_won}/{self.stats.games_played} wins ({win_rate:.1f}%)")
            
            elif choice == 2:
                # View statistics
                self.stats.show_stats()
            
            elif choice == 3:
                # Reset statistics
                self.reset_stats_confirm()
            
            elif choice == 4:
                # Quit
                print("\n👋 Thanks for playing!")
                if self.stats.games_played > 0:
                    print("🎯 Keep practicing and you'll become a guessing master!")
                print("Goodbye! 🌟")
                break

def main():
    """Initialize and start the advanced game."""
    game = NumberGuessingGame()
    game.run()

if __name__ == "__main__":
    main()
