# 1 and 1 = snake eyes
import random 

dice1 = 0
dice2 = 0
total = 0
while not(dice1 == 1 and dice2 == 2):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total += 1
    print(f'roll{total}you rolled {dice1} and {dice2}')
print(f'SNAKE EYES!,you took{total} tries to get it')
    