import tkinter
import random

colours=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score=0
timeleft=120

def startGame(event):
    if timeleft==120:
        countdown()
    nextColour()
def nextColour():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=2
        else:
            score-=1
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]),text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft-=1
        timeLabel.config(text="Time left" + str(timeleft))
        timeLabel.after(1000,countdown)
root=tkinter.Tk()
root.title("color game")
root.geometry("370x200")
instruction=tkinter.Label(root,text="Type in the colour" "of the words, and not the word text!",font=('Helvetica',12))
instruction.pack()
scoreLabel=tkinter.Label(root,text="press enter to start",font=('Helvetica',12))
scoreLabel.pack()
timeLabel = tkinter.Label(root,text='time left: ' + str(timeleft),font=('Helvetica',12))
timeLabel.pack()
label=tkinter.Label(root,font=('Helvetica',60))
label.pack()
e=tkinter.Entry(root)
root.bind('<Return>',startGame)
e.pack()
e.focus_set()
root.mainloop
