# Task 1: Random Choice Game
import random
items = ["bike","motorcycle","car","truck","soda","laptop"]

citem = random.choice(items)

print(items)
ug = input("guess which item was randomly selected from the list above?? ")

if ug == citem:
    print("You win!")
else:
    print("you lose!!!", citem, "Was the item!!")