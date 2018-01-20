from scipy import special, optimize
from model import roads_list


objective_fun = lambda x: \
        sum (
            (x[i] - roads_list[i][0]) * roads_list[i][1] - x[i]
            for i in range(len(x))
        )

x0 = [2, 3]

print(objective_fun(x0))