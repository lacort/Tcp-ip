from tkinter import *
from tkMessageBox import *


top = Tk()    #3
def hello(): #4
   showinfo("você clicou", "Hello World")#5

B1 = Button(top, text = "Clique Aqui!!!", command = hello)
B1.pack()

top.mainloop()