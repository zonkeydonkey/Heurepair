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
        },

        {
            'name': "katowice",
            'demand': {
                'from': 6.9,
                'to': 104.0
            }
        },

        {
            'name': "ketrzyn",
            'demand': {
                'from': 45.3,
                'to': 91.2
            }
        },

        {
            'name': "szczecin",
            'demand': {
                'from': 9.8,
                'to': 12.6
            }
        },

        {
            'name': "sucha",
            'demand': {
                'from': 34.5,
                'to': 65.2
            }
        },

        {
            'name': "warszawa",
            'demand': {
                'from': 76.5,
                'to': 189.3
            }
        },

        {
            'name': "gdansk",
            'demand': {
                'from': 156.3,
                'to': 99.4
            }
        },

        {
            'name': "olsztyn",
            'demand': {
                'from': 43.2,
                'to': 44.3
            }
        },

        {
            'name': "ciechanow",
            'demand': {
                'from': 39.5,
                'to': 29.7
            }
        },

        {
            'name': "elk",
            'demand': {
                'from': 29.3,
                'to': 13.6
            }
        },

        {
            'name': "modlin",
            'demand': {
                'from': 115.4,
                'to': 39.2
            }
        },

        {
            'name': "piaseczno",
            'demand': {
                'from': 44.3,
                'to': 33.2
            }
        },

        {
            'name': "bobrowiec",
            'demand': {
                'from': 25.4,
                'to': 19.2
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
        },

        {
            'city_a': "katowice",
            'city_b': "pcim",
            'capacity': 54.9,
            'length': 76.3
        },

        {
            'city_a': "katowice",
            'city_b': "ketrzyn",
            'capacity': 17.6,
            'length': 37.2
        },

        {
            'city_a': "kielce",
            'city_b': "ketrzyn",
            'capacity': 42.8,
            'length': 62.4
        },

        {
            'city_a': "krakow",
            'city_b': "ketrzyn",
            'capacity': 9.54,
            'length': 37.2
        },

        {
            'city_a': "katowice",
            'city_b': "koluszki",
            'capacity': 52.1,
            'length': 39.7
        },
# 10
        {
            'city_a': "kielce",
            'city_b': "warszawa",
            'capacity': 42.9,
            'length': 18.4
        },

        {
            'city_a': "warszawa",
            'city_b': "krakow",
            'capacity': 3.5,
            'length': 24.3
        },

        {
            'city_a': "pcim",
            'city_b': "sucha",
            'capacity': 17.2,
            'length': 36.2
        },

        {
            'city_a': "sucha",
            'city_b': "koluszki",
            'capacity': 54.3,
            'length': 12.6
        },

        {
            'city_a': "warszawa",
            'city_b': "pcim",
            'capacity': 28.4,
            'length': 29.3
        },

        {
            'city_a': "szczecin",
            'city_b': "pcim",
            'capacity': 83.4,
            'length': 14.3
        },

        {
            'city_a': "szczecin",
            'city_b': "ketrzyn",
            'capacity': 68.3,
            'length': 37.2
        },

        {
            'city_a': "kielce",
            'city_b': "szczecin",
            'capacity': 7.34,
            'length': 8.45
        },

        {
            'city_a': "szczecin",
            'city_b': "sucha",
            'capacity': 92.3,
            'length': 45.2
        },

        {
            'city_a': "katowice",
            'city_b': "sucha",
            'capacity': 17.4,
            'length': 43.8
        },

# 20
        {
            'city_a': "kielce",
            'city_b': "ciechanow",
            'capacity': 17.9,
            'length': 40.2
        },

        {
            'city_a': "gdansk",
            'city_b': "olsztyn",
            'capacity': 30.7,
            'length': 24.1
        },

        {
            'city_a': "olsztyn",
            'city_b': "ciechanow",
            'capacity': 18.9,
            'length': 20.2
        },

        {
            'city_a': "ciechanow",
            'city_b': "koluszki",
            'capacity': 12.7,
            'length': 70.2
        },

        {
            'city_a': "koluszki",
            'city_b': "olsztyn",
            'capacity': 37.8,
            'length': 102.5
        },

        {
            'city_a': "gdansk",
            'city_b': "koluszki",
            'capacity': 36.9,
            'length': 45.9
        },

        {
            'city_a': "sucha",
            'city_b': "ciechanow",
            'capacity': 26.9,
            'length': 59.3
        },

        {
            'city_a': "olsztyn",
            'city_b': "sucha",
            'capacity': 90.9,
            'length': 10.2
        },

        {
            'city_a': "kielce",
            'city_b': "gdansk",
            'capacity': 99.9,
            'length': 90.2
        },

        {
            'city_a': "ketrzyn",
            'city_b': "gdansk",
            'capacity': 12.1,
            'length': 16.8
        },
# 30
        {
            'city_a': "ketrzyn",
            'city_b': "ciechanow",
            'capacity': 19.1,
            'length': 27.7
        },

        {
            'city_a': "ketrzyn",
            'city_b': "olsztyn",
            'capacity': 39.9,
            'length': 115.3
        },

        {
            'city_a': "modlin",
            'city_b': "olsztyn",
            'capacity': 39.7,
            'length': 35.6
        },

        {
            'city_a': "ciechanow",
            'city_b': 'modlin',
            'capacity': 89.7,
            'length': 15.6
        },

        {
            'city_a': "elk",
            'city_b': "ciechanow",
            'capacity': 39.7,
            'length': 19.7
        },

        {
            'city_a': "elk",
            'city_b': "sucha",
            'capacity': 10.7,
            'length': 105.0
        },

        {
            'city_a': "elk",
            'city_b': "pcim",
            'capacity': 9.7,
            'length': 5.6
        },

        {
            'city_a': "elk",
            'city_b': "gdansk",
            'capacity': 107.4,
            'length': 45.4
        },

        {
            'city_a': "krakow",
            'city_b': "elk",
            'capacity': 33.9,
            'length': 77.7
        },

        {
            'city_a': "modlin",
            'city_b': "krakow",
            'capacity': 79.7,
            'length': 80.2
        },
# 40
        {
            'city_a': "krakow",
            'city_b': "piaseczno",
            'capacity': 23.9,
            'length': 67.7
        },

        {
            'city_a': "piaseczno",
            'city_b': "elk",
            'capacity': 23.9,
            'length': 80.3
        },

        {
            'city_a': "bobrowiec",
            'city_b': "piaseczno",
            'capacity': 12.9,
            'length': 1.2
        },

        {
            'city_a': "krakow",
            'city_b': "bobrowiec",
            'capacity': 13.4,
            'length': 79.5
        },

        {
            'city_a': "ciechanow",
            'city_b': "bobrowiec",
            'capacity': 63.9,
            'length': 69.3
        },

        {
            'city_a': "gdansk",
            'city_b': "piaseczno",
            'capacity': 12.9,
            'length': 77.0
        },

        {
            'city_a': "piaseczno",
            'city_b': "sucha",
            'capacity': 23.9,
            'length': 80.4
        },

        {
            'city_a': "pcim",
            'city_b': "bobrowiec",
            'capacity': 9.9,
            'length': 95.7
        },

        {
            'city_a': "koluszki",
            'city_b': "elk",
            'capacity': 30.8,
            'length': 97.7
        },

        {
            'city_a': "szczecin",
            'city_b': "piaseczno",
            'capacity': 6.9,
            'length': 83.4
        }
# 50
    ]
}

budget = 100