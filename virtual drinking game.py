import random
drinks = ["vodka", "Gin", "rum", "whiskey", "wine", "beer"]
try:
    name = input("What is your name? ")
    age = input("How old are you? ")
    age = input(age) # convert string to integer
    country = input("Where are you from? ")
except ValueError:
    print("Invalid age. Please enter a number.")
else:
    # now we have a good age to play with
    if age < 0 or age > 140:
        print("You are not human. This game is for humans only.")
    elif age > 120:
        print("You are too old to play the awsome drinking game.")
    elif age < 18:
        print("You are a minor. You can not play the awesome drinking game.")
    elif (country == "USA" or country == "UAE") and age < 21:
        print("You are ")
    else:
        print("You are an adult. You can play the awesome drinking game.")
        print("have some", random.choice(drinks), "and enjoy the game.")
