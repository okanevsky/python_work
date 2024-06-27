promt = 'введите ваш возраст '
while True:
    age = input(promt)
    #age = int(age)
    if age == 'выход':
        break
    elif int(age) < 3:
        print('вход бесплатный')
    elif int(age)>=3 and int(age) <=12:
        print('вход 10$')
    elif int(age) > 12:
        print('вход 15$')