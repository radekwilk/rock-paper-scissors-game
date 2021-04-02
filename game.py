import random

myList = ['rock', 'paper', 'scissors']

while True:
    # getting input from the user
    user_input = input(
        'Ready to play game? What is your choice? Type rock, paper or scissors: ')
    user_input = user_input.lower()  # input to lower case
    computer_choice = random.choice(myList)  # random selection by computer

    # if user enter anuthing else than approved rock, paper or scissors is asked to enter it again
    if user_input != 'rock' and user_input != 'paper' and user_input != 'scissors':
        print(
            f'Your choice is {user_input}. You can only enter rock, paper or scissors. Please try again!')
        continue
    # if user enter correct string (rock, paper of scissor), checking who got what and decides how wins. If computer wins, is asking to play again. If user wins game is over
    else:
        if user_input == computer_choice:
            print(
                f'Your choice is {user_input}. Computer got {computer_choice}. It is a draw. Try again!')
            continue
        elif user_input == 'rock' and computer_choice == 'paper':
            print(
                f'Your choice is {user_input}. Computer got {computer_choice}. Computer wins!!! Try again!')
            continue
        elif user_input == 'rock' and computer_choice == 'scissors':
            print(
                f'Your choice is {user_input}. Computer got {computer_choice}. You won!!!')
            break
        elif user_input == 'paper' and computer_choice == 'rock':
            print(
                f'Your choice is {user_input}. Computer got {computer_choice}. You won!!!')
            break
        elif user_input == 'paper' and computer_choice == 'scissors':
            print(
                f'Your choice is {user_input}. Computer got {computer_choice}. Computer wins!!! Try again!')
            continue
        elif user_input == 'scissors' and computer_choice == 'rock':
            print(
                f'Your choice is {user_input}. Computer got {computer_choice}. Computer wins!!! Try again!')
            continue
        elif user_input == 'scissors' and computer_choice == 'paper':
            print(
                f'Your choice is {user_input}. Computer got {computer_choice}. You won!!!')
            break
