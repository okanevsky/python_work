filename = 'text_files\opros.txt'
while True:
    with open(filename, 'a') as file_object:
        guest = input('почему вам нравится программировать (для выхода введите "q"): ')
        if guest == 'q':
            break
        else:
            file_object.write('\n'+guest)