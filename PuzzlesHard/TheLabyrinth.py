import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def getNeighbors(graph, x,y):
    if graph[x][y] == '?':
        return []
    else:
        neighbors = []
        
        if graph[x][y-1] != '#':
            neighbors.append((x,y-1))
        if graph[x][y+1] != '#':
            neighbors.append((x,y+1))
        if graph[x-1][y] != '#':
            neighbors.append((x-1,y))
        if graph[x+1][y] != '#':
            neighbors.append((x+1,y))
        
        return neighbors
    


# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

grid = [[0 for j in range(r)] for i in range(c)] 

control_room_reached = False

control_room_found = False
turn = 0
# game loop
while True:
    # ky: row where Kirk is located.
    # kx: column where Kirk is located.
    ky, kx = [int(i) for i in input().split()]
    print(kx, ky, control_room_reached,control_room_found, file = sys.stderr)
    for y in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        
        for x in range(len(row)):
            grid[x][y]=row[x]
            if row[x]=='C' and x == kx and y==ky: 
                control_room_reached=True
                grid[xt][yt]='T'
            if row[x]=='T' and not control_room_reached:
                grid[x][y]='.'
                xt=x
                yt=y
            if x == kx and y==ky: 
                grid[x][y]='K'
            
        
    to_visit = [(kx,ky)]
    direction_to_control=''
    distance = 10000
    unknown_found = False
    control_room_found = False
    visited = []
  
    
    while to_visit and not unknown_found:
      
        x1,y1 = to_visit.pop(0)

        for x2, y2 in getNeighbors(grid, x1,y1):
       
            if (x2,y2) in visited:
                continue
            if control_room_found and not control_room_reached:
                break
            if control_room_reached and grid[x2][y2]=='?':
                continue
          
         
            if grid[x2][y2]=='.':
       
                if x1==kx and y1==ky:
                    if x2>x1:grid[x2][y2]='R'
                    elif x2<x1:grid[x2][y2]='L'
                    elif y2>y1:grid[x2][y2]='D'
                    elif y2<y1:grid[x2][y2]='U' 
                else:
                    if grid[x2][y2]=='.':
                        if x2>x1 :grid[x2][y2]=grid[x1][y1]+'R'
                        elif x2<x1:grid[x2][y2]=grid[x1][y1]+'L'
                        elif y2>y1:grid[x2][y2]=grid[x1][y1]+'D'
                        elif y2<y1:grid[x2][y2]=grid[x1][y1]+'U'
                    elif len(grid[x2][y2])>=len(grid[x1][y1])+1:            
                        if x2>x1 :grid[x2][y2]=grid[x1][y1]+'R'
                        elif x2<x1:grid[x2][y2]=grid[x1][y1]+'L'
                        elif y2>y1:grid[x2][y2]=grid[x1][y1]+'D'
                        elif y2<y1:grid[x2][y2]=grid[x1][y1]+'U'
                
               
                to_visit.append((x2,y2))
            
            
            elif not unknown_found and not control_room_reached and not control_room_found and grid[x2][y2]=='?':
            
                
                if x2>x1:grid[x2][y2]=grid[x1][y1]+'R'
                elif x2<x1:grid[x2][y2]=grid[x1][y1]+'L'
                elif y2>y1:grid[x2][y2]=grid[x1][y1]+'D'
                elif y2<y1:grid[x2][y2]=grid[x1][y1]+'U'
    
            
                if len(grid[x2][y2])<distance:
                    direction_to_control = grid[x2][y2]
                    distance = len(grid[x2][y2])
                    unknown_found=True
                    break
            
            elif not control_room_reached and grid[x2][y2]=='C':
                print("c", file = sys.stderr)
                control_room_found = True
                if x1==kx and y1==ky:
                    if x2>x1:grid[x2][y2]='R'
                    elif x2<x1:grid[x2][y2]='L'
                    elif y2>y1:grid[x2][y2]='D'
                    elif y2<y1:grid[x2][y2]='U' 
                else:grid[x2][y2]=grid[x1][y1]
                if len(grid[x2][y2])<distance and len(grid[x2][y2])>1:
                    direction_to_control = grid[x2][y2]
                    distance = len(grid[x2][y2])
            
                else:
                    direction_to_control = grid[x2][y2]+'C'
            
                
                break
            elif control_room_reached and grid[x2][y2]=='T':
           
                if x1==kx and y1==ky:
                    if x2>x1:grid[x2][y2]='R'
                    elif x2<x1:grid[x2][y2]='L'
                    elif y2>y1:grid[x2][y2]='D'
                    elif y2<y1:grid[x2][y2]='U' 
                else:grid[x2][y2]=grid[x1][y1]
                if len(grid[x2][y2])<distance and len(grid[x2][y2])>1:
                    direction_to_control = grid[x2][y2]
                    distance = len(grid[x2][y2])
           
                else:
                    direction_to_control = grid[x2][y2]+'C'
           
                break
        visited.append((x1,y1))
    
    # Kirk's next move (UP DOWN LEFT or RIGHT).
    
    if direction_to_control[0]=='R':print("RIGHT")
    elif direction_to_control[0]=='L':print("LEFT")
    elif direction_to_control[0]=='U':print("UP")
    elif direction_to_control[0]=='D':print("DOWN")
    
