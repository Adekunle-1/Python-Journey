import random

#A dictionary containing a list of words and hints
dictOfWords = {
    "pencil": "a writing material",
    "laptop": "a computing device",
    "notebook": "a book used for writing notes",
    "phone": "a device used for communication",
    "keyboard": "an input device for typing",
    "mouse": "a pointing device for computers",
    "chair": "an object used for sitting",
    "table": "a piece of furniture with a flat surface",
    "book": "a collection of written pages",
    "bottle": "a container used for liquids"
}

#Extract a list of word in the dictionary
listOfWords = []
for words in dictOfWords.keys():
    listOfWords.append(words)

#Randomly selects a word from the list
wordToGuess = random.choice(listOfWords)

#Extracts the hint of the word and create dashes as placeholders for the word
hint = dictOfWords[wordToGuess]

wordPlaceholder = ""
for x in wordToGuess:
    wordPlaceholder +=  "*"

# Print Instruction and Hints
print("You have 3 lives.\n"
    "Hangman is a word-guessing game.\n"
    "Guess one letter at a time.\n"
    "Each wrong guess reduces your lives by 1.\n"
    "Try to guess the whole word before you run out of lives!\n"
    "Your word is", hint)

#GamePlay
lives = 3
wordPlaceholder = list(wordPlaceholder)
guessedLetters = set()
while lives > 0:
    print ("current word: ", " ".join(wordPlaceholder))
    playerInput = input("ENTER A LETTER: ")
    if playerInput.isalpha():
        if len(playerInput) == 1:
            pass
        else:
            print ('ERROR!! ENTER A SINGLE ALPHABET')
            continue
    else:
        print ('ERROR!! ENTER AN ALPHABET')
        continue


    if playerInput in guessedLetters:
        print ('You already guessed', playerInput)
        continue

    guessedLetters.add(playerInput)

    if playerInput in wordToGuess:
        for i in range(len(wordToGuess)):
            if wordToGuess[i] == playerInput:
                wordPlaceholder[i] = playerInput
                 
    else:
        lives -= 1
        print (f"Wrong!!! You now have {lives} lives")

    if "*" not in wordPlaceholder:
        print ("Game Won!!, the word to guess is: ", wordToGuess)
        break 

if lives == 0:
    print ("You lost!! The word to guess is: ", wordToGuess)




