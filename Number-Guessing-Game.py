import random
n = random.randint(1, 50)
count = 0
print('Note: You have to guess the number in 5 attempts')
count += 1
guess = int(input('Enter a number between 1-50: '))
while n != guess and count < 5:
    if guess < n:
        print("Sorry, Guess again. Number is Low")
        count += 1
        print(f'You have {6 - count} attempts left')
        guess = int(input('Enter a number: '))
    elif guess > n:
        print("Sorry, Guess again. Number is High")
        count += 1
        print(f'You have {6 - count} attempt left')
        guess = int(input('Enter a number: '))
    else:
        break

if count == 5 and n != guess:
    print("Sorry, You lost the game")
    print("The number is:", n)
elif count <= 3:
    print("You are Truly a Legend")
    print(f'You guessed it in just {count} attempt')
else:
    print("You guessed it right!!")
    print(f'You guessed it in just {count} attempt')



