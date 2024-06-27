class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print('Добрый день, ' + self.first_name.title() + ' ' + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts +=1

    def read_login_attempt(self):
        print(self.login_attempts)
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('олег', 'каневский')
user1.describe_user()
user1.greet_user()
user1.read_login_attempt()
user1.increment_login_attempts()
user1.read_login_attempt()
user1.reset_login_attempts()
user1.read_login_attempt()
