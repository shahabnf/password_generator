
import string,random

while True :
    length = int(input('Please enter your preferred password length (Enter 0 to EXIT): '))
    if length == 0 or length == 00 : break
    chars =  string.ascii_letters + string.digits + '!@#$%^&*-+'
    # print(chars)

    password = ''.join([random.choice(chars) for i in range(length)])
        
    print('Your password is : {}'.format(password))

    while True :
        answer = input('Do you want another passwrord (y/n): ').lower()

        if answer == 'n' or answer == 'y' :
            break
    if answer == 'n' :
        print('Thank you')
        break