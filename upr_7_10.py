otpuska = {}
opros = True
while opros:
    name = input('введите ваше имя ')
    otpusk = input('\nвведите место отпуска')
    otpuska[name] = otpusk

    povtor = input('\nпродолжить опрос? (да/нет)')
    if povtor == 'нет':
        opros = False
print('результаты опроса\n')

for name, otpusk in otpuska.items():
    print(name + ' - ' + otpusk)