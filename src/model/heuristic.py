from scipy.optimize import differential_evolution
from model import roads_list, max_road_demand, heuristic_factor
from roads_map import budget


max_obj_fun_res = 200000000000


def objective_fun(x):
    cost = sum(
        (x[i] - roads_list[i][0]) * roads_list[i][1]
        for i in range(len(x))
    )
    result = cost - heuristic_factor * sum(
        x[i]
        for i in range(len(x))
    )

    if cost > budget:
        return max_obj_fun_res
    return result


create_bounds = lambda: \
    [
        (roads_list[i][0], roads_list[i][0])
        if (roads_list[i][0] >= max_road_demand[i])
        else (roads_list[i][0], max_road_demand[i])
        for i in range(len(roads_list))
    ]

bounds = create_bounds()


def run_heuristic_nth_times(n, strategy):
    sum = 0
    for i in range(n):
        result = differential_evolution(objective_fun, bounds, (), strategy)
        sum += result.x
    return sum/n


def run_strategies(n):
    print("best1bin: " + str(run_heuristic_nth_times(n, 'best1bin')))
    print("best1exp: " + str(run_heuristic_nth_times(n, 'best1exp')))
    print("rand1exp: " + str(run_heuristic_nth_times(n, 'rand1exp')))
    print("randtobest1exp: " + str(run_heuristic_nth_times(n, 'randtobest1exp')))
    print("best2exp: " + str(run_heuristic_nth_times(n, 'best2exp')))
    print("rand2exp: " + str(run_heuristic_nth_times(n, 'rand2exp')))
    print("randtobest1bin: " + str(run_heuristic_nth_times(n, 'randtobest1bin')))
    print("best2bin: " + str(run_heuristic_nth_times(n, 'best2bin')))
    print("rand2bin: " + str(run_heuristic_nth_times(n, 'rand2bin')))
    print("rand1bin: " + str(run_heuristic_nth_times(n, 'rand1bin')))

print(bounds)
run_strategies(20)

#result = differential_evolution(objective_fun, bounds)
#print(result.x)
#print(result.fun)
