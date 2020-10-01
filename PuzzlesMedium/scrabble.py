import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def compute_point(word):
    points=0
    for i in word:
        if i=='d' or i=='g':
            points+=2
        elif i=='b' or i=='c' or i=='m'or i=='p':
            points+=3
        elif i=='f' or i=='h' or i=='v'or i=='w' or i=='y':
            points+=4
        elif i=='k':
            points+=5
        elif i=='j' or i=='x':
            points+=8
        elif i=='q' or i=='z':
            points+=10
        else:
            points+=1
    return points

n = int(input())
dictionary=list()
for i in range(n):
    dictionary.append(input())
letters = input()
print(letters, file=sys.stderr)
list_letters=[]
for i in letters:
    list_letters.append(i)
result=""
max_point=0
for word in dictionary:
    print("word ",word, file=sys.stderr)
    letters_save = list(list_letters)
    word_in=True
    
    for i in word:
        
        if i not in letters_save:
            word_in=False
            break
        else:
            letters_save.remove(i)
    if word_in==True:
        print(compute_point(word), file=sys.stderr)            
    if word_in==True and compute_point(word)>max_point:
        print(compute_point(word), file=sys.stderr)
        result=word
        max_point=compute_point(word)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
