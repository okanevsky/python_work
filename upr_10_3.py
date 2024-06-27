filename = 'text_files\guest.txt'
guest = input('ваше имя: ')
with open(filename, 'a') as file_object:
    file_object.write('\n'+guest)