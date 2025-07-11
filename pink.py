from tkinter import *
root = Tk()
root.title("Calculator🎀")
root.geometry('350x350')
root.minsize(300, 300)
root.maxsize(350, 400)
root.configure(bg='#FFC0CB')
# Configure 3 columns to be equal size
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
e = Entry(width=50, borderwidth=5, font=('Curlz MT', 15), bg='#FFE4E1')
e.grid(row=0, column=0, padx=20, pady=20, columnspan=6, ipady=10)
#Define buttons
def backspace():
    current = e.get()
    e.delete(0, END)
    e.insert(0, current[:-1])
def get_number(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear_button():
    e.delete(0, END)
def add():
    global num1, operation
    num1 = float(e.get())
    operation = 'add'
    e.delete(0, END)
def div():
    global num1, operation
    num1 = float(e.get())
    operation = 'div'
    e.delete(0, END)
def mul():
    global num1, operation
    num1 = float(e.get())
    operation = 'mul'
    e.delete(0, END)
def sub():
    global num1, operation
    num1 = float(e.get())
    operation = 'sub'
    e.delete(0, END)
def equal():
    global num2
    try:
        num2 = float(e.get())  # Allow decimals
        e.delete(0, END)
        if operation == "add":
            e.insert(0, str(num1 + num2))
        elif operation == "sub":
            e.insert(0, str(num1 - num2))
        elif operation == "mul":
            e.insert(0, str(num1 * num2))
        elif operation == "div":
            if num2 == 0:
                e.insert(0, '(＃°Д°) Error (÷0)')
            else:
                e.insert(0, str(num1 / num2))
        else:
            e.insert(0, 'w(ﾟДﾟ)w Syntax Error')
    except:
        e.insert(0, '┗|｀O′|┛ Error')
btn_style = {'pady':10, 'padx':10, 'width':10, 'bg':'#FFE4E1', 'font': ('Curlz MT', 10)}
button1 = Button(root, text=1, command=lambda:get_number(1), **btn_style)
button2 = Button(root, text=2, command=lambda:get_number(2), **btn_style)
button3 = Button(root, text=3, command=lambda:get_number(3), **btn_style)
button4 = Button(root, text=4, command=lambda:get_number(4), **btn_style)
button5 = Button(root, text=5, command=lambda:get_number(5), **btn_style)
button6 = Button(root, text=6, command=lambda:get_number(6), **btn_style)
button7 = Button(root, text=7, command=lambda:get_number(7), **btn_style)
button8 = Button(root, text=8, command=lambda:get_number(8), **btn_style)
button9 = Button(root, text=9, command=lambda:get_number(9), **btn_style)
button0 = Button(root, text=0, command=lambda:get_number(0), **btn_style)
button00 = Button(root, text='.', command=lambda:get_number('.'), **btn_style)
button01 = Button(root, text='←', command=backspace, **btn_style)
button_add = Button(root, text='+', command=add, **btn_style)
button_sub = Button(root, text='-', command=sub, **btn_style)
button_div = Button(root, text='÷', command=div, **btn_style)
button_mul = Button(root, text='x', command=mul, **btn_style)
button_clear = Button(root, text='Clear', pady=10, padx=10, command=clear_button, width=25, bg='#FFE4E1')
button_equal = Button(root, text='=', pady=10, padx=10, command=equal, width=25, bg='#FFE4E1')
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=6, column=1)
button00.grid(row=6, column=0)
button01.grid(row=6, column=2)
button_add.grid(row=6, column=3)
button_div.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=1, column=3)
button_clear.grid(row=7, column=0, columnspan=2, rowspan=2, ipady=10)
button_equal.grid(row=7, column=2, columnspan=2, rowspan=2, ipady=10)
root.mainloop()
