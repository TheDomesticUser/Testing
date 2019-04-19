## Elyas - Tuesday November, 14th 2017 ## 


# Question 3

"""

3)	Write a program to calculate the sum and average of a set of numbers. If you input 0, the program closes.

"""

print("Input some integers to calculate their sum and average. Input 0 to exit.") # Prints the instructions 

total = 0
amount = 0 
while 1==1:
    num = int(input("")) # Requests any amount of input from the user -- The use can input a series of numbers
    total = total + num # Determines the total by adding all the numbers inputted by the user
    amount += 1 # It figures out the amount of numbers inputted by the user
    if num == 0: 
        print("Average and Sum of the above numbers are: ", float(total/(amount-1)), float(total))
        # The print function takes the total number and divides it by the amount of numbers the user inputted and it also prints the total of the numbers


# It asks the user to input numbers and then using those numbers it will determine the average and the sum
# After all the numbers have been given, the user must input a '0' to end the code and get the result







