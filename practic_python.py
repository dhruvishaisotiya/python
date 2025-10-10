a=10
b=20
global b
b=9
def change():
# this is globle variable
    global b
    a=45
    b=56
change()
print(a,b)
