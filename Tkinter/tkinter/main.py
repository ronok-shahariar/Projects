from tkinter import *

root = Tk()
root.title("Ronok's Calculator")
root.iconbitmap('C:/Users/Ronok Arya/Downloads/cal2.ico')

e = Entry(root, width=40, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

    if math == "inverse":
        e.insert(0, 1 / f_num)

    if math == "percentage":
        e.insert(0, f_num * int(100))



def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_inverse():
    first_number = e.get()
    global f_num
    global math
    math = "inverse"
    f_num = int(first_number)
    e.delete(0, END)

def button_percentage():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    e.delete(0, END)


# define buttons

button_1 = Button(root, text="1", padx=30, pady=8, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=8, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=8, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=8, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=8, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=8, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=8, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=8, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=8, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=8, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=29, pady=8, command=button_add)
button_equal = Button(root, text="=", padx=29, pady=8, command=button_equal)
button_clear = Button(root, text="C", padx=29, pady=8, command=button_clear)
button_subtract = Button(root, text="-", padx=31, pady=8, command=button_subtract)
button_multiply = Button(root, text="*", padx=30, pady=8, command=button_multiply)
button_divide = Button(root, text="/", padx=30, pady=8, command=button_divide)
button_inverse = Button(root, text="1/x", padx=25, pady=8, command=button_inverse)
button_percentage = Button(root, text="%", padx=28, pady=8, command=button_percentage)

# put the bttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_inverse.grid(row=4, column=1)
button_percentage.grid(row=5, column=1)

# myLabel.pack() = Shoving it into the screen

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)


root.mainloop()
