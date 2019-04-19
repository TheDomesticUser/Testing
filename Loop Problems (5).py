## Elyas - Tuesday November, 14th 2017 ## 


# Question 5

"""

5)	Write a program that finds all the prime numbers from 2 to 100 using nested loops. (Hint: use counters; define prime numbers)

"""

for num in range(2,101): # whatever the range is set to, it will use that range when pritning the prime numbers 
    prime = True
    for counter in range(2,num): # It shows all the numbers from the range or 2-100 in this case
        if (num%counter==0): # if statement
            prime = False #variable becomes false after if statement when there are no remainders
    if prime:
       print (num, 'is a prime number') # Prints the answer + "is a prime number"

       
# This code is based on the range provided. Any range set (in this case 2-100)
                 # It will print any number that is prime that is between 1-101
# A prime number is a number that can only be divided by 1 and itself but yet remain a whole number

# It works by checking if the number in the range can be divisible by certain numbers, if the remainder is 0 then it will not print that number within the range
                                                                     # Prime numbers cannot be divided by any number and remain a whole number







    
    




    
