filename = 'text_files\pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
    
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + '...')
print(len(pi_string))

birthday = input("введите дату своего рождения (01012022): ")
if birthday in pi_string:
    print("ваша дата входит в 1-й миллион pi!")
else:
    print("вашей даты нет в в миллионе pi.")