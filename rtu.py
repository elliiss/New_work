#import time
#a=0
#while True:
#    a+=1
#   print(a)
#   print('Ждём 3 секунды...')
#   time.sleep(3)
#   if a > 3:
#       break
# print('Ждём последние 5 секунд...')
#time.sleep(10)

import sys


products = [{"Вода питьевая": [1, 10.50]},
            {"Вода газированная": [2, 13.50]},
            {"Огненная вода": [3, 15.00]}]
basket = []
check = 0


def show_menu():
    if len(products) > 0:
        for product in products:
            for name, data in product.items():
                print(f"{data[0]}. {name} — {data[1]}")
                print("----------------------------")

    else:
        print("Товара нет")


def purchase(tovar):
    hi_index = len(products) + 1
    try:
        if tovar == 0 or tovar > hi_index:
            print(f"Кажется,этого нет в меню. Попробуйте ввести цифру от 1 до {hi_index}")
        else:
            for product in products:
                for name, data in product.items():
                    if data[0] == tovar:
                        basket.append(product)
                        return data, name
    except EOFError:
        print(f"Попробуйте ввести цифру от 1 до {hi_index}")


def by_menu():
    tovar = int(input("Введите номер желаемой покупки: "))
    data, name = purchase(tovar)

    kolichestvo = float(input("Желаемое колличество: "))
    price = data[1]
    data.append(kolichestvo)

    print(f" Вы выбрали: {name} — {kolichestvo}шт \nОбщая стоимость — {kolichestvo * price} ")
    print("\n")


def get_order():
    o_sum = 0
    if len(basket) > 0:
        for product in basket:
            for name, data in product.items():
                print("\n")
                print(f"{data[0]}. {name} * {data[2]} -- {data[1] * data[2]}")
                print("----------------------------")
                o_sum += data[1] * data[2]
        print(f"Итого ——— {o_sum}")
        print("\n")
        print("Спасибо за покупку!")
    else:
        print("Корзина пуста")


if name == '__main__':
    print("Добро пожаловать в магазин ' У Лизоньки <<24/7>> ' \n")

    T = True
    while T:
        i = input("Введите '0' для выхода\n"
                  "Введите '1' чтобы перейти к товарам:\n"
                  "Введите '2', чтобы оформить заказ\n\n"
                  ">>>>>")
        if i == "1":
            show_menu()
            by_menu()

        elif i == "0":
            sys.exit()

        elif i == "2":
            get_order()

        else:
            print("Ошибка ввода :(")