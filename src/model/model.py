from roads_map import roads_map


def find_city(city_name):
    for city in list(roads_map['cities']):
        if city['name'] == city_name:
            return city['demand']['from'], city['demand']['to']

    return -1, -1


create_roads_list = lambda: \
    [
        (road['capacity'], road['length'])
        for road in list(roads_map['roads'])
    ]

roads_list = create_roads_list()

create_max_road_demand_list = lambda: \
    [
        max(
            min(find_city(road['city_a'])[0], find_city(road['city_b'])[1]),
            min(find_city(road['city_b'])[1], find_city(road['city_a'])[0])
        )
        for road in list(roads_map['roads'])
    ]

max_road_demand = create_max_road_demand_list()


def get_heuristic_factor():
    sum = 0
    for road in roads_list:
        sum += road[1]
    return sum / len(roads_list)

heuristic_factor = get_heuristic_factor()