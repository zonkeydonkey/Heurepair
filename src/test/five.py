roads_map = {
    'cities': [
        {
            'name': "krakow",
            'demand': {
                'from': 23.4,
                'to': 56.3
            }
        },

        {
            'name': "kielce",
            'demand': {
                'from': 45.3,
                'to': 12.1
            }
        },

        {
            'name': "pcim",
            'demand': {
                'from': 12.3,
                'to': 1.8
            }
        },

        {
            'name': "koluszki",
            'demand': {
                'from': 56.9,
                'to': 23.0
            }
        }
    ],

    'roads': [
        {
            'city_a': "kielce",
            'city_b': "krakow",
            'capacity': 34.8,
            'length': 26.4
        },

        {
            'city_a': "pcim",
            'city_b': "krakow",
            'capacity': 6.56,
            'length': 30.2
        },

        {
            'city_a': "pcim",
            'city_b': "koluszki",
            'capacity': 45.9,
            'length': 24.8
        },

        {
            'city_a': "kielce",
            'city_b': "koluszki",
            'capacity': 95.6,
            'length': 20.6
        },

        {
            'city_a': "kielce",
            'city_b': "pcim",
            'capacity': 63.0,
            'length': 12.8
        }
    ]
}

budget = 1500