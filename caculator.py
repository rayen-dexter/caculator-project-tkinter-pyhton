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
    n=e.get()
    total = str(eval(n))
    e.delete(0,END)
    e.insert(END,str(total))
def reset () :
    e.delete(0,END)
def substract() :
    e.insert(END,'-')
def multiply() :
    e.insert(END,'*')
def divide() :
    e.insert(END,'/')
def delete() :
    n=e.get()
    n= n[0:-1]
    e.delete(0,END)
    e.insert(END,str(n))
def point():
    e.insert(END,'.')    
win=Tk()
win.configure(bg='RoyalBlue1')
win.title('calculator')
e=Entry(bg='black',fg='RoyalBlue',font=("Arial Bold", 20))
e.grid(row=1,column=1,columnspan=3)
b0=Button(text='0',relief=RAISED,width=4,command=d0,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b0.grid(row=5,column=2)
b1=Button(text='1',relief=RAISED,width=4,command=d1,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b1.grid(row=2,column=1)
b2=Button(text='2',relief=RAISED,width=4,command=d2,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b2.grid(row=2,column=2)
b3=Button(text='3',relief=RAISED,width=4,command=d3,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b3.grid(row=2,column=3)
b4=Button(text='4',relief=RAISED,width=4,command=d4,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b4.grid(row=3,column=1)
b5=Button(text='5',relief=RAISED,width=4,command=d5,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b5.grid(row=3,column=2)
b6=Button(text='6',relief=RAISED,width=4,command=d6,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b6.grid(row=3,column=3)
b7=Button(text='7',relief=RAISED,width=4,command=d7,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b7.grid(row=4,column=1)
b8=Button(text='8',relief=RAISED,width=4,command=d8,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b8.grid(row=4,column=2)
b9=Button(text='9',relief=RAISED,width=4,command=d9,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20))
b9.grid(row=4,column=3)
add_btn=Button(text='+',relief=RAISED,width=4,command=add,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20)).grid(row=5,column=1)
eql_btn=Button(text='=',relief=RAISED,width=4,command=equal,bg='RoyalBlue1',fg='Grey18',height=3,font=("Arial Bold", 20)).grid(row=5,column=4,rowspan=2,sticky=NE)
del_btn=Button(text='delete',relief=RAISED,width=6,height=4,command=delete,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 15)).grid(row=3,column=4,rowspan=2,sticky=NE)
clear_btn=Button(text='clear\nall',relief=RAISED,width=6,height=3,command=reset,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 15)).grid(row=1,column=4,rowspan=2,sticky=NE)
sub_btn=Button(text='-',relief=RAISED,width=4,command=substract,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20)).grid(row=6,column=1)
mul_btn=Button(text='x',relief=RAISED,width=4,command=multiply,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20)).grid(row=5,column=3)
div_btn=Button(text='/',relief=RAISED,width=4,command=divide,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20)).grid(row=6,column=3)
pnt_btn=Button(text='.',relief=RAISED,width=4,command=point,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 20)).grid(row=6,column=2)
l=Label(text='this app is made by\npython tkinter\ngithub.com/rayen-sayadi',relief=SUNKEN,height=4,bg='RoyalBlue1',fg='Grey18',font=("Arial Bold", 5)).grid(row=7,column=2)
win.mainloop()
