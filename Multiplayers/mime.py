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
    dictionary[ext]=mt
print(dictionary,file=sys.stderr)
for i in range(q):
    fname = input()  # One file name per line.
    print(fname, file=sys.stderr)
    #print("ext  :", re.search('(?<=\.)\w+',fname), file=sys.stderr)
    exp=re.search('(?<=\.)\w+',fname)
    #print("exp.group(O) : ", exp.group(0), file=sys.stderr)
    if exp is None:
        print("UNKNOWN",file=sys.stderr)
    else:
        mime=dictionary.get(exp.group(0))
        if mime is None:
            print("UNKNOWN", file=sys.stderr)
        else:
            print(mime, file=sys.stderr)
        #print(dictionary.get(re.search('(?<=\.)\w+',fname,re.IGNORECASE).group(0)))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

