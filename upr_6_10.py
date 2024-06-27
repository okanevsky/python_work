men_1 = {'имя':'1', 'фамилия':'11', 'город':'111'}
men_2 = {'имя':'2', 'фамилия':'22', 'город':'222'}
men_3 = {'имя':'3', 'фамилия':'33', 'город':'333'}

#favorite_places = {'горы':'', 'море':'', 'лес':'',}

#men_1['любимое место'] = favorite_places
favorite_digits = ['0', '1', '2', '3']
men_1['любимое число'] = favorite_digits[:2]
men_2['любимое число'] = favorite_digits[:1]
men_3['любимое число'] = favorite_digits[:4]

people = [men_1, men_2, men_3]
for men in people:
    for men_0, data in men.items():
        print('\n'+str(men_0))