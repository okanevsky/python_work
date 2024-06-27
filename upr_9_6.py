class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' ' + self.cuisine_type.title())
    def open_restaurant(self):
        print('Ресторан открыт')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['ванильное','клубничное','пломбир']
    def read_flavors(self):
            print(self.flavors)

restaurant = Restaurant('москва','русская')
restaurant.describe_restaurant()
restaurant.open_restaurant()
icecream = IceCreamStand('париж','французская')
icecream.read_flavors()