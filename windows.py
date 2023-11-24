from tkinter import *


class Application(Frame):
    def __init__(self,root) -> None:
        super().__init__()
        self.master = root
        self.pack()
        self.envar = StringVar(None,"123")
        self.window()

    def window(self):
        Label(self,text = "Hello World").pack()
        Entry(self,textvariable = self.envar).pack()
        text = Text(self)
        text.pack()
        text.insert('end',"123")

if __name__ == '__main__':
    root = Tk()
    application = Application(root = root)
    application.mainloop()

