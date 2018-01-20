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
