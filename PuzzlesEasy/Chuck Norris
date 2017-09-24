import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
bit_message=""
for char in message:
    #bit_message = bit_message + bin(ord(char))[2:]
    bit_message = bit_message + ('{0:07b}'.format(ord(char)))
print(bit_message, file=sys.stderr)

count=0
for bit in range(len(bit_message)):
    if count==0:
        temp=bit_message[bit]
        count=count+1

    if bit==len(bit_message)-1:
        if temp=='1':
            print("0 ", end="")
        else:
            print("00 ", end="")
        for i in range(count):
            print("0", end="")
        break
    elif bit_message[bit+1]==temp:
        count=count+1
       
    else:
        if temp=='1':
            print("0 ", end="")
        else:
            print("00 ", end="")
        for i in range(count):
            print("0", end="")
        print(" ", end="")
        count=0
