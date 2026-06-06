# 3MTT-Python-Projects
Data and Python projects built during the 3MTT program

import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Global Experience Oasis!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# Start the loop
while True:
    try:
        # Capture input and convert to integer
        user_guess = int(input("Enter your guess: "))
        
        # Route the logic
        if user_guess > secret_number:
            print("Too High!")
        elif user_guess < secret_number:
            print("Too Low!")
        else:
            print("You Win!")
            break  # Exit the loop upon winning
            
    except ValueError:
        print("Please enter a valid number.")
