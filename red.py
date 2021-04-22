import time

low = True
total_price=0
while low:
    hello_world=input("Добро пожаловать в магазин 'Four small things'!\nПожалуйста, нажмите еденичку для начала шопинга! " )
    if hello_world=='1':
        print('1.Ручка 4в1\n2.Монета номиналом в 14 миллионов долларов\n3.Медуза!\n4.Бассейн для Вашей медузы')
        choice=input('Выбери товар, который тебе необходим ')
        if choice=='Ручка':
            quantity=int(input('Сколько нужно ручек? '))
            advertising='Продается щенок канадского лундерхунда! Добрый, кушает все, к лотку приучен. Заинтересовавшихся просьба звонить на номер +79086734663'
            while True:
                print('Проверяю наличие на складе...')
                time.sleep(2)
                print('Отправляю заказ менеджеру...')
                time.sleep(2)
                print('Заказ подвержден!')
                time.sleep(2)
                print(f'Поздравляем с покупкой отличной ручки 4 в 1 в количестве {quantity}\n{advertising}\nНужно оплатить всего лишь - {quantity*20}')
                total_price += quantity*20
                break
        elif choice=='Монета':
            quantity_1=int(input('Сколько монеток нужно, мой будущий миллионер? '))    
            while True:
                print('Проверяю наличие на складе...')
                time.sleep(2)
                print('Отправляю заказ менеджеру...')
                time.sleep(2)
                print('Заказ подвержден!')
                time.sleep(2)
                print(f'Поздравляем с покупкой монеток в количестве {quantity_1} Тебе осталось оплатить всего лишь: {quantity_1*14000000} ')
                total_price += quantity_1*14000000
                break
        elif choice=='Медуза':
            quantity_2=int(input('Сколько тебе медузок?' ))           
            while True:
                print('Проверяю наличие на складе...')
                time.sleep(2)
                print('Отправляю заказ менеджеру...')
                time.sleep(2)
                print('Заказ подвержден!')
                time.sleep(2)
                print(f'Поздравляю с покупкой существа без мозга..Надеюсь, ты не забудешь купить для нее бассейн. Кстати, с тебя {quantity_2*90} деняк\n Удачи!')
                total_price += quantity_2*90
                break
        elif choice=='Бассейн':
            quantity_3=int(input('Невероятно интересно узнать сколько бассейнов для медузок тебе нужно! Рассказывай'))
            while True:
                print('Проверяю наличие на складе...')
                time.sleep(2)
                print('Отправляю заказ менеджеру...')
                time.sleep(2)
                print('Заказ подвержден!')
                time.sleep(2)
                print(f'Хочу поздравить с покупкой бассейна для медузок! Это стоит всего лишь {quantity_3*105}\n Будем рады видеть Вас снова!')
                total_price += quantity_3*105
                break
        ex =input('Если хочешь выйти отсюда - нажми 0')
        if ex == '0':
            low = False   
    else:
        print('Кажется, ты нажал что-то невероятное...Тыкни на цифру один :)') 
print(f"Жду к оплате {total_price}!!!!")