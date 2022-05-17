str=input()
str=result=str.title()
result=""
for word in str.split():
    result += word[:-1] + word[-1].upper() + " "
    print(result[:-1])
