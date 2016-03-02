import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

matrix = [[0]*(l)*len(t) for i in range(h)]
for i in range(h):
    row = input()
    for j in range(len(t)):
        if t[j].islower():
            pos_char=ord(t[j])-97
        else:
            pos_char=ord(t[j])-65
        pos_row = (l)*pos_char
        for k in range(l):
            matrix[i][l*j+k]=row[pos_row+k]

for i in range(h):
    for k in range((l)*len(t)):
        print(matrix[i][k],end="" )
    print("")
