import random

print ('Hello, what is your name?')
name = input()

print ('Hi ' + name + ', I am thinking of a number between 1 and 20.')
secret_number = random.randint(1,20) # return a random integer

for guess_taken in range(1,7):
    try: 
        guess = int(input('Take a guess! \n'))

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high')
        else:
            break
    except(ValueError):
        print("Please input a number!")

if guess == secret_number:
    if guess_taken == 1:
        print('Bingo, you got it right in one go!')
    print('Bingo, you got it right in ' + str(guess_taken) + ' goes.')
else:
    print('Nope, the number I was thinking is ' + str(secret_number))

