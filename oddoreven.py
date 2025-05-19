#odd or even pgm
num = int(input('enter the number range:'))
even = 0
odd = 0

for i in range(1,num+1):
    if i%2 == 0:
        print(f'{i} is even')
        even += 1
    else:
        print(f'{i} is odd')
        odd += 1
    
print('number of odds and evens')
print(f'{odd} odds')
print(f'{even} evens')
