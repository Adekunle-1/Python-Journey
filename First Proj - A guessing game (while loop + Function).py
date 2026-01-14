import random 

# plays ONE round and returns 'Win' or 'Loss'
def play_game (NumOfTrials, max_num): 
    print(f'You need to enter a number between 1 and {max_num}'.upper())
    NumToGuess = random.randrange(1, max_num + 1)
    
    while NumOfTrials > 0:
        try: 
            userInput = int(input(f'Enter your guess here. You have {NumOfTrials} left:\n  '.upper()))
        except ValueError:
            print ('Please enter a valid number')
            continue

        if userInput == NumToGuess:
            print ('Congratulations!!! YOU WON!!')
            return 'Win'
        
        if userInput > NumToGuess:
            if userInput > max_num:
                print (f'Incorrect, try a lower number. Maximum number should be {max_num}')
            else:
                print('Incorrect, try a lower number')
        else:
            print ('Incorrect, try an higher number')
        
        NumOfTrials -= 1

    print ('Game Over.. Try Again')
    print (f'This was the secret number: {NumToGuess}')
    return 'Loss'





# game start, replay, and scroe count logic.
print ('The difficulty level is determined by the number of tries.'.upper())
print ('Hard = 5 tries, Medium = 4 tries, Easy = 3')
playgame = input('click any button to begin, click q to quit\n'.upper())
score = 0
total_game = 0

while playgame != 'q':
    try:
        NumOfTrials = int(input('How many times do you want to try? \n '.upper()))
    except ValueError:
        print ('Please enter a valid number')
        continue
    
    if NumOfTrials == 3:
        result = play_game (3, 10)
    elif NumOfTrials == 4:
        result = play_game (4, 30)
    elif NumOfTrials == 5:
        result = play_game (5, 50)
    else:
        print('incorrect selection, pick a number in 3, 4 and 5')
        continue
    
    total_game += 1
    if result == 'Win':
        score += 1

    print(f'Your score is {score}, and you have played a total of {total_game} game(s)')
    playgame = input('click any botton to play again, click q to quit\n'.upper())

print ('THANKS FOR PLAYING')