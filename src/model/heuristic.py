from scipy.optimize import differential_evolution
from model import create_roads_list, get_heuristic_factor, create_max_road_demand_list


max_obj_fun_res = 200000


def cost_fun(x, roads_list):
    return sum(
        (x[i] - roads_list[i][0]) * roads_list[i][1]
        for i in range(len(x))
    )


def objective_fun(x, roads_list, budget, max_road_demand):
    cost = cost_fun(x, roads_list)
    heuristic_factor = get_heuristic_factor(roads_list)
    result = cost - heuristic_factor * sum(
        x[i] - max_road_demand[1]
        for i in range(len(x))
    )

    if cost > budget:
        return max_obj_fun_res
    return result


create_bounds = lambda roads_list, max_road_demand: \
    [
        (roads_list[i][0], roads_list[i][0])
        if (roads_list[i][0] >= max_road_demand[i])
        else (roads_list[i][0], max_road_demand[i])
        for i in range(len(roads_list))
    ]


def get_fulfill_demand_factor(x, roads_list, max_road_demand):
    sum = 0
    sum_length = 0
    for i in range(len(x)):
        if x[i] < max_road_demand[i]:
            sum += (max_road_demand[i] - x[i]) * roads_list[i][1]
        sum_length += roads_list[i][1]
    if sum_length == 0:
        return 0
    return sum / sum_length


def get_avg_x_heuristic(map, budget, n, strategy):
    sum = 0
    roads_list = create_roads_list(map)
    max_road_demand = create_max_road_demand_list(map)
    bounds = create_bounds(roads_list, max_road_demand)
    for i in range(n):
        result = differential_evolution(objective_fun, bounds, (roads_list, budget, max_road_demand), strategy)
        sum += result.x
    return sum / n


def run_strategies(map, budget, n):
    best1bin = get_avg_x_heuristic(map, budget, n, 'best1bin')
    best1exp = get_avg_x_heuristic(map, budget, n, 'best1exp')
    rand1exp = get_avg_x_heuristic(map, budget, n, 'rand1exp')
    randtobest1exp = get_avg_x_heuristic(map, budget, n, 'randtobest1exp')
    best2exp = get_avg_x_heuristic(map, budget, n, 'best2exp')
    rand2exp = get_avg_x_heuristic(map, budget, n, 'rand2exp')
    randtobest1bin = get_avg_x_heuristic(map, budget, n, 'randtobest1bin')
    best2bin = get_avg_x_heuristic(map, budget, n, 'best2bin')
    rand2bin = get_avg_x_heuristic(map, budget, n, 'rand2bin')
    rand1bin = get_avg_x_heuristic(map, budget, n, 'rand1bin')
    roads_list = create_roads_list(map)
    print("best1bin: " + str(best1bin) + ", cost: " + str(cost_fun(best1bin, roads_list)))
    print("best1exp: " + str(best1exp) + ", cost: " + str(cost_fun(best1exp, roads_list)))
    print("rand1exp: " + str(rand1exp) + ", cost: " + str(cost_fun(rand1exp, roads_list)))
    print("randtobest1exp: " + str(randtobest1exp) + ", cost: " + str(cost_fun(randtobest1exp, roads_list)))
    print("best2exp: " + str(best2exp) + ", cost: " + str(cost_fun(best2exp, roads_list)))
    print("rand2exp: " + str(rand2exp) + ", cost: " + str(cost_fun(rand2exp, roads_list)))
    print("randtobest1bin: " + str(randtobest1bin) + ", cost: " + str(cost_fun(randtobest1bin, roads_list)))
    print("best2bin: " + str(best2bin) + ", cost: " + str(cost_fun(best2bin, roads_list)))
    print("rand2bin: " + str(rand2bin) + ", cost: " + str(cost_fun(rand2bin, roads_list)))
    print("rand1bin: " + str(rand1bin) + ", cost: " + str(cost_fun(rand1bin, roads_list)))


def run_heuristic_nth_times(map, budget, n, strategy):
    obj_fun_sum = 0
    capacity_values = 0
    roads_list = create_roads_list(map)
    max_road_demand = create_max_road_demand_list(map)
    bounds = create_bounds(roads_list, max_road_demand)
    for i in range(n):
        result = differential_evolution(objective_fun, bounds, (roads_list, budget, max_road_demand), strategy)
        obj_fun_sum += result.fun
        capacity_values += result.x
    capacity_values /= n
    budget_usage = (cost_fun(capacity_values, roads_list) / budget) * 100
    return obj_fun_sum / n, budget_usage, get_fulfill_demand_factor(capacity_values, roads_list, max_road_demand)