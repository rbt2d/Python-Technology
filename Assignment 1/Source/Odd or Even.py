#program for odd or even
num = int(input("Enter  number: "))
#the condition is, if the remainder is 0 when divided by 2 then its even nor its odd
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))