import os
import random
import os.path
WordsFile = open("C:\\Users\\Anas Othman\\Desktop\\Coding\\Python\\Hangman\\Words.txt", "r")
WordsList = ["None"] * 1500
WrongCount = 0
WrongCountStr = str(WrongCount)
RightGuessCount = 0
GuessWord = ""
Guesses = ""
Won = False

def WordsInList():
	for i in range(1500):
		WordsList.pop(i)
		WordsList.insert(i, WordsFile.readline())

def PrintNewScreen(WrongCountStr):
	os.system('cls')
	HMFileName = "C:\\Users\\Anas Othman\\Desktop\\Coding\\Python\\Hangman\\" + WrongCountStr + ".txt"
	HangmanFile = open(HMFileName, "r")
	print(HangmanFile.read())
	for j in range(len(Word) - 1):
		print(Blanks[j], "  ", end="")
	print("")
	print("")
	print("Guessed letters: " + Guesses)

WordsInList()

RandomNum = random.randint(1, 1501)
Word = WordsList[RandomNum]
LetterList = ["None"] * (len(Word) - 1)
for k in range(len(Word) - 1):
	LetterList.pop(k)
	LetterList.insert(k, Word[k:(k + 1)])
Blanks = ["_"] * (len(Word) - 1)

while WrongCount < 6:

	PrintNewScreen(WrongCountStr)

	Guess = input("Type letter: ")
	Guesses = Guesses + "  " + Guess

	for l in range(len(Word) - 1):
		if Guess == LetterList[l]:
			Blanks.pop(l)
			Blanks.insert(l, Guess)
			RightGuessCount = RightGuessCount + 1

	if RightGuessCount == 0:
		WrongCount = WrongCount + 1
		WrongCountStr = str(WrongCount)
	else:
		RightGuessCount = 0

	for m in range(len(Word) - 1):
		if Blanks[m] != "_":
			GuessWord = GuessWord + Blanks[m]

	if len(GuessWord) == (len(Word) - 1):
		Won = True
		break
	else:
		GuessWord = ""

PrintNewScreen(WrongCountStr)
if Won == False:
	print("The word was: " + Word)
else:
	print("You won!")
