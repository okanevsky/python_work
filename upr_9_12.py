from class_Privileges import Privileges
from class_Admin import Admin

user1 = Admin('олег', 'каневский')
user1.describe_user()
user1.greet_user()
user1.privileges.show_privileges()