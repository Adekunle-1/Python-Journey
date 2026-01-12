import random

print('This is a guessing game. There is a cash price of #100 if you can guess correctly')
playgame = 'yes'

while playgame == 'yes':
    print('Number of tries: Difficult = 5, Medium = 4 and Easy = 3')
    numOfTrials = int(input('enter num of trials here: '))
    if numOfTrials == 3:
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
    elif numOfTrials == 4:
        numToGuess = random.randrange(1, 30)
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
    elif numOfTrials == 5:
        numToGuess = random.randrange(1, 50)
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
    else:
        print ('Incorrect selection, you can only select 3 or 4 or 5. Try again')
        numOfTrials = int(input('enter num of trials here: '))
        continue

    if numOfTrials == 0 and userInput != numToGuess:
        print ('Game Over.. Try Again')
        print (f'This is your secret number: {numToGuess}')
    playgame =  input('DO you wanna play another game? enter yes to try again')


            


     