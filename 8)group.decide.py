#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. 
# The hat decides which of the four "Houses" each first-year student goes to:

gryffindor_sc = 0
ravenclaw_sc = 0
hufflepuff_sc = 0
slytherin_sc = 0

print('Q1)do you like dawn or dusk?')
print('1)Dawn')
print('2)Dusk')
ans1 = int(input('answer='))
if ans1 == 1:
    gryffindor_sc,ravenclaw_sc = gryffindor_sc+1,ravenclaw_sc+1
elif ans1 == 2:
    hufflepuff_sc,slytherin_sc = hufflepuff_sc+1,slytherin_sc+1
else:
    print('wrong input')

print('Q2) When I’m dead, I want people to remember me as:')    
print('1)The Good')
print('2)The great')
print('3)The wise')
print('4)The bold')
ans2 = int(input('answer='))

if ans2 == 1 :
    hufflepuff_sc=hufflepuff_sc+2
elif ans2 == 2:
    slytherin_sc=slytherin_sc+2
elif ans2 == 3:
    ravenclaw_sc=ravenclaw_sc+2
elif ans2 == 4:
    gryffindor_sc=gryffindor_sc+2
else:
    print('wrong input')

print('which of the instruments pleases your ear')
print('1)The violin')
print('2)The trumbet')
print('3)The piano')
print('4)The Drum')

ans3 = int(input('answer='))

if ans3 ==1:
    slytherin_sc=slytherin_sc+4
elif ans3 ==2:
    hufflepuff_sc=hufflepuff_sc+4
elif ans3 ==3:
    ravenclaw_sc=ravenclaw_sc+4
elif ans3 ==4:
    gryffindor_sc=gryffindor_sc+4
else:
    print('wrong input')

print(f"score for gryffindor={gryffindor_sc:.1f}")
print(f"score for ravenclaw={ravenclaw_sc:.1f}")
print(f"score for slytherin={slytherin_sc:.1f}")
print(f"sccore for hufflepuff={hufflepuff_sc:.1f}")

scores = {
    "gryffinddor":gryffindor_sc,
    "ravenclaw":ravenclaw_sc,
    "slytherin":slytherin_sc,
    "hufflepuff":hufflepuff_sc
}
top = max(scores,key = scores.get)
print(f"you are selected to {top}🏆")