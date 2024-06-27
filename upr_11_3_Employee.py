class Employee:
    def __init__(self, first, last, price=0):
        self.first = first
        self.last = last
        self.price = price

    def give_raise(self):
        if self.price:
            self.price+=self.price
        else:
            self.price +=5000
        print(self.price)

#user = Employee('oleg', 'kanevsky',5)
#user.give_raise()