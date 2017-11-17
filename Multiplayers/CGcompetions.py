import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    distp = 10000000000
    distd = 10000000000
    gp_x= gd_x = gd_y = d_x = d_y = 0
    gp_y=0
    
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    
    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        
        unit_id = int(unit_id)
        unit_type = int(unit_type)
        player = int(player)
        mass = float(mass)
        radius = int(radius)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        extra = int(extra)
        extra_2 = int(extra_2)
        if unit_id==0 and unit_type==0:
            p_x = x
            p_y = y
        if unit_id==0 and unit_type==1:
            d_x = x
            d_y = y
        if unit_type==4 and (x-p_x)**2 + (y-p_y)**2<distp:
            gp_x = x    
            gp_y = y
            distp = (gp_x-p_x)**2 + (gp_y-p_y)**2
        if unit_type==3 and (gd_x-d_x)**2 + (gd_y-d_y)**2<distd:
            gd_x = x    
            gd_y = y
            distd = (gd_x-d_x)**2 + (gd_y-d_y)**2
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if distp>1000000000:
        print(gd_x, gd_y, 300)
    else:
        print(gp_x, gp_y, 300)
    print(gd_x, gd_y, 300)
    print("WAIT")
