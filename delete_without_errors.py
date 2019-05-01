from tkinter import *
import json
from tkinter import messagebox as mb

lst = []
lst_delete = []


def add():  # Функция добавления задачи
    dictionary = {}
    if entry_task.get() != '' and entry_category.get() != '' and entry_time.get() != '':
        dictionary["task"] = entry_task.get()
        dictionary["category"] = entry_category.get()  # Обработка всяких исключений если пользователь что-то не ввел
        dictionary['time'] = entry_time.get()  # Ипользуется встроенная библиотека вывода сообщений Messagebox
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


# text_list_of_tasks - это виджет Text
def show_list():  # Функция просмотра списка задач
    text_list_of_tasks.configure(state=NORMAL)  # Меняем конфигурацию для редактирования
    text_list_of_tasks.delete(1.0, END)  # удаляем содержимое
    try:
        button_ready_to_remove.place_forget()  # Размещаем кнопки и Text
        button_delete_frame2.place_forget()
        listbox_delete.grid_remove()
        text_list_of_tasks.grid()
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:  # считываем содержимое файла
            contents = json.load(json_file)
        for todo in contents:  # выводим построчно задачи
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)

    except:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + str(todo['task']) + " " + "Категория: " + str(todo[
                                                                                                          'category']) + " " + "Дата: " + str(
                todo['time']) + '\n')
            text_list_of_tasks.configure(state=DISABLED)


    text_list_of_tasks.configure(state=DISABLED) #снова меняем конфигурацию для запрещения редактирования


def delete():  # функция удаления задач из окна tkinter
    for i in reversed(listbox_delete.curselection()):  # просматриваем выбранные пользователем задачи на удаление
        listbox_delete.delete(i)
        lst_delete.append(i) #добавляем выбранные пользователем задачи в список на удаление


def ready_to_delete(): # функция удаления задач из файла
    global lst_delete

    with open('todo_list.json', 'r', encoding='cp1251') as json_file: #считываем данные из файла
        contents = json.load(json_file)
    for i in sorted(lst_delete, reverse=True): #сортируем список для корректного удаления
        contents.pop(i) #удаляем данные из файла функцией pop()

    with open('todo_list.json', 'w') as file_output_json:
        json.dump(contents, file_output_json) #перезаписываем файл уже без удаленных задач
    lst_delete = []


def delete_task(): #окно переключения на панель удаления задач
    global listbox_delete
    global button_delete_frame2
    listbox_delete.delete(0, END) #при открытии окна удаляет все записи, который там могут находиться
    button_delete_frame2.place(x=50, y=25)
    button_ready_to_remove.place(x=180, y=25)
    text_list_of_tasks.grid_remove() #скрывает окно списка задач
    listbox_delete.grid(row=0, column=0, padx=1, pady=1)
    with open('todo_list.json', 'r', encoding='cp1251') as json_file: #считывание файла
        contents = json.load(json_file)
    for todo in contents:
        listbox_delete.insert(END, "Задача: " + todo['task'] + " " + "Категория: " + todo['category'] + " " + "Дата: " +
                              todo['time'] + '\n') #получения данных из файла и вывод на экран


def writer(something): #функция для записи заметок в список contents и добавления их в файл todo_list.json
    try:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for i in something:
            contents.append(i)
    except Exception as ex:
        print(ex)

    try:
        with open('todo_list.json', 'w', encoding='windows-1251') as file_write:
            json.dump(contents, file_write, sort_keys=False, ensure_ascii=False)
    except Exception as e:
        print(e)


def first_open_tasks(): #функция срабатывает при открытии приложения, нужна для вывода задач в окно шоу листа,
                        #если какие-то задачи сохранились в файле
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


def exit1(): #функция выхода из программы, перед выходом повтороно спрашивает пользователя
    answer = mb.askyesno(title='Внимание!', message='Вы точно хотите выйти из программы?')
    if answer == True:
        root.destroy()
    else:
        pass


root = Tk() #главное окно tkinter'a
root.title("Менеджер задач")
root.geometry('640x200')
frame1 = Frame(root, width=320, height=120, background="#2F2F2F")  # default color was #D3D3D3
frame2 = Frame(root, width=320, height=80, background="#2F2F2F")  # default color was #D3D3D3

# ФРЕЙМ ДЛЯ НОРМАЛЬНОГО РАСПОЛОЖЕНИЯ КНОПОК
frame3 = Frame(root, width=320, height=131, background="#2F2F2F")
frame4 = Frame(root, width=320, height=70, background="#2F2F2F")

