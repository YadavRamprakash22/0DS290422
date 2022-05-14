num=int(input("Enter a Number:"))
Even=0
Odd=0
for i in range(1,num):
    if(i%2==0):
        Even+=1
    else:
        Odd+=1
print("Number of Even Numbers:",Even)
print()
print("Number of Odd Numbers:",Odd)