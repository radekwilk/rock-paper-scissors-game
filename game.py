import random

myList = ['rock', 'paper', 'scissors']
humanWins = False


def playGame():
    humanChoice = input(
        'Ready to play game? What is your choice? Type rock, paper or scissors. ')
    computerChoice = random.choice(myList)
    result = [humanChoice.lower(), computerChoice]
    return result


while (humanWins) == False:
    result = playGame()  # geting user input and random choice of the computer
    userImput = result[0]  # user choice
    compChoice = result[1]  # randomly selected by computer

    # if user enter anuthing else than approved rock, paper or rock is asked to enter it again
    if userImput != 'rock' and userImput != 'paper' and userImput != 'scissors':
        print(
            f'Your choice is {userImput}. You can only enter rock, paper or scissors.Please try again!')
        continue
    # if user enter correct string (rock, paper of scissor), checking who got what and decides how wins. If computer wins, is asking to play again. If user wins game is over
    else:
        if userImput == compChoice:
            print(
                f'Your choice is {userImput}. Computer chose {compChoice}. It is a draw. Try again!')
            continue
        elif userImput == 'rock' and compChoice == 'paper':
            print(
                f'Your choice is {userImput}. Computer chose {compChoice}. Computer wins!!!. Try again!')
            continue
        elif userImput == 'rock' and compChoice == 'scissors':
            print(
                f'Your choice is {userImput}. Computer chose {compChoice}. You won!!!')
            humanWins = True
            break
        elif userImput == 'paper' and compChoice == 'rock':
            print(
                f'Your choice is {userImput}. Computer chose {compChoice}. You won!!!')
            humanWins = True
            break
        elif userImput == 'paper' and compChoice == 'scissors':
            print(
                f'Your choice is {userImput}. Computer chose {compChoice}. Computer wins!!!. Try again!')
            humanWins = False
            continue
        elif userImput == 'scissors' and compChoice == 'rock':
            print(
                f'Your choice is {userImput}. Computer chose {compChoice}. Computer wins!!!. Try again!')
            humanWins = False
            continue
        elif userImput == 'scissors' and compChoice == 'paper':
            print(
                f'Your choice is {userImput}. Computer chose {compChoice}. You won!!!')
            humanWins = True
            break
