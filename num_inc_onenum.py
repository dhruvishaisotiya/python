n=1267
m=1
ans=0

while n>0:
    d=n%10
    if d==9:
        d=0
    else:
        d=d+1
    ans=ans+d*m
    m=m*10
    n=n//10
print(ans)