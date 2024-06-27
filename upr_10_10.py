def count_words(filename, word):
    """Подсчет вхождения слова в файле."""
    try:
        with open(filename, 'r', encoding='latin-1') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Файл " + filename + " не найден."
        print(msg)
    else:
        words = contents.lower().split()
        num_words = words.count(word)
        print("Слово " + word + " встречается " + str(num_words) +" раза в файле " + filename)

filenames = ['text_files\Alice.txt', 'text_files\siddhartha.txt', 'text_files\moby_dick.txt', 'text_files\little_women.txt']
for filename in filenames:
    count_words(filename, 'the')