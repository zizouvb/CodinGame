import sys
import math
import random
import numpy
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
link_dic = {}
factory_owner_dic = {}
factory_nbcyb_dic = {}
factory_prod_dic = {}

for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    link_dic[(factory_1, factory_2)] = distance
    link_dic[(factory_2, factory_1)] = distance
    factory_owner_dic[factory_1] = 0
    factory_nbcyb_dic[factory_1] = 0
    factory_prod_dic[factory_1] = 0
    factory_owner_dic[factory_2] = 0
    factory_nbcyb_dic[factory_2] = 0
    factory_prod_dic[factory_2] = 0
    
turn = 0

# game loop
while True:
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        arg_1 = int(arg_1) # owner
        arg_2 = int(arg_2) # number of cyborgs in the factory
        arg_3 = int(arg_3) #factory production
        arg_4 = int(arg_4)
        arg_5 = int(arg_5)
        if entity_type=="FACTORY":
            factory_owner_dic[entity_id] = arg_1
            factory_nbcyb_dic[entity_id] = arg_2
            factory_prod_dic[entity_id] = arg_3
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    

    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
    turn += 1
    unplayed = True
    for entity_id in factory_owner_dic:
        dest_fact = 1
        count = 0
        while factory_owner_dic[dest_fact]==1 and count<50:
            dest_fact=random.randint(0,factory_count-1)
            count += 1
        if factory_owner_dic[entity_id]==1 and factory_nbcyb_dic[entity_id]>factory_nbcyb_dic[dest_fact] and unplayed:
            print("MOVE", entity_id, dest_fact,factory_nbcyb_dic[dest_fact]+1)
            unplayed = False
            break
    if unplayed:
        print("WAIT")
