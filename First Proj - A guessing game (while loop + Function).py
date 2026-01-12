import random 

# plays ONE round and returns 'Win' or 'Loss'
def play_game (NumOfTrials, max_num): 
    print(f'You need to enter a number between 1 and {max_num}'.upper())
    NumToGuess = random.randrange(1, max_num + 1)
    
    while NumOfTrials > 0:
        userInput = int(input(f'Enter your guess here. You have {NumOfTrials} left:\n  '.upper()))

        if userInput == NumToGuess:
            print ('Congratulations!!!')
            return 'Win'
        
        if userInput > NumToGuess:
            print ('Too high, try a lower number')
        else:
            print ('Too low, try an higher number')
        
        NumOfTrials -= 1

    print ('Game Over.. Try Again')
    print (f'This was the secret number: {NumToGuess}')
    return 'Loss'



print ('The difficulty level is determined by the number of tries. Hard = 5, Medium = 4, Easy = 3'.upper())
playgame = input('click any botton to begin, click q to quit\n'.upper())
while playgame != 'q':
    NumOfTrials = int(input('How many times to do you want to try? \n '))
    
    if NumOfTrials == 3:
        result = play_game (3, 10)
    elif NumOfTrials == 4:
        result = play_game (4, 30)
    elif NumOfTrials == 5:
        result = play_game (5, 50)
    else:
        print('incorrect selection, pick a number in 3, 4 and 5')
        continue
    
    playgame = input('click any botton to begin this game, click q to quit\n'.upper())

print ('THANKS FOR PLAYING')
    