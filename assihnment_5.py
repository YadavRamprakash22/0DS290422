class sample:
    def power(self,x,n):
        if (x==0 or x==1 or n==1):
            return x
        if(x==-1):
            if(n%2==0):
                return 1
            else:
                return -1
        if(n==0):
            return 1
        if(n<0):
            return (1/x**(-n))
        if(n>0):
            return x**n
x=int(input("Enter a Number:"))
n=int(input("Enter A Power:"))
sam=sample()
print(sam.power(x,n))
