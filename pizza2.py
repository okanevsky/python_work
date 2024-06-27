def make_pizza(size,*toppings):
    """Вывод списка заказанных дополнений."""
    print("\nMaking a "+ str(size)+" pizza with the following toppings:")
    for topping in toppings:
        print(topping)