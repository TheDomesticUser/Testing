# Elyas 12/7/17 Question 1



'''

Write a program that requires the user to guess a generated number between 1
and 10.  You will display the appropriate messages prompting the user.  You will
also need to keep track of and display the following information (ideally after
the guess or during quit):
Total Guesses
The magic number
Win(s)
Quit (or give up)

'''

# THIS CODE IS TRASH
   
import random

name = str(input("What is your name?")) # Asks the user to input their name
the_name = name.upper()
print ("Hello, ",the_name, ", Welcome to the Magic Number Game!") # Prints a greeting with the inputted name (Welcomes to player)
print ("Type playgame() to start.") # The user must type "play_game()" (Without quotes) to start the game
# When "playgame()" (without quotes) is typed it will print everything below by starting the game

def playgame():
    print ("Welcome to my humble abode, I am MagicMan, Can you guess the magic number I have in mind?") # Prints a greeting message - welcomes the player to the game
    print ("I wish you all the best. Note: You have 5 guesses.")
    
    magic_number = random.randint(1,10) # Randint pick a random number from 1-10 to make the magic number
    amount_of_guess = 0 
    amount_of_wins = 0
    amount_of_loss = 0

    while amount_of_guess < 5: # This code determines the amount of guesses the person has which in this case is 5
        guess_num = int(input("Your guess: "))
        amount_of_guess = amount_of_guess + 1

        if guess_num > 10:
            print ("Try a number between 1 and 10") # This code tells the user to type a number from 1-10 if a number above 10 is typed

        if guess_num < magic_number: # If the guessed number is below the magic or random number then it will tell the user that they guessed too low
            print ("You guessed too low!")

        if guess_num > magic_number: # If the guessed number is above the magic or random number then it will tell the user that they guessed too high
            print ("You guessed too high!")

        if guess_num == magic_number: # When the magic or random number is guessed it will tell the user the amount of tries out of five that it took them to guess it
            print ("You guessed the number in",amount_of_guess,"guesses")
            break
    if guess_num != magic_number: # If w ithin the 5 tries the person does not guess a number equal to the magic number then it will the user the amount of tries 
            print ("You took more than 5 tries. The number was", magic_number)                          # - it took them and it will also reveal the magic number
        
    if amount_of_guess >= 1 and amount_of_guess < 3: # If it took the person 1-3 guesses to get to guess the magic number, it will print "Well Done" (without quotes)
        print("Well Done!")
    elif amount_of_guess >= 3 and amount_of_guess < 5: # If it took the person 3-5 guesses to get to guess the magic number, it will print "Very Good" (without quotes)
        print("Very Good")
    elif amount_of_guess >= 5 and amount_of_guess == 6: # If it took the person 5-6 guesses to get to guess the magic number, it will print "Good Try" (without quotes)
        print("Good Try")

    if amount_of_guess < 5:
        amount_of_wins = amount_of_wins + 1 # If the user wins a game then it will add 1 win everytime to their total win count
    if amount_of_guess >= 5:                                                                            
        amount_of_loss = amount_of_loss + 1 # If the user losses a game then it will add 1 loss everytime to their total loss count

    print ("You have won", amount_of_wins, "time(s) and lost", amount_of_loss, "time(s)")
# When the player guesses the magic number it will tell them they have have won, print the number of times they guessed the magic number if they continued to play
# - it will tell them the amount of times they lost or didn't guess the magic number in 6 tries

    answer = input("Do you want to play again? (print yes or no)") # Asks the user if they want to play again 
    if answer == "yes":
        playgame() # If the user wants to play again it will print the game code again 
    if answer == "no":
        print ("Thank you for playing. :)")   # If the user does not want to play again it will end the game and display a thank you message








        




