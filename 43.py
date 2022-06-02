size=int(input("enter the size of the list:"))
lst=[]
for i in range(size):
    data=int(input("enter data in the list:"))
    lst.append(data)
print(lst)
def cube(lst):
    return lst**2
print(list(map(cube,lst)))
