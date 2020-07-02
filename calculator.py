from tkinter import *
import time

# initially: dark-mode
bg_c = "#383838"
bg_c_r = "#303030"
fg_c = "#E8E8E8"
fg_c_r = "#FFFFFF"
h_b_c = "#000000"

root = Tk()     # basic widget (window)
root.title("Simple Calculator")
root.configure(bg=bg_c_r)
e = Entry(root, width=35, borderwidth=5, bg=bg_c, fg=fg_c, highlightbackground=h_b_c)
maths = Entry(root, width=35, borderwidth=5, bg=bg_c, fg=fg_c, highlightbackground=h_b_c)

# globals
val_add = []
val_sub = []
val_multi = []
val_bracket = []

b_num = 0
last_op = "none"
ans_multi_plus = 1
ans_multi_minus = 1
ans_bracket = int


# multiply entries in given list
def multi_list(my_list):
    result = 1
    for val in my_list:
        result = result * val
    return result


# toggle dark-mode
def button_mode():
    global bg_c
    global fg_c
    if button_mode.config('relief')[-1] == 'sunken':
        button_mode.config(relief="raised")
        for widget in widgets:
            try:
                widget.configure(bg=bg_c, fg=fg_c)
            except TclError:
                widget.configure(bg=bg_c_r)
    else:
        button_mode.config(relief="sunken")
        for widget in widgets:
            try:
                widget.configure(bg=fg_c, fg=bg_c)
            except TclError:
                widget.configure(bg=fg_c_r)


def button_bracket_open():
    global last_op
    global b_num
    b_num += 1
    current_m = maths.get()
    maths.delete(0, END)
    maths.insert(0, str(current_m) + "(")
    if last_op == "click" or last_op == "click+" or last_op == "click-" or last_op == "click*-" or last_op == "click*+" or last_op == "bracket_click":
        print("syntax")
        wrong_syntax()
    elif b_num == 1:
        if last_op == "add" or last_op == "none":
            val_bracket.append("+")
            e.delete(0, END)
            last_op = "bracket_add"
        if last_op == "sub":
            val_bracket.append("-")
            e.delete(0, END)
            last_op = "bracket_sub"
        if last_op == "multi" or last_op == "multi+" or last_op == "multi-":
            val_bracket.append("*")
            e.delete(0, END)
            last_op = "bracket_multi"
    elif b_num != 1:
        val_bracket.append("(")
        e.delete(0, END)


def button_bracket_close():
    global last_op
    global b_num
    b_num -= 1
    current_m = maths.get()
    maths.delete(0, END)
    maths.insert(0, str(current_m) + ")")
    if b_num == 0:
        if last_op == "bracket_add":
            val_bracket.append(str(e.get()))
            val_bracket.insert(0, "0")
            val_add.append(eval("".join(val_bracket)))
            val_bracket.clear()
            e.delete(0, END)
            last_op = "bracket_end"
        elif last_op == "bracket_sub":
            val_bracket.append(str(e.get()))
            val_bracket.insert(0, "0")
            val_sub.append(eval("".join(val_bracket)))
            val_bracket.clear()
            e.delete(0, END)
            last_op = "bracket_end"
        elif last_op == "bracket_multi":
            val_bracket.append(str(e.get()))
            val_bracket.insert(0, "1")
            val_multi.append(eval("".join(val_bracket)))
            val_bracket.clear()
            e.delete(0, END)
            last_op = "bracket_end"
    else:
        val_bracket.append(str(e.get()))
        val_bracket.append(")")
        e.delete(0, END)


# number clicked
def button_click(nb):
    global last_op
    current = e.get()
    current_m = maths.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(nb))
    maths.delete(0, END)
    maths.insert(0, str(current_m) + str(nb))
    if last_op == "add" or last_op == "click+":
        last_op = "click+"
    elif last_op == "sub" or last_op == "click-":
        last_op = "click-"
    elif last_op == "multi-" or last_op == "click*-":
        last_op = "click*-"
    elif last_op == "multi+" or last_op == "click*+":
        last_op = "click*+"
    elif last_op == "bracket_add":
        last_op = "bracket_add"
    elif last_op == "bracket_sub":
        last_op = "bracket_sub"
    elif last_op == "bracket_multi":
        last_op = "bracket_multi"
    else:
        last_op = "click"


