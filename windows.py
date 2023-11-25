from tkinter import *
from tkinter import ttk
import paperselection
import os


class Application(Frame):
    def __init__(self,root) -> None:
        super().__init__()
        self.master = root
        self.pack()
        self.envar = StringVar(None,"123")
        self.select = StringVar()
        root.geometry("500x300")
        self.window()
        if self.select.get() != '':
            self.window2()
 
    def selectorLinstener(self,*args):
        self.select.set(self.selection_get())



    def window(self):
        frame1  = Frame(self)

        path = os.getcwd()
        path = os.path.join(path,"Class_Materials")
        file_name_list = paperselection.get_courses(path)
        Label(frame1,text="Course").grid(row = 0, column= 0)
        self.selector=ttk.Combobox(frame1,width=40,height=len(file_name_list),values=file_name_list)
        self.selector.grid(row = 0, column = 1)
        self.selector.current(0)
        self.selector.bind('<<ComboboxSelected>>',self.selectorLinstener)

        frame1.pack()


    def window2(self):
        frame1 = Frame(self)

        path = os.path.join(path,self.select.get())
        file_paper_list = paperselection.get_courses(path)
        path = os.getcwd()
        path = os.path.join(path,"Class_Materials")
        file_name_list = paperselection.get_courses(path)
        Label(frame1,text="Course").grid(row = 0, column= 0)
        self.selector=ttk.Combobox(frame1,width=40,height=len(file_name_list),values=file_name_list)
        self.selector.grid(row = 0, column = 1)
        self.selector.current(0)
        self.selector.bind('<<ComboboxSelected>>',self.selectorLinstener)



'''
    def window(self):
        Label(self,text = "Hello World",width=10).grid(row = 0 ,column = 0)
        Entry(self,textvariable = self.envar).grid(row = 0, column = 1)
        text = Text(self)
        text.grid(columnspan = 2 , rowspan = 1, pady = 10, padx = 30)
        text.insert('end',"123")
'''

if __name__ == '__main__':
    root = Tk()
    application = Application(root = root)
    application.mainloop()

