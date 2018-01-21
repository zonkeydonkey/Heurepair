import sys
from model import roads_list, max_road_demand
from roads_map import *
import copy

def metrics(map_custom, map_original):
    lenMap = len(map_custom['roads'])
    difference = 0
    for i in range(lenMap):
        # tutaj powinien być warunek sprawdzający czy porównujemy drogi do tych samych/z tych samych miast
        difference += (map_custom['roads'][i]['capacity'] - map_original['roads'][i]['capacity'])*map_original['roads'][i]['length']
    return difference

cur_expenses=0
def greedy(map_original):
    map_copy = copy.deepcopy(map_original)
    lengths = map_copy['roads']
    lengths = sorted(lengths, key=lambda k: k['length'])
    cur_expenses,curr_espenses=0,0

    for i in range(len(lengths)):
        city_A=lengths[i]['city_a']
        city_B=lengths[i]['city_b']

        #SYLWIA, trzeba wywalić potem ten comment: zakładam że poruszamy się w jednym kierunku. Moze to nie ma znaczenia, już nie wiem xD
        city_A_data=(item for item in map_original['cities'] if item["name"] == city_A).__next__()
        city_B_data=(item for item in map_original['cities'] if item["name"] == city_B).__next__()

        cap_of_city_A=city_A_data['demand']['from']
        cap_of_city_B=city_B_data['demand']['to']

        cap_of_city=min(cap_of_city_A, cap_of_city_B)
        lengths[i]['cap']=cap_of_city

        if cur_expenses<budget:
            curr_expenses=cur_expenses
            price=(cap_of_city-map_original['roads'][i]['capacity'])*lengths[i]['length']
            cur_expenses+=price

    print(curr_espenses)
    print(budget)
    return map_copy

repaired_city = greedy(roads_map)

print("Chwila prawdy:",metrics(repaired_city,roads_map))