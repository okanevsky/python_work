print("введите 2 числа")
print("введите 'q' для выхода")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except (TypeError, ValueError) as er:
        print('не является числом ')
    else:
        print(answer)