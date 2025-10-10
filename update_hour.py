# update hour 
# ---------- code 1 ------------
u=12
day="pm"
h=3
for i in range(1,h+1):
    if u==12:
        if day=="pm":
            day="am"
            u=1
        else:
            day="pm"
            u=1
    else:
       u+=1
print("After update hour = ",u)        

# -------- code 2 ----------
# u=9
# day="am"
# h=3
# for i in range(1,h+1):
#     u=u+1
#     if u>12:
#         u=1
#     elif u==12:
#         if day=="am":
#             day="pm"
#         else:
#             day="am"
# if day=="am":
#     print(f"new time = {u}am")
# else:
#     print(f"new time = {u}pm")

