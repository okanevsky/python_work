def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename, 'r', encoding='latin-1') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Файл " + filename + " не найден."
        print(msg)
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print("Файл " + filename + " имеет " + str(num_words) +" слов.")

filenames = ['text_files\Alice.txt', 'text_files\siddhartha.txt', 'text_files\moby_dick.txt', 'text_files\little_women.txt']
for filename in filenames:
    count_words(filename)