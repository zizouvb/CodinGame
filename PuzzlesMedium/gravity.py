    
width, height = [int(i) for i in input().split()]
tab  = [['0' for i in range(width)] for j in range(height)]
for i in range(height):
    a=list(input())
    for j in range(width):
        tab[i][j]=a[j]

k=1
while k==1:
    k=0
    for y in range(height-1):
        for x in range(width):
            if tab[y][x]=='#':
                if tab[y+1][x]=='.':
                    k=1
                    tab[y+1][x]='#'
                    tab[y][x]='.'


for y in range(height):
    for x in range(width):
        print(tab[y][x],end="")
        
    print("")        
                    
