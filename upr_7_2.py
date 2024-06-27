messege = input('На сколько мест вы хотите заказать стол? ')
messege = int(messege)
if messege > 8:
    print('Вам придется подождать')
else:
    print ('стол готов')