#python program for the numbers between the range and has to satisfy the given condition
#numbers stored in this array format
numbers=[]
# the below staement is for the for the For loop for the given range 1500 and 2700

for x in range(1500, 2700):

# now we have to use the if statement where we have given the two statements divisible by 7 and multiple by 5 for this the condition will be the reminder should be equal to zero both cndition has to be satisfied so we use and function
    if ((x%7==0) & (x%5==0)):
# the first value will be 1500 and inorder to select the next value to be added we have to use the append
        numbers.append(str(x))
#In order to print all the remaining numbers after satisfying the condition will be joined by using the join statrement.
print("The Number that are divisible by 7(seven) and multiple of 5 (five) between the range 1500 and 2700:")
print (','.join(numbers))