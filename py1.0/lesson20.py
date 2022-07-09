import tkinter as tk

window=tk.Tk()
window.geometry('400x400')
entry=tk.Text(window,wrap='word')
entry.place(x=0,y=0,relwidth=1,relheight=1)
main_menu=tk.Menu(window)
window.configure(menu=main_menu)
file_menu=tk.Menu(main_menu)
main_menu.add_cascade(label='file',menu=file_menu)
window.mainloop()