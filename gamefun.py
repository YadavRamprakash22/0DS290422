lst=[]
n=int(input('enter the size of the list:'))
def slist(n):
    for i in range(n):
        data=int(input())
        lst.append(data)
slist(n)
print(lst)
def sumlist():
    sa=0
    for i in range(len(lst)):
        sa=sa+lst[i]
    print('sum of the element in the list:',sa)
sumlist()
