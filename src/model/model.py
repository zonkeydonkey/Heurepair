def find_city(map, city_name):
    for city in list(map['cities']):
        if city['name'] == city_name:
            return city['demand']['from'], city['demand']['to']

    return -1, -1


create_roads_list = lambda map: \
    [
        (road['capacity'], road['length'])
        for road in list(map['roads'])
    ]

create_max_road_demand_list = lambda map: \
    [
        max(
            min(find_city(map, road['city_a'])[0], find_city(map, road['city_b'])[1]),
            min(find_city(map, road['city_b'])[1], find_city(map, road['city_a'])[0])
        )
        for road in list(map['roads'])
    ]


def get_heuristic_factor(roads_list):
    sum = 0
    for road in roads_list:
        sum += road[1]
    return sum / len(roads_list)