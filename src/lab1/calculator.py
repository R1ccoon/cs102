def calculator(s) -> [str, float]:
    s = s.replace(' ', '')
    checkarray = ['*', '+', '-', '/', '.', '(', ')']
    for i in s:
        if not i.isdigit() and i not in checkarray:
            return 'Неверный формат ввода'
    if '/0' in s:
        return 'Деление на ноль'
    try:
        return eval(s)
    except Exception:
        return 'Ошибка'


if __name__ == '__main__':

    while True:
        print(str(calcurator(input())))
