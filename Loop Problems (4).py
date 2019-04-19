## Elyas - Tuesday November, 14th 2017 ## 


# Question 4

"""

4)	Write a program that checks for the word “monkey”. Your checker will first ask for a the word “monkey”, then repetitively ask the user to check the word. When the user types the same word, acknowledge that the right password was provided. Do this WITHOUT if statements.

"""

word = str(input("What is your word?")) # Asks the user to input a workd
checker = str(input("Check your word:")) # Asks the user to input the same word again

while checker != word: # If the word is not the same then it will ask the user to check the word by putting in the same word he put in the beginning
    checker = str(input("Check your word:")) # Explained above
while checker == word: # If the user inputs the same word that he inputted in the beginning then it will print "correct" and end the code
    print("Correct!") # Explained above
    break

    
# The code will ask the user to input any word and then it ask it to check the word by typing the word again
# if it's typed again correctly than it will print 'correct'
# If the program is not typed correctly than it will ask the person to re-type the word until it's correct


