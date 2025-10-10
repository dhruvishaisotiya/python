# find Disarium 
# 89,135,175,518,598
n=598 
num=n
count=0
ans=0
while n>0:
    count+=1
    n=n//10
while num>0:
    d=num%10
    ans=ans+d**(count)
    count-=1
    num=num//10
print("ans =" ,ans)