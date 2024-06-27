def make_great(names, great_names):
    while names:
        current_name = names.pop()
        great_names.append('Great ' + current_name)

def show_magicians(names):
    """Вывод простого приветствия для каждого пользователя в списке."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

names = ['hannah', 'ty', 'margot']
great_names = []

make_great(names[:], great_names)
show_magicians(names)
show_magicians(great_names)