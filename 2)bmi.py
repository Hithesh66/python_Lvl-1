mass = int(input("enter body weight:"))

height = float(input("enter height:"))
if mass <= 0 or height <= 0:
    print('are you serious,🙄-try again')
else:
  BMI = float(mass/(height*height))

print(f"{BMI:.2f}")
#height*height=height^2

if BMI < 18.5:
    print('you are underweight🩻')
elif 18.5 <= BMI <24.9:
    print('you are in healthy range🏋️')
elif 25 <= BMI <29.9:
    print('a bit overweight⚖️')
else :
    print('you are overweight🐘')


