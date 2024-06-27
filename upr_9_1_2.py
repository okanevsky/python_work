class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' ' + self.cuisine_type.title())
    def open_restaurant(self):
        print('Ресторан открыт')

restaurant = Restaurant('москва','русская')
#print(restaurant.restaurant_name.title() + ' ' + restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('париж','французская')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('милан','итальянская')
restaurant.describe_restaurant()
restaurant.open_restaurant()