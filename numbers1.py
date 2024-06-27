numbers = [str(number) for number in range(1,11)]
for number in numbers:
    if number == "1":
        print(number + "st")
    elif number == "2":
        print(number + "nd")
    elif number == "3":
        print(number + "rd")
    else:
        print(number + "th")