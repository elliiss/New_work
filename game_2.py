# def summary():
#     frst = int(input('Введи число '))
#     summary = 0
#     while (frst !=0):
#         summary = summary + frst % 10
#         frst =  frst // 10
#     print('Сумма цифр числа равно:', summary)

# def perem():
#     test = int(input('Первая переменная '))
#     test_1 = int(input('Вторая переменная '))
#     test = test + test_1  #20+10=30
#     test_1 = test - test_1 #30-10=20
#     test = test - test_1 #30-20 = 10
#     print(test, test_1)

# def my_index():
#     a = [1, -1, 2, 3, 5, -8, 13, 21, -34, 56, 89]
#     print(a[1], a[5])

# def at_list():
#     my_list = [1000, 100, 299, 90]
#     my_list_g = [100, 679, 90, 233,1000]
#     my_listp
#     list(set(my_list_g).difference(my_list))


# import Canvas
# def draw_state(game_state):
#     canvas.line_width(1)
#     canvas.set_color('grey') #рисуем поле для игры
#     canvas.move_to(116, 0) #рисуем вертикальные линии
#     canvas.line_to(116, 350)
#     canvas.move_to(233, 0)
#     canvas.line_to(233, 350)
#     canvas.move_to(0, 116) #рисуем горизонтальные линии
#     canvas.line_to(350, 116)
#     canvas.move_to(0, 233)
#     canvas.line_to(350, 233)
#     for index, value in enumerate(game_state):
#         x = (index % 3) * 116
#         y = (index // 3) * 116
#         if value == 'x':
#             draw_x(x, y)
#         if value == 'o':
#             draw_o(x, y)
#     canvas.draw()

# def draw_x(x, y): #рисуем 'x'
#     canvas.line_width(6)
#     canvas.set_color('skyblue')
#     canvas.move_to(20 + x, 20 + y)
#     canvas.line_to(96 + x, 96 + y)
#     canvas.move_to(96 + x, 20 + y)
#     canvas.line_to(20 + x, 96 + y)
# def draw_o(x, y): #рисуем 'o'
#     canvas.line_width(6)
#     canvas.set_color('green')
#     canvas.circle(60 + x, 60 + y, 30)

# GAME_STATE = ["x", None, None, "x", "o", None, None, None, "o"]
# draw_state(GAME_STATE)



board = list(range(1, 10))

def draw_board(board):
    for i in range(3):
        print('=================')
        print('||',board[0+i*3],'||', board[1+i*3],'||', board[2+i*3],'||')
        print('=================')
        
        
 
def play(xo):
    correct = False
    while not correct:
        answer = input(f"Куда поставим {xo}?")
        try:
            answer = int(answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число? ")
            continue  #запустить цикл сноаа сначала
        if 1 <= answer <=9:
            if str(board[answer-1]) !="X" and str(board[answer-1]) != "O":
                board[answer-1] = xo
                correct = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Некорректный ввод, Введите число от 1 до 9 чтобы походить.")
   
   
def check_win(board):
    help = ((0,1,2), (3,4,5), (6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in help:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
        return False

 
def main(board):
    rest = 0
    win = False
    while not win:
        draw_board(board)
        if rest %2 ==0:
            play("X")
        else: 
            play("O")
        rest +=1
        if rest > 4:
            if str(check_win(board)) != "False":
                print(check_win(board), "Выйграл!")
                win = True
                break
        if rest ==9:
            print("Ничья")
            win = True
            break
   
main(board)