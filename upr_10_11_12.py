import json

def open_favorite_number(filename):
    """Получает хранимое число, если оно существует."""
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number
    
def get_favorite_number(filename):
    """Создает число"""
    favorite_number = input('введите любимое число: ')
    with open(filename,'w') as f_obj:
        json.dump(favorite_number, f_obj)
    return favorite_number

def output_favorite_number(filename):
    favorite_number = open_favorite_number(filename)
    if favorite_number:
        print('Ваще любимое число: ' + favorite_number)
    else:
        favorite_number = get_favorite_number(filename)

file_name = 'json_files\\favorite_number.json'
output_favorite_number(file_name)