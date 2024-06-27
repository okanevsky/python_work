filename = 'text_files\guest_book.txt'
while True:
    with open(filename, 'a') as file_object:
        guest = input('ваше имя (для выхода введите "q"): ')
        if guest == 'q':
            break
        else:
            file_object.write('\n'+guest)