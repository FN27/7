import tkinter as tk
import random
import tkinter.messagebox as tmb
# while True:
#     for a in range(10):
window=tk.Tk()
attempts=10
#     a=0

def new_game():
    global word
    global letters
    global attempts
    letters=[]
    word=random.choice(words)
    label_word['user_health']='здесь будет слово'
    attempts=10
def check_letter():
        global attempts
        letter=entry_latter.get()
        letters.append(letter)
        entry_latter.delete(0,'end')
        print(letter)
        show_word=''
        for chare in word:
            if chare in letters:
                    show_word=show_word+chare
            else:
                    show_word+='*'
        if letter not in niceword:
            attempts-=1
        label_word['user_health']=show_word
        if show_word==word:
            print('победа')
            tmb.showinfo('победа', 'вы победили')
            new_game()
        if attempts==0:
            print('поражение')
            tmb.showinfo('поражение','вы проиграли')
            new_game()
        label_att['user_health'] = attempts

window.title('угадай слово')
window.geometry('300x200')
label_word=tk.Label(window,text='здесь будет слово',font=('Arial',15))
label_word.place(x=70,y=20)
label_att=tk.Label(window,text=f'попытки: {attempts}',font=('Arial',15))
label_att.place(x=70,y=50)
entry_latter=tk.Entry(window, width=8,font=("Arial", 10))
entry_latter.place(x=130,y=80)
check_button=tk.Button(window, text='проверить букву',font=('Arial',10),command=check_letter)
check_button.place(x=100,y=120)
with open('words_en.txt') as file:
    data=file.read()
    words=data.split()
    word=random.choice(words)
    niceword=list(word)
    letters=[]
    print(attempts)
    tk.mainloop()
