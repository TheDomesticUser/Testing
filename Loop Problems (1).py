## Elyas - Tuesday November, 14th 2017 ## 


# Question 1

"""

1)	Write a program to create the following pattern:

	1
	22
	333
	4444
	
"""
userInput = int(input("Enter a number:")) # Asks the user to input a number
for counter in range(1,userInput+1): # it sets the range -- How much to go by -- As an example if the user puts a 9 above then the code will go up to 9
    print (str(counter)*counter) # Prints the code or the pattern -- The pattern is based on the number inputted (Refer to explanation below)

    
# This code prints the amount of numbers corresponding to the number itself but from 1-x (x being the number inputted by the user)
# If the number is 8 then it will print '8' once, twice, three times, four times, and the amount of '8' corresponding to the given input








