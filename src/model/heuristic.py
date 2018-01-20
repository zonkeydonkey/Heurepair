from scipy.optimize import differential_evolution
from model import roads_list, max_road_demand, heuristic_factor
from roads_map import budget


max_obj_fun_res = 200000000000


def cost_fun(x):
    return sum(
        (x[i] - roads_list[i][0]) * roads_list[i][1]
        for i in range(len(x))
    )


def objective_fun(x):
    cost = cost_fun(x)
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
    best1bin = run_heuristic_nth_times(n, 'best1bin')
    best1exp = run_heuristic_nth_times(n, 'best1exp')
    rand1exp = run_heuristic_nth_times(n, 'rand1exp')
    randtobest1exp = run_heuristic_nth_times(n, 'randtobest1exp')
    best2exp = run_heuristic_nth_times(n, 'best2exp')
    rand2exp = run_heuristic_nth_times(n, 'rand2exp')
    randtobest1bin = run_heuristic_nth_times(n, 'randtobest1bin')
    best2bin = run_heuristic_nth_times(n, 'best2bin')
    rand2bin = run_heuristic_nth_times(n, 'rand2bin')
    rand1bin = run_heuristic_nth_times(n, 'rand1bin')
    print("best1bin: " + str(best1bin) + ", cost: " + str(cost_fun(best1bin)))
    print("best1exp: " + str(best1exp) + ", cost: " + str(cost_fun(best1exp)))
    print("rand1exp: " + str(rand1exp) + ", cost: " + str(cost_fun(rand1exp)))
    print("randtobest1exp: " + str(randtobest1exp) + ", cost: " + str(cost_fun(randtobest1exp)))
    print("best2exp: " + str(best2exp) + ", cost: " + str(cost_fun(best2exp)))
    print("rand2exp: " + str(rand2exp) + ", cost: " + str(cost_fun(rand2exp)))
    print("randtobest1bin: " + str(randtobest1bin) + ", cost: " + str(cost_fun(randtobest1bin)))
    print("best2bin: " + str(best2bin) + ", cost: " + str(cost_fun(best2bin)))
    print("rand2bin: " + str(rand2bin) + ", cost: " + str(cost_fun(rand2bin)))
    print("rand1bin: " + str(rand1bin) + ", cost: " + str(cost_fun(rand1bin)))

print(bounds)
run_strategies(20)

#result = differential_evolution(objective_fun, bounds)
#print(result.x)
#print(result.fun)
