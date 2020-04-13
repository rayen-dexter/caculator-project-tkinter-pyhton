from tkinter import *
def d0 ():
    e.insert(END,'0')
def d1 ():
    e.insert(END,'1')
def d2 ():
    e.insert(END,'2')
def d3 ():
    e.insert(END,'3')
def d4 ():
    e.insert(END,'4')
def d5 ():
    e.insert(END,'5')
def d6 ():
    e.insert(END,'6')
def d7 ():
    e.insert(END,'7')
def d8 ():
    e.insert(END,'8')
def d9 ():
    e.insert(END,'9')
def add() :
    e.insert(END,'+')
def  equal() :
    n=e.get("1.0",END)
    total = str(eval(n))
    e.insert(END,'='+total)
def reset () :
    e.delete('1.0',END)
def substract() :
    e.insert(END,'-')
def multiply() :
    e.insert(END,'*')
def divide() :
    e.insert(END,'/')
win=Tk()
win.configure(bg='DarkTurquoise')
win.title('calculator')
e=Text(bg='black',fg='DarkTurquoise',width=20,height=1,font=("Arial Bold", 15))
e.grid(row=1,column=2)
b0=Button(text='0',relief=RAISED,width=20,command=d0,bg='DarkTurquoise',font=("Arial Bold", 15))
b0.grid(row=1,column=1)
b1=Button(text='1',relief=RAISED,width=20,command=d1,bg='DarkTurquoise',font=("Arial Bold", 15))
b1.grid(row=2,column=1)
b2=Button(text='2',relief=RAISED,width=20,command=d2,bg='DarkTurquoise',font=("Arial Bold", 15))
b2.grid(row=2,column=2)
b3=Button(text='3',relief=RAISED,width=20,command=d3,bg='DarkTurquoise',font=("Arial Bold", 15))
b3.grid(row=2,column=3)
b4=Button(text='4',relief=RAISED,width=20,command=d4,bg='DarkTurquoise',font=("Arial Bold", 15))
b4.grid(row=3,column=1)
b5=Button(text='5',relief=RAISED,width=20,command=d5,bg='DarkTurquoise',font=("Arial Bold", 15))
b5.grid(row=3,column=2)
b6=Button(text='6',relief=RAISED,width=20,command=d6,bg='DarkTurquoise',font=("Arial Bold", 15))
b6.grid(row=3,column=3)
b7=Button(text='7',relief=RAISED,width=20,command=d7,bg='DarkTurquoise',font=("Arial Bold", 15))
b7.grid(row=4,column=1)
b8=Button(text='8',relief=RAISED,width=20,command=d8,bg='DarkTurquoise',font=("Arial Bold", 15))
b8.grid(row=4,column=2)
b9=Button(text='9',relief=RAISED,width=20,command=d9,bg='DarkTurquoise',font=("Arial Bold", 15))
b9.grid(row=4,column=3)
add_btn=Button(text=('+'),command=add,width=20,bg='DarkTurquoise',font=("Arial Bold", 15)).grid(row=5,column=1)
eql_btn=Button(text=('='),width=20,command=equal,bg='DarkTurquoise',font=("Arial Bold", 15)).grid(row=5,column=3)
reset_btn=Button(text=('reset'),width=20,command=reset,bg='DarkTurquoise',font=("Arial Bold", 15)).grid(row=5,column=2)
sub_btn=Button(text=('-'),width=20,command=substract,bg='DarkTurquoise',font=("Arial Bold", 15)).grid(row=6,column=1)
mul_btn=Button(text=('x'),width=20,command=multiply,bg='DarkTurquoise',font=("Arial Bold", 15)).grid(row=6,column=2)
div_btn=Button(text=('/'),width=20,command=divide,bg='DarkTurquoise',font=("Arial Bold", 15)).grid(row=6,column=3)



win.mainloop()
