class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())
    def greet_user(self):
        print('Добрый день, ' + self.first_name.title() + ' ' + self.last_name.title())


user1 = User('олег', 'каневский')
user1.describe_user()
user1.greet_user()

user2 = User('ким', 'ян')
user2.describe_user()
user2.greet_user()

user3 = User('петр', 'маковский')
user3.describe_user()
user3.greet_user()