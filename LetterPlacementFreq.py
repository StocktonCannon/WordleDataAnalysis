import csv
from socket import create_server

# Opens all the needed files
guessFile = open('archive/valid_guesses.csv')
guesscsvreader = csv.reader(guessFile)
solutionFile = open('archive/valid_solutions.csv')
solutioncsvreader = csv.reader(solutionFile)
letterFile = open('archive/letters.csv')
lettercsvreader = csv.reader(letterFile)

# creates two empty list and a dictionary that will be filled with our csv data
validSolutions = []
validGuesses = []
letterCount = dict()

# Loops through the csv files and appends rows to our lists
for row in guesscsvreader:
    validGuesses.append(row[0])

for row in solutioncsvreader:
    validSolutions.append(row[0])

# Creates a dictionary with letter and position titles followed by values of zeros
for row in lettercsvreader:
    letterCount[row[0]] = 0


# loops through each word, and then each letter.  Finally increments a dictionary key's value by one depending on letter and position.
for word in validSolutions:
    for i in range(len(word)):
        letterCount[word[i] + str(i)] += 1

print(letterCount)