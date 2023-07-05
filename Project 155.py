from tkinter import*
import random

root=Tk()
root.geometry('400x400')
root.title("Dictionary")

Dictionary = {"Color":["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def background():
    Random_number = random.randint(0,7)
    print(Dictionary["Color"][Random_number])
    root.configure(background=Dictionary["Color"][Random_number])
    
button1 = Button(root,text="Click Me",command=background)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
    
