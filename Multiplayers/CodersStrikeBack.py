import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

laps = int(input())
checkpoint_count = int(input())
check_tab = np.zeros((checkpoint_count,2))
next_check_tab = np.zeros((2,2))
speed_tab = np.zeros((2,2))
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    check_tab[i,0]=checkpoint_x
    check_tab[i,1]=checkpoint_y
# game loop
turn = 0
while True:
    for i in range(2):
        # x: x position of your pod
        # y: y position of your pod
        # vx: x speed of your pod
        # vy: y speed of your pod
        # angle: angle of your pod
        # next_check_point_id: next check point id of your pod
        x, y, vx, vy, angle, next_check_point_id = [int(j) for j in input().split()]
        next_check_tab[i,0]=check_tab[next_check_point_id,0]
        next_check_tab[i,1]=check_tab[next_check_point_id,1]
        speed_tab[i,0]=vx
        speed_tab[i,1]=vy
    for i in range(2):
        # x_2: x position of the opponent's pod
        # y_2: y position of the opponent's pod
        # vx_2: x speed of the opponent's pod
        # vy_2: y speed of the opponent's pod
        # angle_2: angle of the opponent's pod
        # next_check_point_id_2: next check point id of the opponent's pod
        x_2, y_2, vx_2, vy_2, angle_2, next_check_point_id_2 = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    if turn ==0:
        print(str(int(next_check_tab[0,0]-3*speed_tab[0,0])), str(int(next_check_tab[0,1]-3*speed_tab[0,1])), "BOOST")
        print(str(int(next_check_tab[1,0]-3*speed_tab[1,0])), str(int(next_check_tab[1,1]-3*speed_tab[1,1])), "BOOST")
    else:
        print(str(int(next_check_tab[0,0]-3*speed_tab[0,0])), str(int(next_check_tab[0,1]-3*speed_tab[0,1])), 100)
        print(str(int(next_check_tab[1,0]-3*speed_tab[1,0])), str(int(next_check_tab[1,1]-3*speed_tab[1,1])), 100)
    turn +=1
