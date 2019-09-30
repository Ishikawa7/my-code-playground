'''
Guessing Game Challenge

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed
correctly and how many guesses it took!
'''
import random


def game():
    trys = 0
    randomInt = random.randint(0, 100)
    # print(randomInt)
    guess = int(input('Make a guess '))
    while (randomInt != guess):
        if guess < 0 or guess > 100:
            print("OUT OF BOUNDS")
            break
        elif abs(randomInt - guess) > 10:
            print('COLD')
            break
        else:
            print('WARM')
            break
    else:
        print('YOU WON, in {}'.format(trys + 1))
        return

    while (guess != randomInt):
        trys += 1
        oldGuess = guess
        guess = int(input('Make a guess '))
        if guess < 0 or guess > 100:
            print("OUT OF BOUNDS")
            continue
        elif abs(randomInt - oldGuess) < abs(randomInt - guess):
            print('COLDER')
            continue
        else:
            print('WARMER')
            continue
    else:
        print('YOU WON, in {}'.format(trys + 1))
        return


# GAME MENU
choice = '-'
while (choice != 'end'):
    print("Commands: 'start' to start the game --- 'end' to end the game ")
    choice = input('Input choice: ')
    if choice == 'end':
        break
    elif choice == 'start':
        game()
    else:
        print('Invalid input, retry')
