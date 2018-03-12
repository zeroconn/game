#devcyber
from random import randint
print("""
| Create by Alvise Valente |
""")
roll = input("Press Y to roll the dice, press N to quit: ")
while roll.lower() == "y":
    print(randint(1,6))
    print(randint(1,6))
    roll = input("Press Y to roll again, N to quit: ")

print("Okay, we'll put the dice away...")

#by Alvise