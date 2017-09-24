import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
dictionary = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    print(ext, file=sys.stderr)
    print(mt, file=sys.stderr)
    print(" ", file=sys.stderr)
    dictionary[ext.lower()]=mt
print(dictionary,file=sys.stderr)
for i in range(q):
    fname = input().lower()  # One file name per line.
    print("input : ",fname, file=sys.stderr)
    if len(fname.split('.'))==1:
        exp=None
    else:
        exp=fname.split('.')[-1]
    if exp is None:
        print("UNKNOWN")
    else:
        mime=dictionary.get(exp)
        print("mime : ",mime, file=sys.stderr)
        if mime is None:
            print("UNKNOWN")
        else:
            print(mime)
