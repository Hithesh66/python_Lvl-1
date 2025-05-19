#if i is a multiple of 3 print  fizz,if i is a multiple of 5 print buzz
# and if i is a multiple of both print fizzbuzz 
for i in range(1,101):
   if i % 3 == 0:
    print('fuzz')
   elif i % 5 == 0:
    print('buzz')
   elif i % 3 ==0 and i % 5 == 0:
    print('fizzbuzz')
   else:
    print(i)
#tricky 