from tkinter import *
import json
from tkinter import messagebox as mb

lst = []

def add():
    dictionary = {}
    if entry_task.get() != '' and entry_category.get() != '' and entry_time.get() != '':
        dictionary["task"] = entry_task.get()
        dictionary["category"] = entry_category.get()
        dictionary['time'] = entry_time.get()
        lst.append(dictionary)
        writer(lst)
    elif entry_task.get() == '' and entry_category.get() != '' and entry_time.get() != '':
        mb.showerror("Ошибка", "Вы не ввели задачу")
    elif entry_task.get() != '' and entry_category.get() == '' and entry_time.get() != '':
        mb.showerror("Ошибка", "Вы не ввели категорию")
    elif entry_task.get() != '' and entry_category.get() != '' and entry_time.get() == '':
        mb.showerror("Ошибка", "Вы не ввели время")
    elif entry_task.get() == '' and entry_category.get() == '' and entry_time.get() != '':
        mb.showerror("Ошибка", "Вы не ввели задачу и категорию")
    elif entry_task.get() != '' and entry_category.get() == '' and entry_time.get() == '':
        mb.showerror("Ошибка", "Вы не ввели категорию и время")
    elif entry_task.get() == '' and entry_category.get() != '' and entry_time.get() == '':
        mb.showerror("Ошибка", "Вы не ввели задачу и время")
    else:
        mb.showerror("Ошибка", "Вы ничего не ввели")



    #label_list_of_tasks.config(text=lst)
    #label_list_of_tasks.config(text=[{"sdf":123, "23":432}])

def show_list():

    try:
        button_delete_frame2.grid_remove()
        listbox_delete.grid_remove()
        text_list_of_tasks.grid()
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in content:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)
           
    except:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)




    # сначала присваивает значениe NORMAL атрибуту state для возможности добавления текста
    # после добавления текста изменяет значение на DISABLED для запрещения изменения
    """text_list_of_tasks.configure(state=NORMAL)
    text_list_of_tasks.insert(1.0, lst)
    text_list_of_tasks.configure(state=DISABLED)"""

def delete():
    for i in reversed(listbox_delete.curselection()):
        listbox_delete.delete(i)
        text_list_of_tasks.configure(state=NORMAL)
        text_list_of_tasks.delete(1.0, END)
        text_list_of_tasks.configure(state=DISABLED)
        
def delete_task():
    global button_delete_frame2
    
    button_delete_frame2.grid()

    global listbox_delete
    text_list_of_tasks.grid_remove()
    listbox_delete = Listbox(frame2, selectmode=SINGLE, width=50)
    listbox_delete.grid(row=0, column=0, padx=1, pady=1)
    with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
    for todo in contents:
        listbox_delete.insert(END, "Задача: " + todo['task'] + " " + "Категория: " + todo['category'] + " " + "Дата: " +
                              todo['time'] + '\n')


def writer(something):
    try:
        with open('todo_list.json', 'w', encoding='windows-1251') as file_write:
            json.dump(something, file_write, sort_keys=False, ensure_ascii=False)
    except Exception as e:
        print(e)


def first_open_tasks():
    try:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)
    except Exception as ex:
        print(ex)

def exit():
    root.destroy()

root = Tk()
root.title("Менеджер задач")

frame1 = Frame(root, width=320, height=70,  background="#2F2F2F") #default color was #D3D3D3
frame2 = Frame(root, width=320, height=231, background="#2F2F2F") #default color was #D3D3D3

#ФРЕЙМ ДЛЯ НОРМАЛЬНОГО РАСПОЛОЖЕНИЯ КНОПОК
frame3 = Frame(root, width=320, height=161, background="#2F2F2F")

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1, rowspan=2)
frame3.grid(row=1, column=0)

frame1.grid_propagate(0)
frame2.grid_propagate(0)
frame3.grid_propagate(0)

# label1 = Label(frame1, background='purple', text='coooool').grid()
# label2 = Label(frame2, background='purple', text='coooool').grid()

# фрейм вывода списка задач:
# ширина одного фрейма = 160
# высота равна 115

text_list_of_tasks = Text(frame2, width=39, height=14)
text_list_of_tasks.grid(row=0, column=0, padx=1, pady=1)


"""#тестовый label для правого фрейма для вывода списка задач:
label_list_of_tasks = Label(frame2, width=37, height=13, background='white')
label_list_of_tasks.grid(row=0, column=0, padx=1, pady=2)"""


# левый фрейм:

label_task = Label(frame1, text='Задача: ', fg='white', bg="#2F2F2F")
label_task.grid(row=0,column=0, pady=1)

label_category = Label(frame1, text='Категория: ', fg='white', bg="#2F2F2F")
label_category.grid(row=1, column=0, pady=1)

label_time = Label(frame1, text='Время: ', fg='white', bg="#2F2F2F")
label_time.grid(row=2, column=0, pady=1)


entry_task = Entry(frame1, width=40)
entry_task.grid(row=0, column=1, padx=5, pady=1)


entry_category = Entry(frame1, width=40)
entry_category.grid(row=1, column=1)

entry_time = Entry(frame1, width=40)
entry_time.grid(row=2, column=1)


button_add = Button(frame3, text="Добавить", width=13, command=add, bg='#474747', fg='white',
                    activebackground='#BFB173', relief='raised')
#button_add.grid(row=4,column=1, pady=1)
button_add.place(x=50, y=25)

button_delete = Button(frame3, text="Удалить задачу", width=13, command=delete_task, bg='#474747', fg='white',
                    activebackground='#BFB173', relief='raised')
#button_delete.grid(row=5, column=1)
button_delete.place(x=50, y=55)



button_list_of_tasks = Button(frame3, text="Список задач", width=13, command=show_list, bg='#474747', fg='white',
                    activebackground='#BFB173', relief='raised')
#button_list_of_tasks.grid(row=7,column=1, pady=1)
button_list_of_tasks.place(x=180, y=25)

button_exit = Button(frame3, text="Выход", width=13, command=exit,  bg='#474747', fg='white',
                     activebackground='#610303', relief='raised')
#button_exit.grid(row=8,column=1, pady=1)
button_exit.place(x=180, y=55)

button_delete_frame2 = Button(frame2, text='Delete', command=delete)
button_delete_frame2.grid_remove()


first_open_tasks()


# добавить функцию для фильтра по году или по алфавиту


root.resizable(width=False, height=False)# запрещает юзеру изменять размер окна

root.mainloop()
