import random
# play a dice game with 3 lives, 6 wins the game

lives = 3
while lives > 0:
        print("You have", lives, "Lives left.")
        # roll the dice
        dice = random.randint(1, 6)
        print("You rolled a", dice)
        # check if you win
        if dice == 6:
            print("\n\n YOU WIN!\n\n")
            break
        else:
            lives = lives - 1
        if lives == 0:
            print("\n\nYOU LOSE!\n\n")
            break

print("Thank you for playing. Goodbye.")