# clear all
def button_clear():
    global last_op
    e.delete(0, END)
    val_add.clear()
    val_sub.clear()
    val_bracket.clear()
    maths.delete(0,END)
    last_op = "clear"


def wrong_syntax():
    button_clear()
    e.insert(0, "WRONG SYNTAX")
    time.sleep(1)


# + clicked
def button_add():
    global last_op
    global val_multi
    global ans_multi_plus
    global ans_multi_minus
    current_m = maths.get()
    maths.delete(0, END)
    maths.insert(0, str(current_m) + "+")
    if e.get() != "" and last_op == "click" or last_op == "equal" and len(val_add) == 0:
        val_add.append(int(e.get()))
        e.delete(0, END)
        last_op = "add"
    if last_op == "click+":
        val_add.append(int(e.get()))
        e.delete(0, END)
        last_op = "add"
    if last_op == "click-":
        val_sub.append(int(e.get()))
        e.delete(0, END)
        last_op = "add"
    if last_op == "click*+":
        val_multi.append(int(e.get()))
        ans_multi_plus = multi_list(val_multi)
        val_multi.clear()
        val_add.append(ans_multi_plus)
        ans_multi_plus = 1
        e.delete(0, END)
        last_op = "add"
    if last_op == "click*-":
        val_multi.append(int(e.get()))
        ans_multi_minus = multi_list(val_multi)
        val_multi.clear()
        val_sub.append(ans_multi_minus)
        ans_multi_minus = 1
        e.delete(0, END)
        last_op = "add"
    elif last_op == "bracket_add":
        val_bracket.append(str(e.get()))
        val_bracket.append("+")
        last_op = "bracket_add"
    elif last_op == "bracket_sub":
        val_bracket.append(str(e.get()))
        val_bracket.append("+")
        last_op = "bracket_sub"
    elif last_op == "bracket_multi":
        val_bracket.append(str(e.get()))
        val_bracket.append("+")
        last_op = "bracket_multi"
    if last_op == "bracket_end":
        last_op = "add"
    e.delete(0, END)


# x clicked
def button_multi():
    global last_op
    current_m = maths.get()
    maths.delete(0, END)
    maths.insert(0, str(current_m) + "x")
    if e.get() != "" and last_op == "click" or last_op == "equal" and len(val_multi) == 0:
        val_multi.append(int(e.get()))
        last_op = "multi+"
        e.delete(0, END)
    elif last_op == "click+":
        val_multi.append(int(e.get()))
        last_op = "multi+"
        e.delete(0, END)
    elif last_op == "click-":
        val_multi.append(int(e.get()))
        last_op = "multi-"
        e.delete(0, END)
    elif e.get() != "" and last_op == "multi+" or last_op == "click*+":
        val_multi.append(int(e.get()))
        last_op = "multi+"
        e.delete(0, END)
    elif e.get() != "" and last_op == "multi-" or last_op == "click*-":
        val_multi.append(int(e.get()))
        last_op = "multi-"
        e.delete(0, END)
    elif last_op == "bracket_add":
        val_bracket.append(str(e.get()))
        val_bracket.append("*")
        last_op = "bracket_add"
    elif last_op == "bracket_sub":
        val_bracket.append(str(e.get()))
        val_bracket.append("*")
        last_op = "bracket_sub"
    elif last_op == "bracket_multi":
        val_bracket.append(str(e.get()))
        val_bracket.append("*")
        last_op = "bracket_multi"
    else:
        last_op = "multi"
        e.delete(0, END)


