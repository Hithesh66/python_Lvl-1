#The Magic 8 Ball is a popular office toy and children's toy invented in 
# the 1940s for fortune-telling and advice seeking. 🎱

import random
print('welcometo 8 ball wizard')
print('enter your question to make a choice on it')
quest = (input(print('Question:')))

ans = ['Yes - definitely.','It is decidedly so.','Without a doubt.','Reply hazy, try again.','Ask again later.','better not tell you now.','My sources say no.','Outlook not so good.','Very doubtful.']

answer = random.choice(ans)

print('thinking of your answer')
print('🪄',answer)