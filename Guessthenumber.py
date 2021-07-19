import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('Okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')
print()

print("You only have 5 chances to guess the number. Alright, lets roll!")



while number_of_guesses < 5:
    guess = int(input("Guess a number:- ")) 
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    print("Nailed it!")
else:
    print('You did not guess the number, The number was ' + str(number))
    print("Better Luck Next time!")
    