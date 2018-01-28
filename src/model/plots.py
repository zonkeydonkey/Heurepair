import matplotlib.pyplot as plt
import numpy as np
import data.two as two_dim
import data.five as five_dim
import data.ten as ten_dim
import data.twenty as twenty_dim
import data.thirty as thirty_dim
import data.fourty as fourty_dim
import data.fifty as fifty_dim

from heuristic import run_heuristic_nth_times, run_heuristic_for_budgets
from greedy import greedy_bud, greedy_budg

dimensions = [2, 5, 10, 20, 30, 40, 50]

def run_heuristic_diff_evolution(n, strategy):
    result = []
    result.append(run_heuristic_nth_times(two_dim.roads_map, two_dim.budget, n, strategy))
    result.append(run_heuristic_nth_times(five_dim.roads_map, five_dim.budget, n, strategy))
    result.append(run_heuristic_nth_times(ten_dim.roads_map, ten_dim.budget, n, strategy))
    result.append(run_heuristic_nth_times(twenty_dim.roads_map, twenty_dim.budget, n, strategy))
    result.append(run_heuristic_nth_times(thirty_dim.roads_map, thirty_dim.budget, n, strategy))
    result.append(run_heuristic_nth_times(fourty_dim.roads_map, fourty_dim.budget, n, strategy))
    result.append(run_heuristic_nth_times(fifty_dim.roads_map, fifty_dim.budget, n, strategy))

    return result

def run_greedy_bud():
    result_bud = []
    result_bud.append(greedy_bud(two_dim.roads_map,two_dim.budget))
    result_bud.append(greedy_bud(five_dim.roads_map,five_dim.budget))
    result_bud.append(greedy_bud(ten_dim.roads_map,ten_dim.budget))
    result_bud.append(greedy_bud(twenty_dim.roads_map,twenty_dim.budget))
    result_bud.append(greedy_bud(thirty_dim.roads_map,thirty_dim.budget))
    result_bud.append(greedy_bud(fourty_dim.roads_map,fourty_dim.budget))
    result_bud.append(greedy_bud(fifty_dim.roads_map,fifty_dim.budget))

    return result_bud

def available():
    available_bud = []
    available_bud.append(two_dim.budget)
    available_bud.append(five_dim.budget)
    available_bud.append(ten_dim.budget)
    available_bud.append(twenty_dim.budget)
    available_bud.append(thirty_dim.budget)
    available_bud.append(fourty_dim.budget)
    available_bud.append(fifty_dim.budget)

    return available_bud

def plot_obj_fun_dim(n, strategy):
    obj_func_vals = [i[0] for i in run_heuristic_diff_evolution(n, strategy)]
    plt.plot(dimensions, obj_func_vals)
    plt.ylabel('funkcja celu')
    plt.xlabel('wymiar problemu (ilość połączeń)')
    plt.show()


def plot_budget_usage_dim(n, strategy):
    obj_func_vals = [i[1] for i in run_heuristic_diff_evolution(n, strategy)]
    vals_for_greedy = [j for j in run_greedy_bud()]
    available_budget = [k for k in available()]
    plt.plot(dimensions, obj_func_vals)
    plt.plot(dimensions, vals_for_greedy)
    plt.plot(dimensions, available_budget)
    plt.legend(['alg. ewolucji różnicowej','alg. zachłanny', 'dostępny budżet'])
    plt.ylabel('zużycie budżetu')
    plt.xlabel('wymiar problemu (ilość połączeń)')
    plt.show()


def plot_fulfill_demand_factor_dim(n, strategy):
    obj_func_vals = [i[2] for i in run_heuristic_diff_evolution(n, strategy)]
    plt.plot(dimensions, obj_func_vals)
    plt.ylabel('współczynnik pokrycia zapotrzebowania')
    plt.xlabel('wymiar problemu (ilość połączeń)')
    plt.show()


def plot_obj_fun_budget(n, start_budget, end_budget, delta_budget, map, strategy):
    x_axis = np.arange(start_budget, end_budget, delta_budget)
    y_axis = [i[0] for i in run_heuristic_for_budgets(map, x_axis, n, strategy)]
    plt.plot(x_axis, y_axis)
    plt.ylabel('funkcja celu')
    plt.xlabel('budżet')
    plt.legend(['heurystyczny', 'zachłanny'])
    plt.show()


def plot_budget_usage_budget(n, start_budget, end_budget, delta_budget, map, strategy):
    x_axis = np.arange(start_budget, end_budget, delta_budget)
    y_axis = [i[1] for i in run_heuristic_for_budgets(map, x_axis, n, strategy)]
    y_axis_gr = [j for j in greedy_budg(x_axis,map)]
    plt.plot(x_axis, y_axis)
    plt.plot(x_axis, y_axis_gr)
    plt.legend(['alg. ewolucji różnicowej', 'alg. zachłanny'])
    plt.ylabel('zużycie budżetu')
    plt.xlabel('budżet')
    plt.show()

def plot_fulfill_demand_factor_budget(n, start_budget, end_budget, delta_budget, map, strategy):
    x_axis = np.arange(start_budget, end_budget, delta_budget)
    y_axis = [i[2] for i in run_heuristic_for_budgets(map, x_axis, n, strategy)]
    plt.plot(x_axis, y_axis)
    plt.ylabel('współczynnik pokrycia zapotrzebowania')
    plt.xlabel('budżet')
    plt.show()
