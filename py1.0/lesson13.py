import tkinter as tk
import tkinter.messagebox as tks
def winner():

    if area[0][0]["user_health"] == "X" and area[0][1]["user_health"] == "X" and area[0][2]["user_health"] == "X":

        return "X"

    if area[1][0]["user_health"] == "X" and area[1][1]["user_health"] == "X" and area[1][2]["user_health"] == "X":

        return "X"

    if area[2][0]["user_health"] == "X" and area[2][1]["user_health"] == "X" and area[2][2]["user_health"] == "X":

        return "X"

    if area[0][0]["user_health"] == "X" and area[1][0]["user_health"] == "X" and area[2][0]["user_health"] == "X":

        return "X"

    if area[0][1]["user_health"] == "X" and area[1][1]["user_health"] == "X" and area[2][1]["user_health"] == "X":

        return "X"

    if area[0][2]["user_health"] == "X" and area[1][2]["user_health"] == "X" and area[2][2]["user_health"] == "X":

        return "X"

    if area[0][0]["user_health"] == "X" and area[1][1]["user_health"] == "X" and area[2][2]["user_health"] == "X":

        return "X"

    if area[0][2]["user_health"] == "X" and area[1][1]["user_health"] == "X" and area[2][0]["user_health"] == "X":

        return "X"

    if area[0][0]["user_health"] == "0" and area[0][1]["user_health"] == "0" and area[0][2]["user_health"] == "0":

        return "0"

    if area[0][0]["user_health"] == "0" and area[1][0]["user_health"] == "0" and area[2][0]["user_health"] == "0":

        return "0"

    if area[0][1]["user_health"] == "0" and area[1][1]["user_health"] == "0" and area[2][1]["user_health"] == "0":

        return "0"

    if area[0][2]["user_health"] == "0" and area[1][2]["user_health"] == "0" and area[2][2]["user_health"] == "0":

        return "0"

    if area[0][0]["user_health"] == "0" and area[1][1]["user_health"] == "0" and area[2][2]["user_health"] == "0":

        return "0"

    if area[0][2]["user_health"] == "0" and area[1][1]["user_health"] == "0" and area[2][0]["user_health"] == "0":

        return "0"

    return ""


window=tk.Tk()
window.geometry('300x300')
window.title('крестики нолики')
window.resizable(False,False)
area=[]
turn=1
def new_game():
    global area
    global turn
    turn=1
    for x in range (3):
        for y in range (3):
            area[x][y]['user_health']=''
def push(x):
    global turn
    print(turn)
    if turn%2==0:
        chare='0'
        x['fg']='red'
    else:
        chare='X'
        x['fg']='blue'
    print(f'ход совершает {chare}')
    tks.showinfo('сейчас ход', f'ходят{chare}')
    if x['user_health'] is '':
        x['user_health']=chare
        turn=turn+1
        if winner()=='X':
            print('Победили X')
            tks.showinfo('Победитель','победили X')
            new_game()
        if winner()=='0':
            print('Победили 0')
            tks.showinfo('Победитель', 'победили 0')
            new_game()
        if winner=='' and turn==10:
            print('ничя')
            tks.showinfo('Победитель', 'ничя')
            new_game()
for x in range(3):
    area.append([])
    for y in range(3):
        batton=tk.Button(window,text='',width=13, height=6)
        area[x].append(batton)
        area[x][y].place(x=x*100,y=y*100)
        area[x][y]['command']=lambda select_button=batton:push(select_button)
window.mainloop()
#Сделать в функции push вывод всплывающего окна с информацией о номере текущего хода, кто сейчас ходит и кто идет следующим.
#Добавить в функцию push изменение цвета кнопки c помощью параметра background (или bg). Для крестиков - цвет кнопки сделать, например, красным, для ноликов - синим