frame1.place(x=0, y=0)
frame2.place(x=320, y=0)
frame3.place(x=0, y=69)
frame4.place(x=320, y=130)

# label1 = Label(frame1, background='purple', text='coooool').grid()
# label2 = Label(frame2, background='purple', text='coooool').grid()

# фрейм вывода списка задач:
# ширина одного фрейма = 160
# высота равна 115

text_list_of_tasks = Text(frame2, width=48, height=10)
text_list_of_tasks.grid(row=0, column=0, padx=1, pady=1)
text_list_of_tasks.configure(state=DISABLED)

"""#тестовый label для правого фрейма для вывода списка задач:
label_list_of_tasks = Label(frame2, width=37, height=13, background='white')
label_list_of_tasks.grid(row=0, column=0, padx=1, pady=2)"""

# левый фрейм:

label_task = Label(frame1, text='Задача: ', fg='white', bg="#2F2F2F")
label_task.grid(row=0, column=0, pady=1)

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
button_add.place(x=50, y=25)

button_delete = Button(frame3, text="Удалить задачу", width=13, command=delete_task, bg='#474747', fg='white',
                       activebackground='#BFB173', relief='raised')
button_delete.place(x=50, y=55)

button_list_of_tasks = Button(frame3, text="Список задач", width=13, command=show_list, bg='#474747', fg='white',
                              activebackground='#BFB173', relief='raised')
button_list_of_tasks.place(x=180, y=25)

button_exit = Button(frame3, text="Выход", width=13, command=exit1, bg='#474747', fg='white',
                     activebackground='#610303', relief='raised')
button_exit.place(x=180, from tkinter import *
import json
from tkinter import messagebox as mb

lst = []
lst_delete = []


def add():  # Функция добавления задачи
    lst = [] #обнуляем список lst для того, чтобы удаленные задачи снова не появлялись в спике lst
    dictionary = {}
    if entry_task.get() != '' and entry_category.get() != '' and entry_time.get() != '':
        dictionary["task"] = entry_task.get()
        dictionary["category"] = entry_category.get()  # Обработка всяких исключений если пользователь что-то не ввел
        dictionary['time'] = entry_time.get()  # Ипользуется встроенная библиотека вывода сообщений Messagebox
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


# text_list_of_tasks - это виджет Text
def show_list():  # Функция просмотра списка задач
    text_list_of_tasks.configure(state=NORMAL)  # Меняем конфигурацию для редактирования
    text_list_of_tasks.delete(1.0, END)  # удаляем содержимое
    try:
        button_ready_to_remove.place_forget()  # Размещаем кнопки и Text
        button_delete_frame2.place_forget()
        listbox_delete.grid_remove()
        text_list_of_tasks.grid()
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:  # считываем содержимое файла
            contents = json.load(json_file)
        for todo in contents:  # выводим построчно задачи
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)

    except:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + str(todo['task']) + " " + "Категория: " + str(todo[
                                                                                                          'category']) + " " + "Дата: " + str(
                todo['time']) + '\n')
            text_list_of_tasks.configure(state=DISABLED)


    text_list_of_tasks.configure(state=DISABLED) #снова меняем конфигурацию для запрещения редактирования


def delete():  # функция удаления задач из окна tkinter
    for i in reversed(listbox_delete.curselection()):  # просматриваем выбранные пользователем задачи на удаление
        listbox_delete.delete(i)
        lst_delete.append(i) #добавляем выбранные пользователем задачи в список на удаление


def ready_to_delete(): # функция удаления задач из файла
    global lst_delete

    with open('todo_list.json', 'r', encoding='cp1251') as json_file: #считываем данные из файла
        contents = json.load(json_file)
    for i in sorted(lst_delete, reverse=True): #сортируем список для корректного удаления
        contents.pop(i) #удаляем данные из файла функцией pop()

    with open('todo_list.json', 'w') as file_output_json:
        json.dump(contents, file_output_json) #перезаписываем файл уже без удаленных задач
    lst_delete = []

    show_list() #при нажатии на кнопку "Готово" в окне удаление заметок сразу делается переход на окно show list


def delete_task(): #окно переключения на панель удаления задач
    try:
        global listbox_delete
        global button_delete_frame2
        listbox_delete.delete(0, END) #при открытии окна удаляет все записи, который там могут находиться
        button_delete_frame2.place(x=50, y=25)
        button_ready_to_remove.place(x=180, y=25)
        text_list_of_tasks.grid_remove() #скрывает окно списка задач
        listbox_delete.grid(row=0, column=0, padx=1, pady=1)
        with open('todo_list.json', 'r', encoding='cp1251') as json_file: #считывание файла
            contents = json.load(json_file)
        for todo in contents:
            listbox_delete.insert(END, "Задача: " + todo['task'] + " " + "Категория: " + todo['category'] + " " + "Дата: " +
                                todo['time'] + '\n') #получения данных из файла и вывод на экран
    except Exception as ex:
        print(ex)

