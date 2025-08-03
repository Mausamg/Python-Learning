import random

def number_guessing_game():
    number_to_guess = random.randint(1,50)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print(f"Attempt {attempts}. Too low! Try again.")
            elif guess > number_to_guess:
                print(f"Attempt {attempts}. Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("❌ Please enter a valid integer.")

# Run the game
number_guessing_game()
