def check_winner():

    if area[0][0] == "x" and area[0][1] == "x" and area[0][2] == "x":

        return "x"

    if area[1][0] == "x" and area[1][1] == "x" and area[1][2] == "x":

        return "x"

    if area[2][0] == "x" and area[2][1] == "x" and area[2][2] == "x":

        return "x"

    if area[0][0] == "x" and area[1][0] == "x" and area[2][0] == "x":

        return "x"

    if area[0][1] == "x" and area[1][1] == "x" and area[2][1] == "x":

        return "x"

    if area[0][2] == "x" and area[1][2] == "x" and area[2][2] == "x":

        return "x"

    if area[0][0] == "x" and area[1][1] == "x" and area[2][2] == "x":

        return "x"

    if area[0][2] == "x" and area[1][1] == "x" and area[2][0] == "x":

        return "x"

    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":

        return "0"

    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":

        return "0"

    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":

        return "0"

    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":

        return "0"

    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":

        return "0"

    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":

        return "0"

    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":

        return "0"

    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":

        return "0"

    return "*"
arie=[['*','*','*'],['*','*','*'],['*','*','*']]
#arie[0][0]='x'
#arie[2]='o'
for turn in range(1,10):
    print('Вводить числа: 0,1,2 ')
    print (f'сейчас {turn} ход')
    if turn %2==0:
        chare='0'
        print(f'сейчас ход {chare}')
    else:
        chare='x'
        print(f'Сейчас ход {chare}')
    for game in arie:
        print(game)
    a=input('Введите номер строки')
    a=int(a)
    b=input("Введите номер столбца")
    b=int(b)
    arie[a][b]=chare
    if check_winner()=='x':
        print('победа x')
        break
    elif check_winner()=='0':
        print('победа o')
        break
    elif turn==9 and check_winner()=='*':
        print('Ничя')
        #Придумать, как
            решить
            проблему
            неудобного
            ввода
            номеров
            строк
            и
            столбцов, чтобы
            пользователь
            мог
            вводить
            не
            0, 1
            и
            2, а
            1, 2
            и
            3.
            повторить
            функции, списки.

