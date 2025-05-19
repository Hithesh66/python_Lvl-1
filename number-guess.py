import random

print('welcome to word guessing game ')
print('select the difficuly level')
print('1-easy😴(btw 1-10)-10% chance')
print('2-medium🙄(btw 1-100)-1% chance')
print('3-hard💀(btw 1-1000)-0.1% chance')
max = 0
diff = int(input('difficulty :'))
if diff == 1:
     max = 10
elif diff == 2:
     max = 100
elif diff == 3:
     max =1000
else:
     print('wrong input')     

num = random.randint(1,max)
guess = 0
attempts = 0

while guess != num :
    guess = int(input(f'guess a number btw 1-{max}:-'))
    attempts += 1

    if guess < num :
         print('too low-try again!')
    elif guess > num :
         print('too high-try again!')
    else :
         print(f'you are right🥳,the number is {num}')
         print(f"you got it in {attempts} tries")