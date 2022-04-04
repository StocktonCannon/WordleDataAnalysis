import csv
from functools import reduce
from socket import create_server

def reduceList(guess,solution,options):
    numOfPossibilities = len(options)
    
    


guessFile = open('archive/valid_guesses.csv')
guesscsvreader = csv.reader(guessFile)
solutionFile = open('archive/valid_solutions.csv')
solutioncsvreader = csv.reader(solutionFile)
letterFile = open('archive/letters.csv')
lettercsvreader = csv.reader(letterFile)
validSolutions = []
validGuesses = []
letterCount = dict()
for row in guesscsvreader:
    validGuesses.append(row[0])

for row in solutioncsvreader:
    validSolutions.append(row[0])



for currGuess in validGuesses:
    for currTarget in validSolutions:
        reduceList(currGuess,currTarget,validSolutions)


