# print reverce number ==  ans=ans*10+d
# addition for number == ans=ans+d
# cub for number == ans=ans+d**3
# Armstrong number ==  ans=ans+d**(count) =153,370,371,407,1634

n=int(input("Enter number:"))
num=n
ans=0
count=0
while n>0:
    n=n//10
    count+=1
n=num
while n>0:
    d=n%10
    ans=ans+d**(count)
    n=n//10

# Armstrong number
if ans==num:
    print(num,"given number is Armstrong number")
else:
    print(num,"given number is not Armstrong number")