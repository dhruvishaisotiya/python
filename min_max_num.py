#find minimum and maximum value
max1=0
min1=100
c=0
while True:
    n=input("Enter number:")
    if n=='Q'or n=='q':
        break
    else:
        n=int(n)
        if n>max1:
            max1=n
        if n<min1:
            min1=n
print("minimum value= ",min1)                
print("maximum value= ",max1)                


