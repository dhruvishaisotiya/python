# find given number in first turm ,middle turm and last turm
num=int(input("Enter number:"))
count=0
n=num
while num>0:
    num=num//10
    count+=1
last=n%10
middle=n%10**(count-1)//10
first=n//10**(count-1)
print(f"first turm={first}  middle turm={middle} last turm={last}")
print(last)
print(middle)
print(first)
print(count)