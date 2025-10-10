# find first 2 maximum and last 2 minimum number also include odd and even number
min1=100
max1=0
min2=0
max2=0
mino1=100
maxo1=0
mino2=0
maxo2=0
while True:
    n=input("Enter your string:")
    if(n=='Q' or n=="q"):
        break
    else:
        n=int(n)
        if(n%2==0):
            if(n>max1):
                max2=max1
                max1=n
            elif n>max2 and n!=max1:
                max2=n
            if(n<min1):
                min2=min1
                min1=n
            elif(n<min2) and n!=min1:
                min2=n
        else:
            if(n>maxo1):
                maxo2=maxo1
                maxo1=n
            elif n>maxo2 and n!=maxo1:
                maxo2=n
            if(n<mino1):
                mino2=mino1
                mino1=n
            elif(n<mino2) and n!=mino1:
                mino2=n
        

print("min1= ",min1)
print("max1 =",max1) 
print("min2= ",min2)
print("max2= ",max2)  
print("min1= ",mino1)
print("max1 =",maxo1) 
print("min2= ",mino2)
print("max2= ",maxo2)                            