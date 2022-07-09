import tkinter as tk
import random
import tkinter.messagebox as mbox

colors = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange', 'purple', 'brown', 'white']
times = 10


def instruction_button():
    mbox.showinfo('Brain Practise',
                  'Вам нужно писать название цвета надписи , после 10 раз вам покажут статистику и отценку, '
                  'а также время игры')


def new_word():
    label_word['user_health'] = random.choice(colors)
    label_word['font'] = ('Helvetica', 50)
    label_word['fg'] = random.choice(colors)


def check_by_button():
    global times
    user_word = text_write.get()
    game_word = label_word['fg']
    if user_word == game_word:
        print('правильно')
        times -= 1
    else:
        print('не правильно')
        times -= 1
    new_word()
    if times == 0:
        mbox.showinfo("Brain Practise", 'game end')
    text_write.delete(0, 'end')


def check_button_():
    global times
    user_word = text_write.get()
    game_word = label_word['fg']
    if user_word == game_word:
        print('правильно')
        times -= 1
    else:
        print('не правильно')
        times -= 1
    new_word()
    if times == 0:
        mbox.showinfo("Brain Practise", 'game end')
    text_write.delete(0, 'end')


window = tk.Tk()
window.title('Brain Practise')
window.geometry('600x600')
tick = tk.PhotoImage(file='tick.png')
cross = tk.PhotoImage(file='cross.png')
label_img = tk.Label(window, image=tick)
label_img.place(x=500, y=200)
label_word = tk.Label(window, text='Нажмите Enter и слово появится', font=('Helvetica', 20))
label_word.place(x=25, y=100)
text_write = tk.Entry(window, font=('Helvetica', 10))
text_write.place(x=25, y=200)
instruction = tk.Button(window, text='инструкция', command=instruction_button)
instruction.place(x=25, y=500)
check_button = tk.Button(window, text='enter', command=check_by_button)
check_button.place(x=169, y=198)
window.bind('<Return>', check_button_)
window.mainloop()