def writer(something): #функция для записи заметок в список contents и добавления их в файл todo_list.json
    try:
        with open('todo_list.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for i in something:
            contents.append(i)
    except Exception as ex:
        print(ex)

    try:
        with open('todo_list.json', 'w', encoding='windows-1251') as file_write:
            json.dump(contents, file_write, sort_keys=False, ensure_ascii=False)
    except Exception as e:
        print(e)


def first_open_tasks(): #функция срабатывает при открытии приложения, нужна для вывода задач в окно шоу листа,
                        #если какие-то задачи сохранились в файле
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


def exit1(): #функция выхода из программы, перед выходом повтороно спрашивает пользователя
    answer = mb.askyesno(title='Внимание!', message='Вы точно хотите выйти из программы?')
    if answer == True:
        root.destroy()
    else:
        pass


root = Tk() #главное окно tkinter'a
root.title("Менеджер задач")
root.geometry('640x200')
frame1 = Frame(root, width=320, height=120, background="#2F2F2F")  # default color was #D3D3D3
frame2 = Frame(root, width=320, height=80, background="#2F2F2F")  # default color was #D3D3D3

# ФРЕЙМ ДЛЯ НОРМАЛЬНОГО РАСПОЛОЖЕНИЯ КНОПОК
frame3 = Frame(root, width=320, height=131, background="#2F2F2F")
frame4 = Frame(root, width=320, height=70, background="#2F2F2F")

frame1.place(x=0, y=0)
frame2.place(x=320, y=0)
frame3.place(x=0, y=69)
frame4.place(x=320, y=130)


text_list_of_tasks = Text(frame2, width=48, height=10)
text_list_of_tasks.grid(row=0, column=0, padx=1, pady=1)
text_list_of_tasks.configure(state=DISABLED)


# левый фрейм:

label_task = Label(frame1, text='Задача: ', fg='white', bg="#2F2F2F")
label_task.grid(row=0, column=0, pady=1)

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
button_add.place(x=50, y=25)

button_delete = Button(frame3, text="Удалить задачу", width=13, command=delete_task, bg='#474747', fg='white',
                       activebackground='#BFB173', relief='raised')
button_delete.place(x=50, y=55)

button_list_of_tasks = Button(frame3, text="Список задач", width=13, command=show_list, bg='#474747', fg='white',
                              activebackground='#BFB173', relief='raised')
button_list_of_tasks.place(x=180, y=25)

button_exit = Button(frame3, text="Выход", width=13, command=exit1, bg='#474747', fg='white',
                     activebackground='#610303', relief='raised')
button_exit.place(x=180, y=55)

button_delete_frame2 = Button(frame4, text='Удалить', width=13, activebackground='#BFB173', bg='#474747', fg='white',
                              command=delete)
button_delete_frame2.place()
button_delete_frame2.place_forget()

button_ready_to_remove = Button(frame4, text='Готово', width=13, activebackground='#BFB173', bg='#474747', fg='white',
                                command=ready_to_delete)
button_ready_to_remove.place()
button_ready_to_remove.place_forget()

listbox_delete = Listbox(frame2, selectmode=SINGLE, width=53, highlightcolor='white', bg='white',
                         selectbackground='#2F2F2F')
listbox_delete.grid(row=0, column=0)
listbox_delete.grid_remove()

first_open_tasks()


root.resizable(width=False, height=False)  # запрещает юзеру изменять размер окна

root.mainloop()y=55)

button_delete_frame2 = Button(frame4, text='Удалить', width=13, activebackground='#BFB173', bg='#474747', fg='white',
                              command=delete)
button_delete_frame2.place()
button_delete_frame2.place_forget()

button_ready_to_remove = Button(frame4, text='Готово', width=13, activebackground='#BFB173', bg='#474747', fg='white',
                                command=ready_to_delete)
button_ready_to_remove.place()
button_ready_to_remove.place_forget()

listbox_delete = Listbox(frame2, selectmode=SINGLE, width=53, highlightcolor='white', bg='white',
                         selectbackground='#2F2F2F')
listbox_delete.grid(row=0, column=0)
listbox_delete.grid_remove()

first_open_tasks()


root.resizable(width=False, height=False)  # запрещает юзеру изменять размер окна

root.mainloop()