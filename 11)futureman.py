#The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀
#destination weight=Earth weight × relative gravity
#Number	Planet	Relative Gravity
#6	Uranus	0.89,
#7	Neptune	1.14
mass = float(input('enter your mass on earth:'))
print('1-mercury')
print('2-venus')
print('3-mars')
print('4-jupiter')
print('5-saturn')
print('6-uranus')
print('7-neptune')
planet = int(input('enter your destination number:'))
print('your mass at the destination is :')
if planet == 1:
    desti_weight = mass * 0.38
    print(desti_weight)
elif planet == 2:
    dest = mass * 0.91
    print(dest)
elif planet == 3:
    dest = mass * 0.38
    print(dest)
elif planet == 4:
    dest = mass * 2.53
    print(dest)
elif planet == 5:
    dest = mass * 1.07
    print(dest)
elif planet ==6:
    dest = mass * 0.89
    print(dest)
elif planet == 7:
    dest = mass * 1.14
    print(dest)

else:
    print('invalid planet number')
    

