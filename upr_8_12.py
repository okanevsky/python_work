def make_buter(*toppings):
    """Вывод списка заказанных дополнений."""
    print("\nMaking a buter with the following toppings:")
    for topping in toppings:
        print(topping)
make_buter('pepperoni')
make_buter('mushrooms', 'green peppers', 'extra cheese')
make_buter('1', '2', '3','4')