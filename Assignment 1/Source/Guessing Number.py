#program to guess the number .
# firstly we have to import some libraries
import random
Random=random.randrange(1,11)
#then enter the value
a= input("Enter the user Guessing number in the range between 1 to 11:")
Number= int(a)
#  the coondition is to we guess a number
if(Number>Random):
#now we need to print
    print("Your Entered  Guessing Number is higher than Required")
#now we have to use else if what we use in python was elif as the condition
elif Number<Random:

    print("Your Entered Guessing Number is lower than required")

else:
# print the given condition
    print("Your answer is PERFECT GUESS!! Congratulations!!")