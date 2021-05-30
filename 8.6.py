from tkinter import *

def newfile():
    print('new file!')
def OpenFile():
    print('Open file!')
def InsText():
    print('Insert Text!')
def InsPic():
    print('Insert Picture!')
def about():
    print('this is simple example of a menu')
root=Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New',command=newfile)
filemenu.add_command(label='Open',command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

insertmenu=Menu(menu)
menu.add_cascade(label='Insert', menu=insertmenu)
insertmenu.add_command(label='Text',command=InsText)
insertmenu.add_command(label='Picture',command=InsPic)

helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About...',command=about)

mainloop()
