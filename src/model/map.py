map = {
    'cities': [
        {
            'name': "krakow",
            'from': 23.4,
            'to': 56.3
        },

        {
            'name': "kielce",
            'from': 45.3,
            'to': 12.1
        },

        {
            'name': "pcim",
            'from': 12.3,
            'to': 1.8
        }
    ],

    'roads': [
        {
            'city_a': "kielce",
            'city_b': "krakow",
            'capacity': 34.8,
            'length': 200.4
        },

        {
            'city_a': "pcim",
            'city_b': "krakow",
            'capacity': 4.56,
            'length': 356.2
        }
    ]
}

create_roads_list = lambda: \
    [
        (road['capacity'], road['length'])
        for road in list(map['roads'])
    ]

roads_list = create_roads_list()

