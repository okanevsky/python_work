filename = 'text_files\learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

i=0
while i<3:
    for line in lines:
        print(line.strip())
    i+=1
    print('')