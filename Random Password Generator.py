import random

# Get the desired password length from the user
passlen = int(input("Enter the length of the password: "))

# Define the character set for the password
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*{}?*-"

# Ensure passlen is not greater than the length of s
if passlen > len(s):
    print("Error: Password length exceeds available character set size.")
else:
    # Generate a random password by sampling characters from 's'
    p = "".join(random.choices(s, k=passlen))  # Changed sample() to choices() to allow repetition
    
    # Print the generated password
    print("Generated Password:", p)
