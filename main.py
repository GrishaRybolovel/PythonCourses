from tkinter import *

root = Tk()
root.geometry("200x100")
root.title("Магазин")
storage = {"Сладкое" : [['Шоколад', '100']]}


def addItem():

    def putItem():
        if categoryGetter.get():
            if categoryGetter.get() not in storage:
                storage.update({categoryGetter.get() : []})
            storage[categoryGetter.get()].append([nameGetter.get(), costGetter.get()])
            window.destroy()
        print(*storage)


    window = Toplevel()

    nameLabel = Label(window, text="Введите название товара->")
    nameGetter = Entry(window)
    costLabel = Label(window, text="Введите цену товара->")
    costGetter = Entry(window)
    categoryLabel = Label(window, text="Введите категорию товара->")
    categoryGetter = Entry(window)


    nameLabel.grid(row=0, column=0)
    nameGetter.grid(row=0, column=1)
    costLabel.grid(row=1, column=0)
    costGetter.grid(row=1, column=1)
    categoryLabel.grid(row=2, column=0)
    categoryGetter.grid(row=2, column=1)

    btnGet = Button(window, text="Получить товар", command=putItem)
    btnExit = Button(window, text="Выйти", command=lambda: window.destroy())
    btnExit.grid(row=3, column=0)
    btnGet.grid(row=3, column=1)



def buyItem():
    window = Toplevel()

    def findByName():
        windowName = Toplevel()

        def getItem():
            for name in storage.keys():
                for i in range(len(storage[name])):
                    if storage[name][i][0] == getName.get():
                        storage.pop(name, storage[name][i])
                        windowName.destroy()



        label = Label(windowName, text="Введите название товара->")
        getName = Entry(windowName)
        btnGet = Button(windowName, text="Купить товар", command=getItem)
        btnExit = Button(windowName, text="Выйти", command=lambda: windowName.destroy())

        label.grid(row=0, column=0)
        getName.grid(row=0, column=1)
        btnGet.grid(row=1,column=1)
        btnExit.grid(row=1, column=0)



    def findByCategory():
        windowC = Toplevel()

        if storage.keys():
            for name in storage.keys():
                Label(windowC, text=f"Категория: {name}").pack()
                for item in storage[name]:
                    Label(windowC, text=item).pack()
        else:
            Label(windowC, text="Нет товаров!").pack()

        btnLeave = Button(windowC, text="Выйти", command=lambda: windowC.destroy())
        btnLeave.pack()



    btnFindByName = Button(window, text="Найти товар по названию", command=findByName)
    btnFindByCategory = Button(window, text="Показать товары", command=findByCategory)
    btnExit = Button(window, text="Выйти", command=lambda: window.destroy())

    btnFindByName.pack()
    btnFindByCategory.pack()
    btnExit.pack()


btnAddItem = Button(root, text="Пополнить магазин", command=addItem)
btnBuyItem = Button(root, text="Купить товар", command=buyItem)
btnExit = Button(root, text="Выйти", command=lambda: root.quit())

btnAddItem.pack()
btnBuyItem.pack()
btnExit.pack()

root.mainloop()