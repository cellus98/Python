def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 3:
                guess = input('Sorry wrong answer. Try again. ')
                attempt = attempt + 1
    if attempt == 3:
                print('The correct answer is ' + answer)
                
score = 0
print('Guess the Animal!')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastes land animal?')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal?')
check_guess(guess3, 'blue whale')
guess4 = input('Which one of these is a fish (Type A, B, C, or D) ?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n ')
check_guess(guess4, 'C')

print('Your score is ' + str(score))

