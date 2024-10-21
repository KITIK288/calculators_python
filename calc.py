# Это калькулятор, написанный на python.

def calc():
    print("Это калькулятор на языке python")
    print("Введите ваше число")
    num1 = int(input())
    print("Введите второе число")
    num2 = int(input())
    print("Выберите, какую операцию вы хотите произвести над вашими числами")
    print("1 - сложение")
    print("2 - вычитание")
    print("3 - умножение")
    print("4 - деление")
    you_choice = int(input())
    while 1:
        if you_choice > 4 or you_choice == 0:
            print("Не корректный выбор, попробуйте ещё раз")
            you_choice = int(input())
        else:
            break
    if you_choice == 1:
        suma = num1 + num2
        print("Сумма чисел", num1 ,"и", num2 ,"=", suma)
    elif you_choice  == 2:
        difference = num1 - num2
        print("Разность чисел", num1, "и", num2, "=",  difference)
    elif you_choice == 3:
        mult =  num1 * num2
        print("Произведение чисел", num1, "и", num2, "=",  mult)
    else:
        div = num1 /  num2
        print("Произведение чисел", num1, "и", num2, "=",  div)

calc()