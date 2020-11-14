dict_x = {}
dict_x['key_junk'] = 'junk'
dict_x['key1'] = 'Alan' # new entries automatically added
dict_x['key2'] = 'Peeeeter'
dict_x['key2'] = 'Peter' # update an entry

print(dict_x.keys())
print(dict_x.values())
print(dict_x.items())

for key in dict_x.keys():
    print('key = ' + key)

for value in dict_x.values():
        print('value = ' + value)

for key, value in dict_x.items():
        print('key = ' + key, 'value = ' + value)


CUSTOMERS = {
    "customer_1": {
        "account_1A": {
            "first_name": "Alan",
            "last_name": "Johnson"
        },
        "account_1B": {
            "first_name": "Melanie",
            "last_name": "Johnson"
        }
    },
    "customer_2": {
        "account_2A": {
            "first_name": "Matthew",
            "last_name": "Johnson"
        }
    }
}

print (CUSTOMERS["customer_1"].keys())
print (CUSTOMERS["customer_1"].values())
print (CUSTOMERS["customer_1"].items())

ACCOUNT_1A = CUSTOMERS["customer_1"]["account_1A"]
# produces a list of keys: ['first_name', 'last_name']
print (ACCOUNT_1A.keys())
# produces a list of values: ['Alan', 'Johnson']
print (ACCOUNT_1A.values())
# produces a list of (name, value) tuples: [('first_name', 'Alan'), ('last_name', 'Johnson')]
print (ACCOUNT_1A.items())

# produces 3 element dictionary {1: 1, 2: 4, 3: 9}
DICT_A = {
    i: i_squared
    for i in range(1,4)
    for i_squared in [i*i]
}
print(DICT_A)

regions = {
    'Region_CH': 'Switzerland',
    'Region_APAC': 'APAC',
    'Region_AM': 'America'
}
countries = {
    'Region_CH': {'CH': 'Switzerland'},
    'Region_APAC': {'JP': 'Japan',
                    'SG': 'Singapore'},
    'Region_AM': {'CH', 'Mexico'}
}

# produces 1 element dictionary: {'Region_APAC': {'JP': 'Japan', 'SG': 'Singapore'}}
DICT_B = {
    region_code: {
        country_code: countries[region_code][country_code]
        for country_code in countries[region_code]
    }
    for region_code in regions.keys() if region_code == 'Region_APAC'
}

print(DICT_B)

# produces 1 element dictionary: {'Region_APAC': {'JP': 'Japan', 'SG': 'Singapore'}}
DICT_C = {
    region_code: {
        country_code: country_name
        for country_code, country_name in countries[region_code].items()
    }
    for region_code in regions.keys() if region_code == 'Region_APAC'
}

print(DICT_C)