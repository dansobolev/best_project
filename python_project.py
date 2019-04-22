'''from tkinter import *
window = Tk()
window.title("Менеджер задач")
window.geometry('450x230')


frame1 = Frame(window, background='black').pack()

"""label1 = Label(text='Задача: ').grid(row=0, column=0)
label2 = Label(text="Категория: ").grid(row=1, column=0)
label3 = Label(text='Время:').grid(row=2, column=0)

entry1 = Entry().grid(row=0, column=1)
entry2 = Entry().grid(row=1, column=1)
entry3 = Entry().grid(row=2, column=1)

Entry1 = Entry(text='attempt').grid(row=0,column=3)"""





window.resizable(width=False, height=False) # запрещает юзеру изменять размер окна

window.mainloop()'''
from tkinter import *

def exit():
    root.destroy()


root = Tk()
root.title("Менеджер задач")

frame1 = Frame(root, width=320, height=230, background="#D3D3D3")
frame2 = Frame(root, width=320, height=230, background="#D3D3D3")

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)

frame1.grid_propagate(0)
frame2.grid_propagate(0)

# label1 = Label(frame1, background='purple', text='coooool').grid()
# label2 = Label(frame2, background='purple', text='coooool').grid()

# фрейм вывода списка задач:
# ширина одного фрейма = 160
# высота равна 115

text_list_of_tasks = Text(frame2, width=37, height=13).grid(row=0, column=0, padx=1, pady=1)

# левый фрейм:

label_task = Label(frame1, text='Задача: ', background='#D3D3D3').grid(row=0,column=0, pady=1)
label_category = Label(frame1, text='Категория: ', background='#D3D3D3').grid(row=1, column=0, pady=1)
label_time = Label(frame1, text='Время: ', background='#D3D3D3').grid(row=2, column=0, pady=1)

entry_task = Entry(frame1, width=40).grid(row=0, column=1, padx=5, pady=1)
entry_category = Entry(frame1, width=40).grid(row=1, column=1)
entry_time = Entry(frame1, width=40).grid(row=2, column=1)

button_add = Button(frame1, text="Добавить", width=10).grid(row=4,column=1, pady=1)
button_list_of_tasks = Button(frame1, text="Список задач", width=13).grid(row=5,column=1, pady=1)
button_exit = Button(frame1, text="Выход", width=8, command=exit).grid(row=6,column=1, pady=1)



root.resizable(width=False, height=False) # запрещает юзеру изменять размер окна

root.mainloop()



