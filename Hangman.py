from SenseHatHangman import SenseHatHangman
shh = SenseHatHangman()
guessedWord = list("monitor")
displayed = list("-------")
incorrectGuesses = list("")
correctGuesses = list("")
gameOver = False

def containsDash(guessedWord = ''):
    for c in guessedWord:
        if c == '-':
            return True
     
shh.start()
while not(gameOver):
    print('The incorrect guesses:', incorrectGuesses)
    print('The correct guesses:', correctGuesses)
    print('The guessed word so far:', displayed)
    char = input("Enter a character:")
    if char.isnumeric() or char in incorrectGuesses or char in correctGuesses:
        print("Character already guessed or is numeric.")
    else:
        for i in range(len(guessedWord)):
            c = guessedWord[i]
            if c == char:
                displayed[i] = c
        if char in guessedWord:
            correctGuesses.append(char)
        else:
            incorrectGuesses.append(char)
            shh.wrongGuess()  
    gameOver = len(incorrectGuesses)>10 or not(containsDash(displayed))

if len(incorrectGuesses)>10:
    shh.gameOver()
elif not(containsDash(displayed)):
    shh.winner(guessedWord)
