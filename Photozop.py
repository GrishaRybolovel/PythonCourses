from PIL import Image, ImageTk
from tkinter import Frame, Canvas, Button, Tk, filedialog



class Photoshop(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.createMenu()

    def createMenu(self):
        self.btnOpen = Button(text="Открыть", command=self.open)
        self.btnOpen.place(x=30, y=200)
        self.canvas = Canvas(self.parent, width=400, height=400, bg="green")
        self.canvasImage = self.canvas.create_image(0, 0)
        self.canvas.pack()

    def open(self):
        self.filename = filedialog.askopenfilename()

        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.canvasImage, image=self.photo, anchor="nw")
        self.canvas.configure(width=self.photo.width(), height=self.photo.height())






if __name__ == "__main__":
    root = Tk()
    root.title("Фотожоп")
    root.geometry("700x500")
    app = Photoshop(root)
    root.mainloop()
