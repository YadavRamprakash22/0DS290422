s=input('ENter a String:')
def upplow(s):
    upp=0
    low=0
    for i in s.split(' '):
        for j in i:
            if j.isupper():
                upp+=1
            else:
                low+=1
    print('no. of uppercase:',upp)
    print('no. of lowercase:',low)
upplow(s)
