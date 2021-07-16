import random
while True:

    user_choice = input("Enter a choice (rock, paper, or scissors?) ")
    random_num = random.randint(0,2)
    if random_num == 0:
        cpu_choice = "rock"
    elif random_num == 1:
        cpu_choice = "paper"
    elif random_num == 2:
        cpu_choice = "scissors"

    print()
    print("your choice:" ,user_choice)
    print("computer's choice:" ,cpu_choice)

    print()

    if user_choice == "rock":
        if cpu_choice == "rock":
            print("It's a tie!")
        elif cpu_choice == "paper":
            print("Paper covers rock!, You lost")
        elif cpu_choice == "scissors":  
            print("Rock smashes scissors, You win")
    elif user_choice == "paper":
            if cpu_choice == "paper":
                print("It's a tie!")
            elif cpu_choice == "rock":
                print("Paper covers rock!, You win")
            elif cpu_choice == "scissors":
                print("You lost")
    elif user_choice == "scissors":
            if cpu_choice == "scissors":
                print("It's a tie!")
            elif cpu_choice == "rock":
                print("Rock smashes scissors, You lost")
            elif cpu_choice == "paper":
                print("Scissors cut paper!, You win")
    print()