import random
pass_length = int(input('How Many Digits Password Do You Need:-'))  #max=72
passcode = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
if pass_length<=6:
    print('Your password is very weak!!')
elif pass_length<=10:
    print("Your password is weak!!")
elif pass_length<=20:
    print('Your password is strong!!')
else:
    print("Your password is very strong")
print('Your Password is:',''.join(random.sample(passcode,pass_length)))
