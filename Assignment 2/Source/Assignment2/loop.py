#write a python program for the given letter A because my name start with A = Avinash
#here my name stored in the name variable
name = input("Enter your Name:")
#now i applied for loop where the word has been divded and printed splitted.

for item in name.split():
#now i porinted the first letter of the word
   print (item[0].upper())
#now we use the two for loops as a nested loop one covers row and another one covers the column
#for row it will take seven rows
for row in range(7):
    #for column it take five columns
    for col in range(5):
        #now we applied the if condition column and row using and and or operator
        #this if condition will cover the column part.
        if((col==0 or col==4) and row!=0) or ((row==0 or row ==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print (end=" ")
            # this print will takes to the next line of the row
    print()