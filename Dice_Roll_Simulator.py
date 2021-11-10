import random
min_value = 1
max_value = 6
roll_again = 'Yes'
while roll_again == 'Yes' or roll_again == 'Y':
    print('Dice Rolling...')
    print(random.randint(min_value, max_value))
    print(random.randint(min_value, max_value))
    roll_again = input('Roll the Dice Again(Yes/Y)?').capitalize()
    if roll_again == 'n'.capitalize():
        break
