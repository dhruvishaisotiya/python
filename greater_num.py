# three number in find greater number
num1=int(input("Enter number1 :"))
num2=int(input("Enter number2 :"))
num3=int(input("Enter number3 :"))

if(num1>num2 and num1>num3):
    print(f"number1  {num1} is greater")
elif(num2>num1 and num2>num3):
    print(f"num2   {num2} is greater")
else:
    print(f" number3 {num3} is greater")