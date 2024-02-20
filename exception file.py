# Class work session 5&6
import age

# what is your name

name = input("What is your name? ")
print("Hello,", name, "!")
print("Hello, ", name, "!", sep="")

# How old are you
try:
    age = input("How old are you? ")
    age = int(age)  # convert string to integer

    birth_year = 2023 - age
    print("You were born in ", birth_year, ".", sep="")
    print("Hello, ", name, "!", sep="")
    number = input("give me a number to divide the age ")
    number = int(number)
    print(age / number)
except ValueError:
    print("Invalid age. Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except:
    print("Some other errors i did not forsee")
else:
    print("No exceptions were raised.")
finally:
    print("than you for playing")
