import tkinter as tk

root=tk.Tk()

v=tk.IntVar()
v.set(2)

langu=[('Python',1),('Perl',2),('Java',3),('C++',4),('C',5)]

def ShowChoice():
    print(v.get())
tk.Label(root,text="""choice your favourite programming language:""",justify=tk.LEFT,padx=20).pack()
for val,langu in enumerate(langu):
    tk.Radiobutton(root,text=langu,indicatoron=0,width=10,padx=20,variable=v,command=ShowChoice,value=val).pack(anchor=tk.W)

root.mainloop()
