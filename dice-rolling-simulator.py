import random

print("Dices being rolled...")
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("Here's the result..!!\nDice 1 rolled on: {}\nDice 2 rolled on: {}\nTotal Score = {}".format(dice1, dice2, dice1+dice2))
