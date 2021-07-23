import random
n = random.randint(10,100)
count = 0
guess = int(input('Enter a number b/w 1-100:'))
while n != guess:
    if guess < n:
        print("Sorry, Guess again. Too Low")
        count += 1
        guess = int(input('Enter a number:'))
    elif guess > n:
        print("Sorry, Guess again. Too High")
        count += 1
        guess = int(input('Enter a number:'))
    else:
        break

print('Congrats!! You guessed it right')
print(f'You guessed it in {count} attempt!!')
