from tkinter import *


def openFile():
    print("file has been opened")
def saveFile():
    print("file has been saved")
def cut():
    print("Yo cut ")
def copy():
    print("you copy") 
def paste():
    print("You paste")
window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='Save',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="edit",menu=editMenu)
editMenu.add_command(label="cut",command=cut)
editMenu.add_command(label="copy",command=copy)
editMenu.add_command(label='past',command=paste)


window.mainloop()