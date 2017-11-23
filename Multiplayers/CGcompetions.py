import sys
import math
import random
import time
import copy
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# to do : 
"""

2 - move doof
3 - add grenade when rage
4 - add oil
5 - add tar
https://github.com/git-knight/mad-starter/blob/master/main.cpp
https://github.com/dreignier/fantastic-bits/blob/master/fantastic-bits.cpp
https://github.com/CodinGame/MeanMax/blob/master/Referee.java
check https://tech.io/playgrounds/1003/flocking-autonomous-agents/steering-strategy
check if( u->type == Tanker && ( u->x * u->x + u->y * u->y > 6000 * 60000 )  --- u->extra < u->extra2
"""
DEPTH = 3
ANGLES_LIST = [0,45,90,135,180,225,270,315]
THRUSTS_LIST = [0,100,300]

SPAWN_WRECK = False;
LOOTER_COUNT = 3;
MAP_RADIUS = 6000.0;

TANKERS_BY_PLAYER_MIN = 1;
TANKERS_BY_PLAYER_MAX = 3;

WATERTOWN_RADIUS = 3000.0;

TANKER_THRUST = 500;
TANKER_EMPTY_MASS = 2.5;
TANKER_MASS_BY_WATER = 0.5;
TANKER_FRICTION = 0.40;
TANKER_RADIUS_BASE = 400.0;
TANKER_RADIUS_BY_SIZE = 50.0;
TANKER_EMPTY_WATER = 1;
TANKER_MIN_SIZE = 4;
TANKER_MAX_SIZE = 10;
TANKER_MIN_RADIUS = TANKER_RADIUS_BASE + TANKER_RADIUS_BY_SIZE * TANKER_MIN_SIZE;
TANKER_MAX_RADIUS = TANKER_RADIUS_BASE + TANKER_RADIUS_BY_SIZE * TANKER_MAX_SIZE;
TANKER_SPAWN_RADIUS = 8000.0;
TANKER_START_THRUST = 2000;

MAX_THRUST = 300;
MAX_RAGE = 300;
WIN_SCORE = 50;

REAPER_MASS = 0.5;
REAPER_FRICTION = 0.20;
REAPER_SKILL_DURATION = 3;
REAPER_SKILL_COST = 30;
REAPER_SKILL_ORDER = 0;
REAPER_SKILL_RANGE = 2000.0;
REAPER_SKILL_RADIUS = 1000.0;
REAPER_SKILL_MASS_BONUS = 10.0;

DESTROYER_MASS = 1.5;
DESTROYER_FRICTION = 0.30;
DESTROYER_SKILL_DURATION = 1;
DESTROYER_SKILL_COST = 60;
DESTROYER_SKILL_ORDER = 2;
DESTROYER_SKILL_RANGE = 2000.0;
DESTROYER_SKILL_RADIUS = 1000.0;
DESTROYER_NITRO_GRENADE_POWER = 1000;

DOOF_MASS = 1.0;
DOOF_FRICTION = 0.25;
DOOF_RAGE_COEF = 1.0 / 100.0;
DOOF_SKILL_DURATION = 3;
DOOF_SKILL_COST = 30;
DOOF_SKILL_ORDER = 1;
DOOF_SKILL_RANGE = 2000.0;
DOOF_SKILL_RADIUS = 1000.0;

LOOTER_RADIUS = 400.0;
LOOTER_REAPER = 0;
LOOTER_DESTROYER = 1;
LOOTER_DOOF = 2;

TYPE_TANKER = 3;
TYPE_WRECK = 4;
TYPE_REAPER_SKILL_EFFECT = 5;
TYPE_DOOF_SKILL_EFFECT = 6;
TYPE_DESTROYER_SKILL_EFFECT = 7;

EPSILON = 0.00001;
MIN_IMPULSE = 30.0;
IMPULSE_COEFF = 0.5;

GLOBAL_ID = 0;



class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def squaredDistance(self, point):
        return (self.x-point.x)**2+(self.y-point.y)**2 

    def distance(self, point):
        return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2) 
        
    def isInRange(self, point, range):
        return point != self and squared_distance(point)<range**2

WATERTOWN = Point(0, 0);

