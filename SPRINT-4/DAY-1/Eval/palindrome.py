import math
def is_palindrome(n):
   temp=n
   ans=0

   while(n>0):
    reaminder=n%10
    n=math.floor(n/10)
    ans=remainder+ans*10

   if(temp==ans):
    print("palindrome")
   else:
    print("Not a palindrome")


   
is_palindrome(121)                     