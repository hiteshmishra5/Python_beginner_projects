def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt <= 2:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score += 1
            still_guessing = False
        else:
            if attempt <= 1:
                guess = input("Sorry Wrong Answer, Try again? ")
            attempt += 1
    if attempt == 3:
        print("The Correct answer is: ", answer)


score = 0
print("Guess The Word:")
guess1 = input("Which bear lives in the north pole? ")
check_guess(guess1, 'polar bear')
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, 'Cheetah')
guess3 = input("Which is the largest animal? ")
check_guess(guess3, 'Blue Whale')
print("Your Score is: ", score)
