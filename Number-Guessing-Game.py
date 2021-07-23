import random
n = random.randint(10, 100)
count = 0
print('You have the guess the number in 5 attempt: ')
count += 1
guess = int(input('Enter a number between 1-100: '))
while n != guess and count < 5:
    if guess < n:
        print(n)
        print("Sorry, Guess again. Too Low")
        count += 1
        print(f'You have {6 -count} attempt left')
        guess = int(input('Enter a number: '))
    elif guess > n:
        print("Sorry, Guess again. Too High")
        count += 1
        print(f'You have {6 - count} attempt left')
        guess = int(input('Enter a number: '))
    else:
        break
        
if count == 5 and n != guess:
    print("Sorry, You lost the game")
    print("The number is:", n)
else:
    print("You guessed it right!!")
    print(f'You guessed it in just {count} attempt')
    
