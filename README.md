# Overview


This project contains various files used in manipulating, organizing, and displaying a wordle data set found on kaggle.com.  [Kaggle-data](https://www.kaggle.com/datasets/bcruise/wordle-valid-words)
This data set holds all the valid guesses in the wordle game and all the valid solutions.  Our main purpose is to find a more optimal way to beat wordle in less guesses.  This is done by finding the most common letters used in wordle, the most common letter positions, and allowing us to input our current game state to get a list of remaining posibilities.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](https://www.youtube.com/watch?v=iPTvy4AFEok)

# Data Analysis Results

* What are some of the best starting guesses in wordle? tares, chino
* Which letters are used most? e - 1233 , a - 979, t-729, s-669, r-899, o-754, l-719, 
* On average what is the least amount of guesses I can use to get my answer? Out of about a 100 games, i got an average of about 3.7 guesses

# Development Environment

* VS Code
* Python Language
* CSV Library


# Useful Websites

* [Kaggle](https://www.kaggle.com/)
* [Python CSV Tutorial](https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/)

# Future Work

* Solve for letter Position
* Read list of possibilties and give optimal word guess
