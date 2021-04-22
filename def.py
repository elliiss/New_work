# def ticket(price=5):
#     amount = int(input('Сколько вы хотите купить билетов? '))
#     return amount*price

# print(ticket(int(input("Билеты"))))

import random
import time

def display_intro():
    print('Ты - Шрек, спасающий Фиону.\nСейчас ты находишься между 2 башнями.\nВ одной башне тебя ждет Фиона.\nА в другой - дракон, который за секунду тебя испепелит.')

def choose_tower():
    sick=int(input('Выбери башню '))
    while sick!=1 and sick!=2:
        sick=int(input('Выбери башню '))
    return sick

def check_tower(chosenTower):
    print('Вы приближаетесь к башне..')
    time.sleep(2)
    print('Она тёмная и жуткая..')
    time.sleep(2)
    print('Перед тобой резко открывается дверь и из нее на тебя пристально смотрит...')
    print('---------------------------------')
    time.sleep(2)
    jode = random.randint(1,2)
    if jode==chosenTower:
        print('Ты спас Фиону!')
    else:
        print('Тебя сжёг дракон :(')

start_game='yes'
while start_game=='yes' or start_game=='y':
    display_intro()
    check_tower(choose_tower())
    start_game=input('Хочешь сыграть еще раз? ')

