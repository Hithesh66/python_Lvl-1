#the height requirement is 137 cm and the cost is 10 credits

height =  int(input('enter your height:'))

credits = int(input('enter the credits left:'))

min_h = 137
min_c = 10

if height >= min_h and credits >= min_c:
    print('enjoy the ride')
elif height >= min_h and credits < min_c:
    print('you dont have enough credits')
elif height < min_h and credits >= min_c:
    print('you are not tall enough to ride')
else:
    print('you have not met either requirements')