class Wreck(Point):
    def __init__(self,unit_id,x, y, extra, radius):
        Point.__init__(self,x, y)
        self.water = extra
        self.radius = radius
        self.unit_id = unit_id

    def harvest(self,players, skills_effects):
            for player in players:
                if self.isInRange(player.reaper, self.radius): # and not player.reaper.isInDoofSkill(skills_effects)):
                    player.score += 1
                    water -= 1
                
            return water > 0;


class Unity(Point):
    def __init__(self,unit_id,unit_type, x, y):
        Point.__init__(self,x, y)
        self.unit_type = unit_type
        self.known = False
        self.unit_id = unit_id
        vx = 0
        vy = 0

    def move(self, dt):
        self.x = self.x + dt*vx
        self.y = self.y + dt*vy

    def squaredSpeed(self):
        return vx*vx + vy*vy

    def thrust(self, point, power):
        distance = self.distance(point)
        if (Math.abs(distance) <= EPSILON):
            return 0
        coef = ((power) / self.mass) / distance
        vx += (point.x - self.x) * coef
        vy += (point.y - self.y) * coef

    def isInDoofSkill(self, skills_effects):
        for s in skills_effects:
            if self.isInRange(s, s.radius + self.radius) and s is Doofskill:
                return True
        return False

    def adjust(self,skills_effects): 
            self.x = round(self.x)
            self.y = round(self.y)

            if self.isInDoofSkill(skills_effects):
            # No friction if we are in a doof skill effect
                self.vx = round(self.vx)
                self.vy = round(self.vy)
            else:
                self.vx = round(self.vx * (1.0 - self.friction))
                self.vy = round(self.vy * (1.0 - self.friction))
            

    def isCollidingBorder(self):        
        if self.distance(WATERTOWN)+self.radius < MAP_RADIUS:
            return True
        return False

    def squared_distance(self, unity):
        if unity:
            return (self.x-unity.x)**2+(self.y-unity.y)**2 
        else:
            return 100000000



class Tanker(Unity):
    def __init__(self,unit_id,unit_type, x, y, extra2, player):
        Unity.__init__(self,unit_id,TYPE_TANKER,0, 0)
        self.player=player
        self.capacity=extra2
        self.water = TANKER_EMPTY_WATER
        self.mass = TANKER_EMPTY_MASS + TANKER_MASS_BY_WATER * self.water
        self.friction = TANKER_FRICTION;
        self.radius = TANKER_RADIUS_BASE + TANKER_RADIUS_BY_SIZE * self.capacity;


    def die(self):
        # Don't spawn a wreck if our center is outside of the map
        if self.distance(WATERTOWN) >= MAP_RADIUS:
            return None
            

        return Wreck(round(self.x), round(self.y), self.water, self.radius)
        

    def isFull(self):
        return water >= size
        

    def play(self):
        if self.isFull(): 
        # Try to leave the map
            self.thrust(WATERTOWN, -TANKER_THRUST)
        elif self.distance(WATERTOWN) > WATERTOWN_RADIUS: 
        # Try to reach watertown
            self.thrust(WATERTOWN, TANKER_THRUST);
            

class Looter(Unity):
    def __init__(self,unit_id,unit_type, x, y, player):
        Unity.__init__(self,unit_id,unit_type, x, y)
        self.player = player
        self.radius = LOOTER_RADIUS

    def applySolution(self,angle, thrust):
        self.angle = angle
        self.thrust = thrust

class Reaper(Looter):
    def __init__(self,unit_id,unit_type, x, y,vx,vy, player):
        Looter.__init__(self,unit_id,LOOTER_REAPER, x, y, player)
        self.mass = REAPER_MASS
        self.friction = REAPER_FRICTION
        self.skill_cost = REAPER_SKILL_COST
        self.skill_range = REAPER_SKILL_RANGE
        self.wreck=None
        self.vx = vx
        self.vy = vy
    def moveOld(self):
        print(reaper.wreck.x-2*reaper.vx, reaper.wreck.y-2*reaper.vy, 300)

class Destroyer(Unity):
    def __init__(self,unit_id,unit_type, x, y, player):
        Looter.__init__(self,unit_id,LOOTER_DESTROYER, x, y, player)
        self.mass = DESTROYER_MASS
        self.friction = DESTROYER_FRICTION
        self.skill_cost = DESTROYER_SKILL_COST
        self.skill_range = DESTROYER_SKILL_RANGE
        self.tanker = None
