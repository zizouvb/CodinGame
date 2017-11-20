import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# to do : 
"""
1 - Slow down on wreck
2 - move doof
3 - add grenade when rage

"""
class Player():
    def __init__(self,player_id,reaper, destroyer,doof):
        self.id = player_id
        self.reaper = reaper
        self.destroyer = destroyer
        self.doof = doof



class Unity():
    def __init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2):
        self.unid_id = unit_id
        self.unit_type = unit_type
        self.player = player
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.radius = radius
        self.extra = extra
        self.extra_2 = extra

    def squared_distance(self, unity):
        if unity:
            return (self.x-unity.x)**2+(self.y-unity.y)**2 
        else:
            return 100000000


class Tanker(Unity):
    def __init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2):
        Unity.__init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
    


class Reaper(Unity):
    def __init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2):
        Unity.__init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        self.wreck = None 
        print("reaper instanciation", file=sys.stderr)

    def move(self):
        print(reaper.wreck.x-2*reaper.vx, reaper.wreck.y-2*reaper.vy, 300)


class Doof(Unity):
    def __init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2):
        Unity.__init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)

class Destroyer(Unity):
    def __init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2):
        Unity.__init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        self.tanker = None
        print("destroyer instanciation", file=sys.stderr)

class Wreck(Unity):
    def __init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2):
        Unity.__init__(self,unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)


# game loop
while True:
    
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    list_wrecks = []
    list_tankers = []
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
        if player==0 and unit_type==0:
            reaper = Reaper(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        if player==0 and unit_type==1:
            destroyer = Destroyer(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        if player==0 and unit_type==2:
            doof = Doof(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        if unit_type==4: 
            list_wrecks.append(Wreck(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2))
            
        if unit_type==3:
            list_tankers.append(Tanker(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2))
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    for wreck in list_wrecks:
        if reaper.squared_distance(wreck)<reaper.squared_distance(reaper.wreck):
                reaper.wreck = wreck 

    
    for tanker in list_tankers:
        if destroyer.squared_distance(tanker)<destroyer.squared_distance(destroyer.tanker):
                destroyer.tanker = tanker



    if not reaper.wreck:
        print(destroyer.tanker.x,destroyer.tanker.y, 300)
    else:
        reaper.move()
        
    if not destroyer.tanker:
        print(0,0, 300)
    else:
        print(destroyer.tanker.x,destroyer.tanker.y, 300)
    print("WAIT")
