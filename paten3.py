n=5
# for i in range(1,n+1):
#     for k in range(n-i,0,-1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


for i in range(1,n+1):
    print(((n-i)*"  ")+("* "*i))

# print("*")
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
# print(i)
#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 

# print(j)
#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 