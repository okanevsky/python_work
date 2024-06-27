class Privileges():
    def __init__(self):
        self.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']
    def show_privileges(self):
        print(self.privileges)