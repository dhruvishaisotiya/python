# calculate odd and even number sum, count and avg 
c=0
s=0
co=0
so=0
while True:
    n=input("Enter number:")
    if n=="Q" or n=="q":
        break
    else:
        n=int(n)
        if n%2==0:
            s+=n
            c+=1
        else:
            so+=n
            co+=1
print(f"sum of even is {s} and count is{c} and avg is {s//c}")# 6
print(f"sum of odd is {so} and count is{co} and avg is {so/co}")# 5.0