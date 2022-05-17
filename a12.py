import string
str=input("Enter a String:")
invalidcharacters= set(string.punctuation)
if any(char in invalidcharacters for char in str):
    print ("invalid")
else:
    print("valid")
