users = ['UseR1', 'user2', 'user3', 'user4', 'user5', 'adMin']
current_users = [current_user.lower() for current_user in users]
new_users = ['USER1', 'user6', 'user7', 'user8', 'user9', 'Admin']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Имя " + new_user + " занято")
    else:
        print("Приветствую " + new_user)
