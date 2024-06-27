class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' ' + self.cuisine_type.title())

    def open_restaurant(self):
        print('Ресторан открыт')

    def read_number(self):
        print(self.number_served)

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, numbers):
        self.number_served +=numbers


restaurant = Restaurant('москва','русская')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(50)
restaurant.read_number()

restaurant.increment_number_served(12)
restaurant.read_number()