class Doof(Unity):
    def __init__(self,unit_id,unit_type, x, y, player):
        Looter.__init__(self,unit_id,LOOTER_DOOF, x, y, player)
        self.mass = DOOF_MASS
        self.friction = DOOF_FRICTION
        self.skill_cost = DOOF_SKILL_COST
        self.skill_range = DOOF_SKILL_RANGE

class Solution():
    def __init__(self):
        self.score = -1
        self.angles = [0]*DEPTH*LOOTER_COUNT
        self.thrusts = [0]*DEPTH*LOOTER_COUNT
        for i in range(DEPTH*LOOTER_COUNT):
            self.randomize(i)

    def mutate(self):
        return copy.deepcopy(self)

    def randomize(self,depth_idx):
        self.angles[depth_idx] = random.choice(ANGLES_LIST)
        self.thrusts[depth_idx] = random.choice(THRUSTS_LIST)
       
    
    def silverSol(self):
        for wreck in list_wrecks:
            if players[0].looters[LOOTER_REAPER].squared_distance(wreck)<players[0].looters[LOOTER_REAPER].squared_distance(players[0].looters[LOOTER_REAPER].wreck):
                players[0].looters[LOOTER_REAPER].wreck = wreck 
        reaper = players[0].looters[LOOTER_REAPER] 
        destroyer = players[0].looters[LOOTER_DESTROYER] 
        for tanker in list_tankers:
            if destroyer.squared_distance(tanker)<destroyer.squared_distance(destroyer.tanker):
                destroyer.tanker = tanker

class Player():
    def __init__(self,player_id):
        self.id = player_id
        self.looters = [0]*LOOTER_COUNT
        self.score = -1

    def save(self):# to complete
        return
    def load(self):# to complete
        return
    def move(self,solution,looter_idx, turn):
        self.looters[looter_idx].applySolution(solution.angles[3*looter_idx+turn],solution.thrusts[3*looter_idx+turn])

    def getLootScore(self,solution,looter_idx):
        turn = 0
        while(turn<DEPTH):
            self.move(solution,looter_idx, turn)
            #play() 
            #self.score += evaluate()

    def getScore(self,solution):
        for i in range(LOOTER_COUNT):
            self.getLootScore(solution,i)
            
    def solve(self,time_to_stop,list_tankers,list_wrecks):

        solution = Solution()
        self.list_wrecks = list_wrecks
        self.list_tankers = list_tankers
        self.save()
        self.getScore(solution)
        child = Solution()
        while(time.time()>time_to_stop):
            child = solution.mutate()
            if self.getScore(solution)<self.getScore(child):
                solution = child


players = [Player(0),Player(1),Player(2)]


# game loop
while True:
    for i in range(3):
        players[i].score = int(input())
    for i in range(3):
        players[i].rage = int(input())

    unit_count = int(input())
    list_tankers = []
    list_wrecks = []

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
        if unit_type==LOOTER_REAPER:
            players[player].looters[LOOTER_REAPER] = Reaper(unit_id, unit_type,x,y,vx,vy,player) 
        if unit_type==LOOTER_DESTROYER:
            players[player].looters[LOOTER_DESTROYER] = Destroyer(unit_id, unit_type,x,y,player)
        if unit_type==LOOTER_DOOF:
            players[player].looters[LOOTER_DOOF] = Doof(unit_id, unit_type,x,y,player)
        if unit_type==4: 
            list_wrecks.append(Wreck(unit_id,x, y, extra, radius))
        if unit_type==3:
            list_tankers.append(Tanker(unit_id,unit_type, x, y, extra_2, player))
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    time_limit = 40
    players[0].solve(time_limit,list_wrecks,list_tankers)



    if not reaper.wreck:
        print(destroyer.tanker.x,destroyer.tanker.y, 300)
    else:
        reaper.move()
        
    if not destroyer.tanker:
        print(0,0, 300)
    else:
        print(destroyer.tanker.x,destroyer.tanker.y, 300)
    if not destroyer.tanker:
        print(0,0, 300)
    else:
        print(destroyer.tanker.x,destroyer.tanker.y, 300)
