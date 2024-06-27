cities = {'москва':'', 'питер':'', 'новосиб':'',}

city_1 = {'страна':'россия', 'население':'12000000', 'факт':'столица россии',}
city_2 = {'страна':'россия', 'население':'6000000', 'факт':'культурная столица россии',}
city_3 = {'страна':'россия', 'население':'2500000', 'факт':'столица сибири',}

cities['москва'] = city_1
cities['питер'] = city_2
cities['новосиб'] = city_3

for town, data in cities.items():
    print("\n"+town.title())
    for key, value in data.items():
        if key == 'страна' or key == 'факт':
            print(str(key) + " - " + str(value).title())
        else:
            print(str(key) + " - " + str(value))