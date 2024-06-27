filename = 'text_files\Alice.txt'
try:
    with open(filename, 'r', encoding='latin-1') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) +" words.")