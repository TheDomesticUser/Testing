## Elyas - Tuesday November, 14th 2017 ## 


# Question 2

"""

2)	Write a program to create a multiplication table for a given user input. The table should include its multiples from 1 to 10

	Input a number: 7                                                       
	7 x 1 = 7                                                               
	7 x 2 = 14                                                              
	7 x 3 = 21                                                              

"""
userInput = int(input("Enter a number:")) # Asks the user to input a number
for counter in range (1, 11): # Multiplies that number by the range or from 1-10
    print (userInput, 'x', counter, '=', userInput*counter) # Prints the results 

    
# This code takes in an input from the user then multiplies it by the given range which means it'll print the number multiplied by 1-10
                                                                                              #(1-10 is the range but it can be changed)





