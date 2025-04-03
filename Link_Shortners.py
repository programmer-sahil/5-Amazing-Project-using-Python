# link shortners

import pyshorteners

# Get the link from the user
link = input("Enter the link: ")

# Create a Shortener object
shortener = pyshorteners.Shortener()

# Shorten the link using TinyURL
shortened_link = shortener.tinyurl.short(link)

# Print the shortened link
print("Shortened Link:", shortened_link)


# how to run: pip install pyshorteners
