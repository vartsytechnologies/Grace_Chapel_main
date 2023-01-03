import tkinter
from tkinter import *
import time
import tkinter.messagebox


class Place():
    def __init__(self,master):
        self.master = master
        self.master.geometry("450x450+400+100")
        self.master.title("Trial with Firebase")

        def submit():
            tkinter.messagebox.showerror("server "
                                         "error","ERROR 402 OCCURED")


        def page():
            self.label = Label(self.master,text = "Enter a Place",font = ("arial",15))
            self.label.pack()
            self.entry = Entry(self.master,font = ("arial",15))
            self.entry.pack(padx = 10,pady=10)
            self.button = Button(self.master,text="Submit",font = ("arial",15),command = submit)
            self.button.pack(padx=10,pady=10)
        page()

root = Tk()
obj = Place(root)
root.mainloop()