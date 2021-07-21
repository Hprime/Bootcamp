import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('Okay! '+ player_name+ ' I need you to Guess a number between 1 and 10:')
print()

def game():
    number = random.randint(1, 10)
    print("You have 5 chances to guess that number, Alright, Lets roll!")
    i = 1
    r = 1
    while i<6:  
        user_number = int(input('Enter your number: ')) 
        if user_number < number:
            print("Your guess is too low")
            print()
            print("You now have " + str(5-i)+ " chances left" )
            i = i+1
        elif user_number > number:
            print("Your guess is too high")
            print()
            print("You now have " + str(5-i)+ " chances left" )
            i = i+1
        elif user_number == number:
            print("\nYou have guessed the correct number!")
            print("Nailed it!")
            r = 0;
            break
        else:
            print("This is an invalid number. Please try again")
            print("You now have " + str(5-i)+ " chances left" )
            continue
    if r==1:
        print("Ooooh, Sorry you lost the game!!")
        print()
        print("My number was = " + str(number))
        print("Better luck next time!")

def main():
    game()
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
        else:
            break
main()
print("\nEnd of the Game! Thank you for playing!")
