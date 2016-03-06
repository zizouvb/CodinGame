import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def false_distance(lat_a, lon_a, lat_b, lon_b):
    x = (lon_b-lon_a) * math.cos((lat_a+lat_b)/2)
    y = lat_b-lat_a
    return pow(x,2)+pow(y,2)
    
def convert_comma(pos_tab):
    pos_tab=pos_tab.split(',')
    return float(str(pos_tab[0])+'.' +str(pos_tab[1]))
    
lon = convert_comma(input())
lat = convert_comma(input())
 
n = int(input())

min_dist=float('inf')
for i in range(n):
    defib=input().split(';')
    lon_def = convert_comma(defib[4])
    lat_def = convert_comma(defib[5])
    current_distance = false_distance(lat,lon, lat_def, lon_def)
    if current_distance<min_dist:
        min_dist=current_distance
        name_def =defib[1]
print(name_def)
    
