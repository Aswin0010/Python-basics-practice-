n= int (input ("Enter the number n : "))
for i in range (0,n):
     for j in range (0, n-i):
         if (i==0 or i==n-1 or j==n-i-1 or j==0) :
             print ("*", end = " ")    
         else:
             print(" ",end=" ")
     print()       