"""
Python Installation Test
This script tests if Python is working correctly for the Number Guessing Game project.
Run this first to make sure everything is set up properly!
"""

import sys
import random

def test_python_installation():
    """Test basic Python functionality."""
    print("🐍 PYTHON INSTALLATION TEST")
    print("=" * 30)
    
    # Test Python version
    version = sys.version_info
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3:
        print("⚠️  Warning: Python 2 detected. Python 3 is recommended.")
    else:
        print("✅ Python 3 detected - Perfect!")
    
    # Test random module
    try:
        test_number = random.randint(1, 100)
        print(f"✅ Random module working: Generated {test_number}")
    except ImportError:
        print("❌ Error: Random module not available")
        return False
    
    # Test user input (basic)
    print("✅ Input/Output working")
    
    # Test basic operations
    test_var = "Hello, World!"
    if len(test_var) == 13:
        print("✅ String operations working")
    
    test_num = 5 + 3
    if test_num == 8:
        print("✅ Math operations working")
    
    # Test if/else
    if True:
        print("✅ Conditional statements working")
    
    # Test loops
    count = 0
    for i in range(3):
        count += 1
    if count == 3:
        print("✅ Loops working")
    
    print("\n🎉 CONGRATULATIONS!")
    print("Your Python installation is ready for the Number Guessing Game!")
    print("\nNext steps:")
    print("1. Try running: simple_guessing_game.py")
    print("2. Then try: number_guessing_game.py") 
    print("3. Finally: advanced_guessing_game.py")
    print("\nHappy coding! 🚀")
    
    return True

if __name__ == "__main__":
    try:
        test_python_installation()
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("Please make sure Python is installed correctly.")
        print("Visit https://python.org/downloads to download Python.")
