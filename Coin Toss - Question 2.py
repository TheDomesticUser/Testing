# Elyas 12/7/17 Question 2



'''

Coin Toss Game: Write a program that flips heads or tails (hint: make certain random number(s) head(s), and others tails).
Have a counter that gives the user 1 point for heads, but subtracts 1 point for tails.  Counters can be negative!
Have a user input of some sort, and create a list that shows the history of the flips.

'''

import random

name = str(input("Greetings user, what is your name?"))
the_name = name.upper()
print ("Hello,",the_name,"and Welcome to the Coin Toss Game!")
print ("Type playgame() to start.")

def playgame():
    History_List = []
    score = 0
    print("Your goal is score a total of 3 points.")
    print("Once the coin is tossed - if you land heads you gain one point and if you land tails you lose one point.")
    print("Type toss to toss the coin and type end to stop the coin toss game (toss/end)")

    while True:
        flip = random.randint(0,1) # Selecs a random value "1" being Tails and "0" being Heads - The user received a point for tails
        
        answer = input("What do you want to do?") # Asks the user what they'd like to input
        while answer == "toss":
            if flip == 0: # If the user decides to toss and the flip is equal to the randit "0" which is Heads in this case then it will tell them that they flipped Heads
                print ("You flipped Heads")                                                                                # - and add 1 point to their score                            
                History_List.append("Heads")
                score = score + 1
                break
            if flip == 1: # If the user decides to toss and the flip is equal to the randit "1" which is Tails in this case then it will tell them that they flipped Tails
                print ("You flipped Tails")                                                                                 # - and deduct 1 point from their score
                History_List.append("Tails")
                score = score - 1
                break
    
        print(str(History_List)) # Prints the previous results - Tells the user what they flipped if they decide to play many times
        print("Your current score is ", score) # Prints the total score that the user obtained throughout the game
        if int(score) == 3: # When a total of 3 points is reached it will end the game and tell the user that they've won
                print ("Well Done!, You're a WINNER!")
                break 
        
        if answer == "end": # If the user decides to end and they have not accumulated 3 points then it will tell them that they've lost
            print ("You've lost. Good Effort! Try again next time.")
            break

        


  
        
