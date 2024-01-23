# Программирование на языке высокого уровня (Python).
# Задание №2.
#
# Выполнил: Кобылка Кирилл Константинович.
# Группа: ПИН-б-о-21-1
# E-mail: kivi3viki4@gmail.com


from терминал import Терминал

if __name__ == "__main__":

    терминал1 = Терминал()
    print(терминал1)
    while True:
        терминал1.показать_меню()
        пункт_меню = input()
        терминал1.обработать_команду(пункт_меню)


# -------------
# Пример вывода:

# --------------------------------------------------
# Пиццерия #1
# Добро пожаловать!
#
# Меню:
# 1. Пицца: Пепперони | Цена: 350.00 р.
#    Тесто: тонкое Соус: томатный
#    Начинка: пепперони, сыр моцарелла
# 2. Пицца: Барбекю | Цена: 450.00 р.
#    Тесто: тонкое Соус: барбекю
#    Начинка: бекон, ветчина, зелень, сыр моцарелла
# 3. Пицца: Дары моря | Цена: 550.00 р.
#    Тесто: пышное Соус: тар-тар
#    Начинка: кальмары, креветки, мидии, сыр моцарелла
# Для выбора укажите цифру через <ENTER>.
# Для отмены заказа введите -1
# Для подтверждения заказа введите 0
#
# 1
# Пицца Пепперони добавлена!
# 2
# Пицца Барбекю добавлена!
# 0
# Заказ подтвержен.
# Заказ №2
# 1. Пицца: Пепперони | Цена: 350.00 р.
#    Тесто: тонкое Соус: томатный
#    Начинка: пепперони, сыр моцарелла
# 2. Пицца: Барбекю | Цена: 450.00 р.
#    Тесто: тонкое Соус: барбекю
#    Начинка: бекон, ветчина, зелень, сыр моцарелла
# Сумма заказа: 800.00 р.
# Введите сумму: 1000
# Вы внесли 1000.00 р. Сдача: 200.00 р.
#
# Заказ поступил на выполнение...
# 1. Пепперони
# Начинаю готовить пиццу Пепперони
#   - замешиваю тонкое тесто...
#   - добавляю соус: томатный...
#   - и, конечно: пепперони, сыр моцарелла...
# Выпекаю пиццу... Готово!
# Нарезаю на аппетитные кусочки...
# Упаковываю в фирменную упаковку и готово!
# 2. Барбекю
# Начинаю готовить пиццу Барбекю
#   - замешиваю тонкое тесто...
#   - добавляю соус: барбекю...
#   - и, конечно: бекон, ветчина, зелень, сыр моцарелла...
# Выпекаю пиццу... Готово!
# Нарезаю на аппетитные кусочки...
# Упаковываю в фирменную упаковку и готово!
#
# Заказ №2 готов! Приятного аппетита!

