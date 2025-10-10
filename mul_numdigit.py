n=1234567
def mul_numdegit(n):
    ans=1
    while n>0:
        d=n%10
        ans=ans*d
        n=n//10
    return ans
c=mul_numdegit(n)
print(c)