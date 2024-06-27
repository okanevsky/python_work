sandwich_orders = ['1','pastrami', '2', '3','pastrami', '4','pastrami', '5']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('pastrami больше нет')

while sandwich_orders:
    current_san = sandwich_orders.pop()
    print('Бутер: ' + current_san + ' готовится')
    finished_sandwiches.append(current_san)

for sandwich in finished_sandwiches:
    print(sandwich + ' готов')