# - clicked
def button_subtract():
    global last_op
    global val_multi
    global ans_multi_plus
    global ans_multi_minus
    current_m = maths.get()
    maths.delete(0, END)
    maths.insert(0, str(current_m) + "-")
    if e.get() != "" and last_op == "click" or last_op == "equal" and len(val_add) == 0:
        val_add.append(int(e.get()))
        e.delete(0, END)
    if last_op == "click-":
        val_sub.append(int(e.get()))
        e.delete(0, END)
    if last_op == "click+":
        val_add.append(int(e.get()))
        e.delete(0, END)
    if last_op == "click*+":
        val_multi.append(int(e.get()))
        ans_multi_plus = multi_list(val_multi)
        val_multi.clear()
        val_add.append(ans_multi_plus)
        ans_multi_plus = 1
        e.delete(0, END)
    if last_op == "click*-":
        val_multi.append(int(e.get()))
        ans_multi_minus = multi_list(val_multi)
        val_multi.clear()
        val_sub.append(ans_multi_minus)
        ans_multi_minus = 1
        e.delete(0, END)
    elif last_op == "bracket_add":
        val_bracket.append(str(e.get()))
        val_bracket.append("-")
        last_op = "bracket_add"
    elif last_op == "bracket_sub":
        val_bracket.append(str(e.get()))
        val_bracket.append("-")
        last_op = "bracket_sub"
    elif last_op == "bracket_multi":
        val_bracket.append(str(e.get()))
        val_bracket.append("-")
        last_op = "bracket_multi"
    elif last_op == "bracket_end":
        last_op = "sub"
    e.delete(0, END)
    last_op = "sub"


# = clicked, calculate
def button_equal():
    global last_op
    global ans_multi_plus
    global ans_multi_minus
    global val_multi
    global val_add
    global val_sub
    global b_num
    if b_num == 0:
        if last_op == "click+":
            val_add.append(int(e.get()))
        if last_op == "click-":
            val_sub.append(int(e.get()))
        if last_op == "click*+":
            val_multi.append(int(e.get()))
            ans_multi_plus = multi_list(val_multi)
            val_add.append(ans_multi_plus)
            ans_multi_plus = 1
            val_multi.clear()
        if last_op == "click*-":
            val_multi.append(int(e.get()))
            ans_multi_minus = multi_list(val_multi)
            val_sub.append(ans_multi_minus)
            ans_multi_minus = 1
            val_multi.clear()
        if last_op == "bracket_end":
            ans_multi_plus = multi_list(val_multi)
            val_add.append(ans_multi_plus)
            ans_multi_plus = 1
            val_multi.clear()
        ans_add = sum(val_add)
        ans_sub = sum(val_sub)
        ans = ans_add - ans_sub
        e.delete(0, END)
        maths.delete(0, END)
        maths.insert(0, ans)
        e.insert(0, ans)
        val_add.clear()
        val_sub.clear()
        last_op = "equal"
    else:
        wrong_syntax()


# setup of buttons
button_1 = Button(root, text="1", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=38, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_add)
button_minus = Button(root, text="-", padx=42, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_subtract)
button_multi = Button(root, text="x", padx=39, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_multi)
button_equal = Button(root, text="=", padx=38, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=117, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_clear)
button_mode = Button(root, text="toggle dark-mode", padx=39, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_mode)
button_bracket_op = Button(root, text="(", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_bracket_open)
button_bracket_cl = Button(root, text=")", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=button_bracket_close)
widgets = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0,
           button_plus, button_minus, button_multi, button_equal, button_clear, button_mode, root, e]

maths.grid(row=0, column=0, columnspan=3)
button_clear.grid(row=7, column=0, columnspan=3)
button_mode.grid(row=0, column=4, columnspan=3)

buttons = [
           [button_8, button_9],
           [button_4, button_5, button_6],
           [button_1, button_2, button_3],
           [button_plus, button_0, button_minus],
           [button_multi, button_equal],
           [button_bracket_op, button_bracket_cl]]


def add_new_button(button, row, col):
    global buttons
    row = row - 1
    rowsize = []
    try:
        buttons_row = buttons[row]
        buttons_row.insert(col, button)
    except IndexError:
        buttons.append([button])
    for rows in range(len(buttons)):
        rowsize.append(len(buttons[rows]))
    maxrow = max(rowsize)
    for r in range(len(buttons)):
        for c in range(maxrow):
            try:
                if buttons[r][c] != button:
                    buttons[r][c].grid(row=r+1, column=c)
                else:
                    buttons[r][c].grid(row=row+1, column=col)
            except IndexError:
                pass


# initialize root
add_new_button(button_7, 1, 0)
root.mainloop()
print(b_num)
print(val_bracket)
print(val_multi)
print(last_op)