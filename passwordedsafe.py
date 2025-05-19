import getpass
password = '1221ha'
attempt = 5

while attempt > 0:

    enter = getpass.getpass('enter password:-')

    if enter == password:
        print('✅Access granted!welcome hithesh')
        break
    else:
        attempt -= 1
        print(f'wrong password-you have {attempt} attempts left')
if attempt == 0:
    print('5 attempts finished!run the pgm again')