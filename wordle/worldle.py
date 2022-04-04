#Collect user input, create variables depicting their current game state
firstCharacter = input("enter first character -> ")
secondCharacter = input("enter second character -> ")
thirdCharacter = input("enter third character -> ")
fourthCharacter = input("enter fourth character -> ")
fifthCharacter = input("enter fifth character -> ")
unusedCharacters = input("enter a string of unused letters -> ")
unorderedLetters = input("enter a string of letters that must be used -> ")

# Open CSV, store all data in a list, then close the CSV
wordFile = open("wordle/words.txt", "r")
setOfWords = []
for line in wordFile:
    stripped_line = line.strip()
    setOfWords.append(stripped_line)
wordFile.close()

# Return list of possible words with set letters (letters in green on wordle)
setofWordsWithSetLetters = []
for word in setOfWords:
    if (word[0] == firstCharacter or firstCharacter == "") and (word[1] == secondCharacter or secondCharacter == "") and (word[2] == thirdCharacter or thirdCharacter == "") and (word[3] == fourthCharacter or fourthCharacter == "") and (word[4] == fifthCharacter or fifthCharacter == ""):
        setofWordsWithSetLetters.append(word)

# removes words that contain unused letters from our list
listToRemove = []
for word in range(len(setofWordsWithSetLetters)):
    possible = True
    for letter in setofWordsWithSetLetters[word]:
        for unusedCharacter in unusedCharacters:
            if (unusedCharacter == letter):
                possible = False
    if (not possible):
        listToRemove.append(setofWordsWithSetLetters[word])
for i in listToRemove:
    setofWordsWithSetLetters.remove(i)

#Finally removes words that don't contain needed letters (yellow/orange letters in wordle)
listToRemove = []
for wordIndex in range(len(setofWordsWithSetLetters)):
    possible = True
    for unorderedLetter in unorderedLetters:
        if (not (unorderedLetter in setofWordsWithSetLetters[wordIndex])):
            possible = False
    if (not possible):
        listToRemove.append(setofWordsWithSetLetters[wordIndex])
for i in listToRemove:
    setofWordsWithSetLetters.remove(i)

# Prints an array with all possible options
print(setofWordsWithSetLetters)

