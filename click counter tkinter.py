from tkinter import * 
root = Tk()
root.title('counter')
root.configure(bg='Gold')
root.geometry('200x280')
y=0
x=Label(text=y,font=("Arial Bold", 50),bg='Gold')
x.pack()
def click():
    global y
    y += 1
    x.configure(text=y,font=("Arial Bold", 50),bg='Gold')
    x.pack()
o=Button(root,text = '+',
         font =( 'Verdana',40),
         command=click,bg='Grey',fg='Gold',relief=RAISED)
def reset():
    global y
    y = 0
    x.configure(text=y,font=("Arial Bold", 50),bg='Gold')
    x.pack()
o.pack()
p=Button(root,text = 'reset',
         font =( 'Verdana',20),
         command=reset,bg='Grey',fg='Gold',relief=RAISED)
p.pack()

mainloop() 


