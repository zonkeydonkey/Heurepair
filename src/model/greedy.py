import sys
import copy
import test.ten as map
# from ten import *

def metrics(map_custom, map_original):
    lenMap = len(map_custom['roads'])
    difference = 0
    if (len(map_custom['cities'])!=len(map_original['cities'])) or (len(map_custom['roads'])!=len(map_original['roads'])):
        print("Cant compare - different number of cities or roads")
    for i in range(lenMap):
        if map_custom['roads'][i]['city_a'] != map_original['roads'][i]['city_a'] or map_custom['roads'][i]['city_b'] != map_original['roads'][i]['city_b'] or map_custom['roads'][i]['city_a'] != map_original['roads'][i]['city_a']:
            print("Can't compare - different roads on same position")
        difference += (map_custom['roads'][i]['capacity'] - map_original['roads'][i]['capacity'])*map_original['roads'][i]['length']
    return difference

cur_expenses=0
def greedy(map_original):
    map_copy = copy.deepcopy(map_original)
    lengths = map_copy['roads']
    lengths = sorted(lengths, key=lambda k: k['length'])
    cur_expenses=0

    for i in range(len(lengths)):
        city_A=lengths[i]['city_a']
        city_B=lengths[i]['city_b']

        # We move in one direction
        city_A_data=(item for item in map_original['cities'] if item["name"] == city_A).__next__()
        city_B_data=(item for item in map_original['cities'] if item["name"] == city_B).__next__()

        cap_of_city_A=city_A_data['demand']['from']
        cap_of_city_B=city_B_data['demand']['to']

        cap_between_cities=min(cap_of_city_A, cap_of_city_B)
        lengths[i]['cap']=cap_between_cities

        if cur_expenses<map.budget and map_original['roads'][i]['capacity'] < cap_between_cities:
            if (cap_between_cities > map_original['roads'][i]['capacity']):
                newCapacity = (cap_between_cities - map_original['roads'][i]['capacity'])
                price= newCapacity * lengths[i]['length']
                print("Debug: before - ", lengths[i]['capacity'])
                lengths[i]['capacity'] = newCapacity
                cur_expenses+=price
                print("Debug: after - ",lengths[i]['capacity'])
    return map_copy

repaired_city = greedy(map.roads_map)

print("Chwila prawdy:",metrics(repaired_city,map.roads_map))