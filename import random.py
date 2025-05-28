import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        user_input = input("Enter your guess (1-100): ")
        
        if not user_input.isdigit():
            print("Please enter a valid integer.")
            continue
            
        guess = int(user_input)
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
            
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

number_guessing_game()