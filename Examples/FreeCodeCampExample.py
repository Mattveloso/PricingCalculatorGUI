from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3,padx=10,pady=10)

def button_click(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number=e.get()
	global f_num
	f_num=int(first_number)
	e.delete(0,END)

def button_equal():
	second_number=e.get()
	e.delete(0,END)
	e.insert(0,f_num+int(second_number))

#buttons
button=[]
for number in range(0,10):
    button.append(Button(root, text=str(number),padx=40,pady=20,command=lambda: button_click(number)))
    button[number].grid(row=number, column=number)
# but_1= Button(root, text="1",padx=40,pady=20,command=lambda: button_click(1))
# but_2= Button(root, text="2",padx=40,pady=20,command=lambda: button_click(2))
# but_3= Button(root, text="3",padx=40,pady=20,command=lambda: button_click(3))
# but_4= Button(root, text="4",padx=40,pady=20,command=lambda: button_click(4))
# but_5= Button(root, text="5",padx=40,pady=20,command=lambda: button_click(5))
# but_6= Button(root, text="6",padx=40,pady=20,command=lambda: button_click(6))
# but_7= Button(root, text="7",padx=40,pady=20,command=lambda: button_click(7))
# but_8= Button(root, text="8",padx=40,pady=20,command=lambda: button_click(8))
# but_9= Button(root, text="9",padx=40,pady=20,command=lambda: button_click(9))
# but_0= Button(root, text="0",padx=40,pady=20,command=lambda: button_click(0))
#but_add= Button(root, text="+",padx=39,pady=20,command=button_add)
#but_equal= Button(root, text="=",padx=85,pady=20,command=button_equal)
#but_clear= Button(root, text="Clc",padx=80,pady=20,command= button_clear)

#put the buttons on the screen

# but_1.grid(row=3,column=0)
# but_2.grid(row=3,column=1)
# but_3.grid(row=3,column=2)
#
# but_4.grid(row=2,column=0)
# but_5.grid(row=2,column=1)
# but_6.grid(row=2,column=2)
#
# but_7.grid(row=1,column=0)
# but_8.grid(row=1,column=1)
# but_9.grid(row=1,column=2)
#
# but_0.grid(row=4,column=0)

# but_clear.grid(row=4, column=1,columnspan=2)
# but_add.grid(row=5,column=0)
# but_equal.grid(row=5,column=1,columnspan=2)

root.mainloop()
