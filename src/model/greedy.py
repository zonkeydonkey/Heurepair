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
def greedy_fun(map_original,map_budget):
    map_copy = copy.deepcopy(map_original)
    lengths = map_copy['roads']
    lengths = sorted(lengths, key=lambda k: k['length'])
    cur_expenses=0
    last_expenses=0
    num_of_renov_roads=0
    renovated=[]
    max_caps=[]
    road_lengths=[]
    sum_of_len=0
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
        max_caps.append(lengths[i]['cap'])
        road_lengths.append(lengths[i]['length'])

    gen_vals=[]
    for i in range(len(lengths)):
        last_expenses = cur_expenses
        gen_vals.append(0)
        if cur_expenses < map_budget and lengths[i]['capacity'] < lengths[i]['cap']:
            capacity_diff = (lengths[i]['cap'] - lengths[i]['capacity'])
            gen_vals.pop(i)
            gen_vals.append(capacity_diff)
            price = capacity_diff * lengths[i]['length']
            lengths[i]['capacity'] = lengths[i]['capacity'] + capacity_diff
            cur_expenses+=price
            num_of_renov_roads += 1
            renovated.append([lengths[i]['city_a'], lengths[i]['city_b']])
            if cur_expenses > map_budget:
                num_of_renov_roads -= 1
                gen_vals.pop(i)
                for j in range(len(lengths) - i):
                    gen_vals.append(0)
                if last_expenses==0:
                    print("Budżet jest zbyt mały do wyremontowania czegokolwiek!", "\n Wynosił: ", map_budget, \
                            "\n Do wyremontowania najkrótszej drogi, należałoby wydać: ", cur_expenses)
                    return 0, max_caps, gen_vals, road_lengths
                else:
                    renovated.pop(num_of_renov_roads)
                    print("Dysponowano budżetem: ", map_budget, "\n Zużyto: ", last_expenses)
                    print("Wyremontowana liczba dróg: ", num_of_renov_roads)
                    print("Wyremontowano połączenia między miastami: ")
                    print(renovated)
                    return last_expenses, max_caps, gen_vals, road_lengths
    if cur_expenses > 0:
        print('Udało się wyremontować wszystkie drogi!')
        print("Dysponowano budżetem: ", map_budget, "\n Zużyto: ", cur_expenses)
        print("Wyremontowana liczba dróg: ", num_of_renov_roads)
        print("Wyremontowano połączenia między miastami: ")
        print(renovated)
    return cur_expenses, max_caps, gen_vals, road_lengths
    # return map_copy


def greedy_bud(map_original,map_budget):
    bud, x, y, z = greedy_fun(map_original,map_budget)
    bud = 100*bud/map_budget
    return bud

def greedy_budg(budgets, map_original):
    res=[]
    for bud in budgets:
        bud_fun, x, y, z = greedy_fun(map_original, bud)
        bud_fun = 100*bud_fun/bud
        res.append(bud_fun)
    return res

def fulfill(map_original,map_budget):
    x, caps, vals, lgths = greedy_fun(map_original,map_budget)
    sum_of_len = sum(lgths)
    fulfill_demand=0
    for i in range(len(caps)):
        fulfill_demand += (caps[i] - vals[i])*lgths[i]/sum_of_len
    return fulfill_demand


def fulfill_budg(budgets, map_original):
    res1=[]
    for bud in budgets:
        fulf = fulfill(map_original, bud)
        res1.append(fulf)
    return res1

greedy_fun(map.roads_map,map.budget)

# print("Chwila prawdy:",metrics(repaired_city,map.roads_map))