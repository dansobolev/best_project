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
import json

def exit():
    root.destroy()


lst = []


def add():
    dictionary = {}
    dictionary["task"] = entry_task.get()
    dictionary["category"] = entry_category.get()
    dictionary['time'] = entry_time.get()

    lst.append(dictionary)


    writer(lst)

    #label_list_of_tasks.config(text=lst)
    #label_list_of_tasks.config(text=[{"sdf":123, "23":432}])



def show_list():

    try:
        button_delete_frame2.grid_remove()
        listbox_delete.grid_remove()
        text_list_of_tasks.grid()
        for todo in lst:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)
    except:
        for todo in lst:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            text_list_of_tasks.configure(state=DISABLED)




    # сначала присваивает значениу NORMAL атрибуту state для возможности добавления текста
    # после добавления текста изменяет значение на DISABLED для запрещения изменения
    """text_list_of_tasks.configure(state=NORMAL)
    text_list_of_tasks.insert(1.0, lst)
    text_list_of_tasks.configure(state=DISABLED)"""

def delete():
    for i in reversed(listbox_delete.curselection()):
        listbox_delete.delete(i)


def delete_task():
    global button_delete_frame2
    button_delete_frame2 = Button(frame2, text='Delete', command=delete)
    button_delete_frame2.grid()
    global listbox_delete

    text_list_of_tasks.grid_remove()
    listbox_delete = Listbox(frame2, selectmode=SINGLE, width=50)
    listbox_delete.grid(row=0, column=0, padx=1, pady=1)
    for todo in lst:
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


def filter_tasks():
    pass


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

text_list_of_tasks = Text(frame2, width=37, height=13)
text_list_of_tasks.grid(row=0, column=0, padx=1, pady=1)


"""#тестовый label для правого фрейма для вывода списка задач:
label_list_of_tasks = Label(frame2, width=37, height=13, background='white')
label_list_of_tasks.grid(row=0, column=0, padx=1, pady=2)"""


# левый фрейм:

label_task = Label(frame1, text='Задача: ', background='#D3D3D3')
label_task.grid(row=0,column=0, pady=1)

label_category = Label(frame1, text='Категория: ', background='#D3D3D3')
label_category.grid(row=1, column=0, pady=1)

label_time = Label(frame1, text='Время: ', background='#D3D3D3')
label_time.grid(row=2, column=0, pady=1)


entry_task = Entry(frame1, width=40)
entry_task.grid(row=0, column=1, padx=5, pady=1)


entry_category = Entry(frame1, width=40)
entry_category.grid(row=1, column=1)

entry_time = Entry(frame1, width=40)
entry_time.grid(row=2, column=1)


button_add = Button(frame1, text="Добавить", width=10, command=add)
button_add.grid(row=4,column=1, pady=1)

button_delete = Button(frame1, text="Удалить задачу", command=delete_task)
button_delete.grid(row=5, column=1)

button_filter = Button(frame1, text="Фильтр задач", command=filter_tasks)
button_filter.grid(row=6, column=1)

button_list_of_tasks = Button(frame1, text="Список задач", width=13, command=show_list)
button_list_of_tasks.grid(row=7,column=1, pady=1)

button_exit = Button(frame1, text="Выход", width=8, command=exit)
button_exit.grid(row=8,column=1, pady=1)


first_open_tasks()


# добавить функцию для фильтра по году или по алфавиту


root.resizable(width=False, height=False)# запрещает юзеру изменять размер окна

root.mainloop()



