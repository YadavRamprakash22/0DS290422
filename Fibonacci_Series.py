num1=0
num2=1
num3=int(input("Enter a number:"))
print(num1,num2,end=" ")
while(num3-2):
    fib=num1+num2
    num1=num2
    num2=fib
    print(fib,end=" ")
    num3=num3-1
