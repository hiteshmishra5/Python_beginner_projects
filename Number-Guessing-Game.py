import random
n = random.randint(10,100)
guess = int(input('Enter a number b/w 1-100:'))
while n != guess:
    if guess < n:
        print("Too Low")
        guess = int(input('Enter a number:'))
    elif guess > n:
        print("Too High")
        guess = int(input('Enter a number:'))
    else:
        break

print("You guessed it right!!")