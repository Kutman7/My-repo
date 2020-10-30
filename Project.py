import math as mat
from tkinter import *

# defining window
win = Tk()
win.title("Calculator")
win.resizable(False, False)
win.iconbitmap("Black_Friday__Black_Friday_Calculator"
               "_Calculation_Budget_Finance-512.ico")

show_btn = Entry(win, justify=RIGHT, font=("arial", 50, "bold"),
                 bg="#27282b", fg="#ebebeb", width=11, borderwidth=20)
show_btn.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def btn_click(num):
    x = show_btn.get()
    show_btn.delete(0, END)
    show_btn.insert(0, str(x) + str(num))


# Functions of Operators


def btn_add():
    first_num = show_btn.get()
    global f_num
    global math
    math = "addition"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_sub():
    first_num = show_btn.get()
    global f_num
    global math
    math = "subtraction"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_mul():
    first_num = show_btn.get()
    global f_num
    global math
    math = "multiplication"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_div():
    first_num = show_btn.get()
    global f_num
    global math
    math = "division"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_square():
    first_num = show_btn.get()
    global f_num
    global math
    math = "square"
    try:
        f_num = int(first_num)
    except ValueError:
        pass


def btn_percentage():
    first_num = show_btn.get()
    global f_num
    global math
    math = "percentage"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_power():
    first_num = show_btn.get()
    global f_num
    global math
    math = "power"
    try:
        f_num = int(first_num)
    except ValueError:
        pass


def btn_factorial():
    first_num = show_btn.get()
    global f_num
    global math
    math = "factorial"
    try:
        f_num = int(first_num)
    except ValueError:
        pass


def btn_clear1():
    first_num = show_btn.get()
    for k in range(len(first_num) - 1, -1, -1):
        show_btn.delete(k)
        break


