# money counting 
day=int(input("Enter day : "))
w=day//7
d=day%7
sum=0
temp1=1 
for i in range(w):
    temp2=temp1 # temp1 is use for weeks count
    for j in range(7):
        sum=sum+temp2
        temp2+=1  # temp2 is use day count
    temp1+=1 
for i in range(d):
    sum=sum+temp1
    temp1+=1  # temp1 is use increase count
print(f"Total money gathered =${sum}")
