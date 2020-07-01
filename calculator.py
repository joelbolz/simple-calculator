from tkinter import *

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

# globals
val_add = []
val_sub = []
val_multi = []
last_op = ""
ans_multi_plus = 1
ans_multi_minus = 1


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


# number clicked
def button_click(nb):
    global last_op
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(nb))
    if last_op == "add" or last_op == "click+":
        last_op = "click+"
    elif last_op == "sub" or last_op == "click-":
        last_op = "click-"
    elif last_op == "multi-" or last_op == "click*-":
        last_op = "click*-"
    elif last_op == "multi+" or last_op == "click*+":
        last_op = "click*+"
    else:
        last_op = "click"


# clear all
def button_clear():
    global last_op
    e.delete(0, END)
    val_add.clear()
    val_sub.clear()
    last_op = "clear"


# + clicked
def button_add():
    global last_op
    global val_multi
    global ans_multi_plus
    global ans_multi_minus
    if e.get() != "" and last_op == "click" or last_op == "equal" and len(val_add) == 0:
        val_add.append(int(e.get()))
        e.delete(0, END)
    if last_op == "click+":
        val_add.append(int(e.get()))
        e.delete(0, END)
    if last_op == "click-":
        val_sub.append(int(e.get()))
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
    e.delete(0, END)
    last_op = "add"


# x clicked
def button_multi():
    global last_op
    if e.get() != "" and last_op == "click" or last_op == "equal" and len(val_multi) == 0:
        val_multi.append(int(e.get()))
        last_op = "multi+"
        e.delete(0, END)
    elif last_op == "click+":
        val_multi.append(int(e.get()))
        last_op = "multi+"
        e.delete((0, END))
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
    else:
        last_op = "multi"
        e.delete(0, END)


# - clicked
def button_subtract():
    global last_op
    global val_multi
    global ans_multi_plus
    global ans_multi_minus
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
    ans_add = sum(val_add)
    ans_sub = sum(val_sub)
    ans = ans_add - ans_sub
    e.delete(0, END)
    e.insert(0, ans)
    val_add.clear()
    val_sub.clear()
    last_op = "equal"


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
button_test = Button(root, text="test", padx=40, bg=bg_c, fg=fg_c, highlightbackground=h_b_c, pady=20, command=lambda: button_click(8))
widgets = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0,
           button_plus, button_minus, button_multi, button_equal, button_clear, button_mode, root, e]

e.grid(row=0, column =0, columnspan=3)
button_clear.grid(row=6, column =0, columnspan=3)
button_mode.grid(row=0, column =4, columnspan=3)

buttons = [
           [button_8, button_9],
           [button_4, button_5, button_6],
           [button_1, button_2, button_3],
           [button_plus, button_0, button_minus],[button_multi, button_equal]]


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
