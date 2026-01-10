import random

print('this is a guessing game, you have 3 trials. There is a cash price of #100 if you can guess correctly. guess a number from 1 - 10').upper()
playgame = 'yes'

while playgame == 'yes':
    numOfTrials = 3
    numToGuess = random.randrange(1, 10)
    while numOfTrials > 0:
            userInput = int(input(f'Enter your pick here, you have {numOfTrials} left: '))
            if userInput == numToGuess:
                print ('Success')
                break
            else:
                print ('try again')
                numOfTrials -= 1

    if numOfTrials == 0 and userInput != numToGuess:
        print ('Game Over')
        print (f'This is your secret number: {numToGuess}')
    playgame =  input('DO you wanna play another game: yes or no')  


