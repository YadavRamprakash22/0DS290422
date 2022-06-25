# Enter your code here. Read input from STDIN. Print output to STDOUT
A= int(input())
SET_N = set(map(int, input().split()))

A= int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N & SET_B))
