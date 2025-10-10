n=19
num=n
while n!=4 and n!=1:
    ans=0
    while n>0:
        d=n%10
        ans=ans+d**2
        n=n//10
    n=ans
if(n==1):     # ans==1
        print(num," is Happy number")
else:
        print(num," is not Happy number")        
       
    