def btn_clear():
    try:
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_equal():
    second_num = show_btn.get()
    show_btn.delete(0, END)
    try:
        if math == "addition":
            show_btn.insert(0, f_num + int(second_num))
        elif math == "subtraction":
            show_btn.insert(0, f_num - int(second_num))
        elif math == "multiplication":
            show_btn.insert(0, f_num * int(second_num))
        elif math == "division":
            show_btn.insert(0, f_num // int(second_num))
        elif math == "square":
            show_btn.insert(0, mat.sqrt(f_num))
        elif math == "power":
            show_btn.insert(0, f_num * f_num)
        elif math == "percentage":
            show_btn.insert(0, f_num / 100 * int(second_num))
        else:
            show_btn.insert(0, mat.factorial(f_num))
    except NameError:
        pass


# Creating Number Buttons


btn_1 = Button(win, text="1", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(1))
btn_2 = Button(win, text="2", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(2))
btn_3 = Button(win, text="3", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(3))
btn_4 = Button(win, text="4", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(4))
btn_5 = Button(win, text="5", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(5))
btn_6 = Button(win, text="6", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(6))
btn_7 = Button(win, text="7", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(7))
btn_8 = Button(win, text="8", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(8))
btn_9 = Button(win, text="9", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(9))
btn_0 = Button(win, text="0", activebackground="#cce7e8", bg="#5e5d5d",
               padx=24, pady=2, font=("Verdana", 22), borderwidth=10,
               activeforeground="#5e0808", command=lambda: btn_click(0))

# Creating Operation Buttons


btn_add = Button(win, text="+", activebackground="#e07b39", bg="#857b7b",
                 padx=50, pady=2, font=("Verdana", 22), borderwidth=10,
                 activeforeground="#5e0808", command=btn_add)
btn_sub = Button(win, text="-", activebackground="#e07b39", bg="#857b7b",
                 padx=55, pady=2, font=("Verdana", 22), borderwidth=10,
                 activeforeground="#5e0808", command=btn_sub)
btn_mul = Button(win, text="x", activebackground="#e07b39", bg="#857b7b",
                 padx=53, pady=2, font=("Verdana", 22), borderwidth=10,
                 activeforeground="#5e0808", command=btn_mul)
btn_div = Button(win, text="÷", activebackground="#e07b39", bg="#857b7b",
                 padx=50, pady=2, font=("Verdana", 22), borderwidth=10,
                 activeforeground="#5e0808", command=btn_div)
btn_clear1 = Button(win, text="<=", activebackground="#e07b39",
                    padx=38, pady=2, font=("Verdana", 22), borderwidth=10,
                    activeforeground="#5e0808", bg="#857b7b",
                    command=btn_clear1)
btn_clear = Button(win, text="C", activebackground="#cce7e8", bg="#5e5d5d",
                   padx=23, pady=2, font=("Verdana", 22), borderwidth=10,
                   activeforeground="#5e0808", command=btn_clear)
btn_percentage = Button(win, text="%", activebackground="#cce7e8", padx=18,
                        pady=2, font=("Verdana", 22),
                        borderwidth=10, bg="#5e5d5d",
                        activeforeground="#5e0808", command=btn_percentage)
btn_square = Button(win, text="√", activebackground="#cce7e8", bg="#5e5d5d",
                    padx=21, pady=2, font=("Verdana", 22), borderwidth=10,
                    activeforeground="#5e0808", command=btn_square)
btn_power = Button(win, text="x²", activebackground="#cce7e8", bg="#5e5d5d",
                   padx=17, pady=2, font=("Verdana", 22), borderwidth=10,
                   activeforeground="#5e0808", command=btn_power)
btn_factorial = Button(win, text="n!", activebackground="#cce7e8", padx=18,
                       pady=2, font=("Verdana", 22),
                       borderwidth=10, bg="#5e5d5d",
                       activeforeground="#5e0808", command=btn_factorial)
btn_equal = Button(win, text="=", activebackground="#e07b39", bg="#857b7b",
                   padx=211, pady=2, font=("Verdana", 22), borderwidth=10,
                   activeforeground="#5e0808", command=btn_equal)


def q1(n):
    btn_1['bg'] = 'green'


def q2(n):
    btn_2['bg'] = 'green'


def q3(n):
    btn_3['bg'] = 'green'


def q4(n):
    btn_4['bg'] = 'green'


def q5(n):
    btn_5['bg'] = 'green'


def q6(n):
    btn_6['bg'] = 'green'


def q7(n):
    btn_7['bg'] = 'green'


def q8(n):
    btn_8['bg'] = 'green'


def q9(n):
    btn_9['bg'] = 'green'


def q10(n):
    btn_0['bg'] = 'green'


# ******************************************************************************
# ******************************************************************************


def lv(n):
    btn_1['bg'] = "#5e5d5d"
    btn_2['bg'] = "#5e5d5d"
    btn_3['bg'] = "#5e5d5d"
    btn_4['bg'] = "#5e5d5d"
    btn_5['bg'] = "#5e5d5d"
    btn_6['bg'] = "#5e5d5d"
    btn_7['bg'] = "#5e5d5d"
    btn_8['bg'] = "#5e5d5d"
    btn_9['bg'] = "#5e5d5d"
    btn_0['bg'] = "#5e5d5d"


btn_1.bind("<Enter>", q1)
btn_1.bind("<Leave>", lv)
btn_2.bind("<Enter>", q2)
btn_2.bind("<Leave>", lv)
btn_3.bind("<Enter>", q3)
btn_3.bind("<Leave>", lv)
btn_4.bind("<Enter>", q4)
btn_4.bind("<Leave>", lv)
btn_5.bind("<Enter>", q5)
btn_5.bind("<Leave>", lv)
btn_6.bind("<Enter>", q6)
btn_6.bind("<Leave>", lv)
btn_7.bind("<Enter>", q7)
btn_7.bind("<Leave>", lv)
btn_8.bind("<Enter>", q8)
btn_8.bind("<Leave>", lv)
btn_9.bind("<Enter>", q9)
btn_9.bind("<Leave>", lv)
btn_0.bind("<Enter>", q10)
btn_0.bind("<Leave>", lv)

# Setting buttons on win


btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)

btn_add.grid(row=1, column=3)
btn_sub.grid(row=2, column=3)
btn_mul.grid(row=3, column=3)
btn_div.grid(row=4, column=3)

btn_clear.grid(row=5, column=0)
btn_percentage.grid(row=4, column=1)
btn_square.grid(row=4, column=2)
btn_power.grid(row=5, column=1)
btn_factorial.grid(row=5, column=2)
btn_clear1.grid(row=5, column=3)

btn_equal.grid(row=6, column=0, columnspan=5)

win.mainloop()
