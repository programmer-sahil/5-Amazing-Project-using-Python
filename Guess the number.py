import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Initialize user variable
user = None  

# Allow 3 attempts
for i in range(3):
    try:
        user = int(input("Guess the number (1-10): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Skip this iteration if input is not an integer
    
    if user == number:
        print(f"Hurray! You guessed the number right, it's {number}.")
        break  # Exit the loop when guessed correctly
    else:
        print("Wrong guess. Try again!")

# If user never guessed correctly
if user != number:
    print(f"Sorry, you've used all attempts. The number was {number}.")
