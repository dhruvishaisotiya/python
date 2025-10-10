a=10
# b=20
global b
b=9
def change():

    global b
    a=45
    b=56
    b=9
change()
print(a,b)