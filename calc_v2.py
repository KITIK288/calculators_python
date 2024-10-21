def calculator(expression):
    try:
        expression = expression.replace(" ", "")

        if not all(char in '0123456789+-*/.' for char in expression):
            raise ValueError("Выражение содержит недопустимые символы.")

        result = eval(expression)
        return result

    except ZeroDivisionError:
        return "Ошибка: деления на ноль."
    except Exception as e:
        return f"Ошибка: {str(e)}"

def start():
    user_input = input("Введите математическое выражение: ")
    output = calculator(user_input)
    print(f"Результат: {output}")

start()
