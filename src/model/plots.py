import matplotlib.pyplot as plt
import numpy as np
import test.two as two_dim
import test.five as five_dim
import test.ten as ten_dim
import test.twenty as twenty_dim
import test.thirty as thirty_dim
import test.fourty as fourty_dim
import test.fifty as fifty_dim

from heuristic import run_heuristic_nth_times, run_heuristic_for_budgets

dimensions = [2, 5, 10, 20, 30, 40, 50]

def run_heuristic_diff_evolution(n):
    result = []
    result.append(run_heuristic_nth_times(two_dim.roads_map, two_dim.budget, n, 'rand2bin'))
    result.append(run_heuristic_nth_times(five_dim.roads_map, five_dim.budget, n, 'rand2bin'))
    result.append(run_heuristic_nth_times(ten_dim.roads_map, ten_dim.budget, n, 'rand2bin'))
    result.append(run_heuristic_nth_times(twenty_dim.roads_map, twenty_dim.budget, n, 'rand2bin'))
    result.append(run_heuristic_nth_times(thirty_dim.roads_map, thirty_dim.budget, n, 'rand2bin'))
    result.append(run_heuristic_nth_times(fourty_dim.roads_map, fourty_dim.budget, n, 'rand2bin'))
    result.append(run_heuristic_nth_times(fifty_dim.roads_map, fifty_dim.budget, n, 'rand2bin'))

    return result

# def run_greedy(n):
#     result = []
#     result.append(run_heuristic_nth_times(two_dim.roads_map, two_dim.budget, n, 'rand2bin'))
#     result.append(run_heuristic_nth_times(five_dim.roads_map, five_dim.budget, n, 'rand2bin'))
#     result.append(run_heuristic_nth_times(ten_dim.roads_map, ten_dim.budget, n, 'rand2bin'))
#     result.append(run_heuristic_nth_times(twenty_dim.roads_map, twenty_dim.budget, n, 'rand2bin'))
#     result.append(run_heuristic_nth_times(thirty_dim.roads_map, thirty_dim.budget, n, 'rand2bin'))
#     result.append(run_heuristic_nth_times(fourty_dim.roads_map, fourty_dim.budget, n, 'rand2bin'))
#     result.append(run_heuristic_nth_times(fifty_dim.roads_map, fifty_dim.budget, n, 'rand2bin'))
#
#     return result_gr


def plot_obj_fun_dim(n):
    obj_func_vals = [i[0] for i in run_heuristic_diff_evolution(n)]
    plt.plot(dimensions, obj_func_vals)
    plt.ylabel('funkcja celu')
    plt.xlabel('wymiar problemu (ilość połączeń)')
    plt.show()


def plot_budget_usage_dim(n):
    obj_func_vals = [i[1] for i in run_heuristic_diff_evolution(n)]
    plt.plot(dimensions, obj_func_vals)
    plt.ylabel('zużycie budżetu')
    plt.xlabel('wymiar problemu (ilość połączeń)')
    plt.show()


def plot_fulfill_demand_factor_dim(n):
    obj_func_vals = [i[2] for i in run_heuristic_diff_evolution(n)]
    plt.plot(dimensions, obj_func_vals)
    plt.ylabel('współczynnik pokrycia zapotrzebowania')
    plt.xlabel('wymiar problemu (ilość połączeń)')
    plt.show()


def plot_obj_fun_budget(n, start_budget, end_budget, delta_budget, map):
    x_axis = np.arange(start_budget, end_budget, delta_budget)
    y_axis = [i[0] for i in run_heuristic_for_budgets(n, x_axis, map)]
    plt.plot(x_axis, y_axis)
    plt.ylabel('funkcja celu')
    plt.xlabel('budżet')
    plt.show()


def plot_budget_usage_budget(n, start_budget, end_budget, delta_budget, map):
    x_axis = np.arange(start_budget, end_budget, delta_budget)
    y_axis = [i[1] for i in run_heuristic_for_budgets(n, x_axis, map)]
    plt.plot(x_axis, y_axis)
    plt.ylabel('zużycie budżetu')
    plt.xlabel('budżet')
    plt.show()


def plot_fulfill_demand_factor_budget(n, start_budget, end_budget, delta_budget, map):
    x_axis = np.arange(start_budget, end_budget, delta_budget)
    y_axis = [i[2] for i in run_heuristic_for_budgets(n, x_axis, map)]
    plt.plot(x_axis, y_axis)
    plt.ylabel('współczynnik pokrycia zapotrzebowania')
    plt.xlabel('budżet')
    plt.show()

# plot_obj_fun_dim(50)
# plot_budget_usage_dim(50)
# plot_fulfill_demand_factor_dim(50)

# plot_fulfill_demand_factor_budget(20,100,150,3,twenty_dim.roads_map)
plot_fulfill_demand_factor_budget(30,100,150,3,thirty_dim.roads_map)

