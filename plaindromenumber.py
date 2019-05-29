'''n=int(input('enter the number'))
temp=n
rev=0

while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp==rev:
    print("number is plaindrome ")
else:
     print("number is not plaindrome ")'''
    
num=int(input('enter the number'))
temp=num
rev=0

while temp!=0:
    rev=(rev*10)+(temp%10)
    temp=temp//10
    
if num==rev:
    print("number is plaindrome ")
else:
     print("number is not plaindrome ")
    

