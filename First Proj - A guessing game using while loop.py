import random

print('this is a guessing game, you have 3 trials. There is a cash price of #100 if you can guess correctly. guess a number from 1 - 10'.upper())
playgame = 'yes'

while playgame == 'yes':
    numOfTrials = 3
    numToGuess = random.randrange(1, 10)
    while numOfTrials > 0:
            userInput = int(input(f'Enter your guess here, you have {numOfTrials} left: '))
            if userInput == numToGuess:
                print ('Congratulations!!!')
                break
            else:
                if userInput > numToGuess:
                    print ('Too high, try a lower number')
                else:
                    print ('Too low, try an higher number')
                numOfTrials -= 1

    if numOfTrials == 0 and userInput != numToGuess:
        print ('Game Over.. Try Again')
        print (f'This is your secret number: {numToGuess}')
    playgame =  input('DO you wanna play another game? enter yes to try again')  


