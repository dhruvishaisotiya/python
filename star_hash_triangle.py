n=5
for i in range(1,n+1):
    if(i%2==0):
        print("# "*i)
    else:
        print("* "*i)

for i in range(1,n+1):
    if(i%2==0):
        print(" "*(n-i)+"# "*i)
    else:
        print(" "*(n-i)+("* "*i))       
