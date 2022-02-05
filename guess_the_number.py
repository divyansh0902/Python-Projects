import random

'''def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}:"))
        print(guess)
        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too high")

    print("congrats, right guess {random_number}")'''

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = random.randint(low,high)
        feedback = input(f'is {guess} too high (H),too low (L) or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

        print(f'you guessed number {guess}, correctly')





computer_guess(1000)