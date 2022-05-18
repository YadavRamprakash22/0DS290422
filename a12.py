str=input("Enter a String:")
for i in str:
    if(i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' ):
        flag=True
    else:
        flag=False
if flag:
    print("string is not accepted")
else:
    print("string is accepted")
