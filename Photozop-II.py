from PIL import Image, ImageTk, ImageDraw
from tkinter import Frame, Canvas, Button, Tk, filedialog


class Photoshop(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.createMenu()

    def inversion(self):
        self.draw = ImageDraw.Draw(self.image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()

        for x in range(self.width):
            for y in range(self.height):
                r = self.pix[x, y][0]
                g = self.pix[x, y][1]
                b = self.pix[x, y][2]
                self.draw.point((x, y), (255 - r, 255 - g, 255 - b))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.canvasImage, image=self.photo, anchor="nw")



    def grey(self):
        pass

    def increase(self):
        pass

    def decrease(self):
        pass

    def save(self):
        self.filename = filedialog.asksaveasfilename()
        self.image.save(self.filename + ".png")


    def createMenu(self):
        # Кнопка открытия
        self.btnOpen = Button(text="Открыть", height=2, width=12, command=self.open)
        self.btnOpen.place(x=20, y=60)

        self.btn_save = Button(text="Сохранить", height=2, width=12, command=self.save,
                               state='disabled')
        # Кнопка сохранения
        self.btn_save.place(x=20, y=105)
        self.canvas = Canvas(self.parent, width=400, height=400, bg="green")

        self.canvasImage = self.canvas.create_image(0, 0)
        self.canvas.pack()

        #
        self.btnInversion = Button(text="Инверсия", height=2, width=12,
                                   command=self.inversion, state='disabled')
        self.btnInversion.place(x=570, y=60)
        #
        self.btnGrey = Button(text="Оттенок серого", height=2, width=12,
                              command=self.grey, state='disabled')
        self.btnGrey.place(x=570, y=105)

        #
        self.btnIncrease = Button(text="Увеличить", height=2, width=12,
                                  command=self.increase, state='disabled')
        self.btnIncrease.place(x=570, y=150)

        #
        self.btnDecrease = Button(text="Уменьшить", height=2, width=12,
                                  command=self.decrease, state='disabled')
        self.btnDecrease.place(x=570, y=195)

    def open(self):
        self.filename = filedialog.askopenfilename()

        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.canvasImage, image=self.photo, anchor="nw")

        self.btn_save.configure(state="active")
        self.btnInversion.configure(state="active")


if __name__ == "__main__":
    root = Tk()
    root.title("Фотожоп")
    root.geometry("700x500")
    app = Photoshop(root)
    root.mainloop()
