import random

print('welcome to Rock-Paper-Scissor game🎯')
usersc = 0
compsc = 0
while True:
    user = input(f'enter your choice,rock paper,scissor or quit-q:').lower()

    if user == "q":
        break
    
    if user not in ['rock','paper','scissor']:
       print('invalid input!')
       continue

    comp = random.choice(["rock","paper","scissor"])
    print(f'computer chooses {comp}')

    if comp == user:
        print('Its a draw')
    elif (comp == "rock" and  user == "scissor") or \
         (comp == "scissor" and user == "paper") or \
         (comp == "paper" and user == "rock"):
         print('computer win🤖 this round! ')
         compsc += 1
    else:
        print('🎉you win this round')
        usersc += 1

print('Game over🎯') 
print(f'score board-you - {usersc} , bot - {compsc}')   
if usersc > compsc :
    print('🙆‍♂️you win the game🎉')
else:
    print('🤖computer win this game😭')