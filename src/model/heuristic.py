import sys
from scipy.optimize import differential_evolution
from model import roads_list, max_road_demand
from roads_map import budget


def objective_fun(x):
    cost = sum(
        (x[i] - roads_list[i][0]) * roads_list[i][1]
        for i in range(len(x))
    )
    result = cost - sum(
        x[i]
        for i in range(len(x))
    )

    if cost > budget:
        return sys.float_info.max / 10000
    return result


create_bounds = lambda: \
    [
        (roads_list[i][0], roads_list[i][0])
        if (roads_list[i][0] >= max_road_demand[i])
        else (roads_list[i][0], max_road_demand[i])
        for i in range(len(roads_list))
    ]

bounds = create_bounds()

print(bounds)
result = differential_evolution(objective_fun, bounds)
print(result.x)
print(result.fun)
