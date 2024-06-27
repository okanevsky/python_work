def read_file(filename):
    """Чтение содержимого файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #msg = "Файл " + filename + " не найден."
        #print(msg)
    else:
        # Подсчет приблизительного количества строк в файле.
        print(contents)

filenames = ['text_files\cats.txt', 'text_files\dogs.txt']
for filename in filenames:
    read_file(filename)