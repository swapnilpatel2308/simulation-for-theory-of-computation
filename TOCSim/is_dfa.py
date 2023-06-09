import tkinter as tk
from tkinter import *
from tkinter.simpledialog import askstring
import math
from tkinter import messagebox


def is_dfa(transitions):
    states = set()
    symbols = set()

    for state, symbol, next_state in transitions:
        states.add(state)
        symbols.add(symbol)

    for state in states:
        for symbol in symbols:
            found_transitions = [next_state for s, sym, next_state in transitions if s == state and sym == symbol]
            if len(found_transitions) != 1:
                return False

    return True


root = tk.Tk()
root.geometry("1000x700+0+0")
root.resizable(False, False)
root.title("Is DFA")

frame1 = tk.Frame(root, width=1000, height=40, background="#9999ff")
frame1.place(x=0, y=0)
flag = 0

count1 = 1

count2 = 0
lx0 = 0
lx1 = 0
ly0 = 0
ly1 = 0

state_list = []

node1, node2 = -1, -1

transection_list = []

flag1 = 0

input_state = []
final_state = []


def clear():
    global flag, count1, count2, lx0, lx1, ly0, ly1, state_list, node1, node2, transection_list, flag1, input_state, final_state
    canvas.delete("all")
    flag = 0
    count1 = 1
    count2 = 0
    lx0 = 0
    lx1 = 0
    ly0 = 0
    ly1 = 0
    state_list = []
    node1, node2 = -1, -1
    transection_list = []
    flag1 = 0
    input_state = []
    final_state = []
    b1.config(text="Draw Line")


def run():
    result = is_dfa(transection_list)
    if(result):
        messagebox.showinfo("Result","This is a DFA")
    else:
        messagebox.showinfo("Result","This is Not a DFA")

def select_line():
    global flag
    if(flag == 0):
        flag = 1
        b1.config(text="Draw Node")
    else:
        flag = 0
        b1.config(text="Draw Line")


b1 = Button(frame1, text="Draw Line", command=select_line)
b1.place(x=20, y=6)

b2 = Button(frame1, text="Clear", command=clear)
b2.place(x=900, y=6)

b3 = Button(frame1, text="Run", command=run)
b3.place(x=450, y=6)


frame2 = tk.Frame(root, width=1000, height=660)
frame2.place(x=0, y=40)

canvas = Canvas(frame2, width=1000, height=660, background="#191919")
canvas.place(x=0, y=0)


def chack_is_node(x, y):
    for node in state_list:
        x1 = canvas.coords(node)[0]
        y1 = canvas.coords(node)[1]
        if(x <= x1+20 and x >= x1 and y <= y1+20 and y > y1):
            return (True, node)
    return False, -1


def click(e):
    global node1, node2, flag1
    if(flag == 0):
        global count1
        r = 20
        state_list.append(canvas.create_rectangle(
            e.x, e.y, e.x+r, e.y+r, fill="#00ffff"))
        canvas.create_text(e.x+r//2, e.y+r//2,
                           text=f'Q{count1}', fill='#000000')
        count1 = count1 + 1
        print(state_list)

    elif(flag == 1):
        global lx0, lx1, ly0, ly1, count2
        lx0 = e.x
        ly0 = e.y
        lx1 = e.x
        ly1 = e.y
        con, node1 = chack_is_node(e.x, e.y)
        if(con):
            flag1 = 1
            canvas.create_line(lx0, ly0, lx1, ly1, fill='#ffffff',
                               tags=f'a{count2}', arrow=tk.LAST, width=2)
            count2 = count2 + 1


def on_drag(e):
    global lx0, lx1, ly0, ly1
    if(flag1 == 1):
        lx1 = e.x
        ly1 = e.y
        canvas.coords(f'a{count2-1}', lx0, ly0, lx1-5, ly1-5)


def on_release(e):
    global flag1, node2
    flag1 = 0
    con, node2 = chack_is_node(e.x, e.y)

    if(con):
        name = askstring('Input', 'Enter the value ')
        cod = (canvas.coords(f'a{count2-1}'))
        if(name != None and name != ''):
            if(node1 == node2):
                c1 = canvas.coords(node1)
                canvas.create_line([(c1[0]+20, c1[1]), (c1[0]+20, c1[1]-20),
                                   (c1[0], c1[1]-20), (c1[0], c1[1]-5)], fill='#ffffff', arrow=tk.LAST)
                canvas.create_text(
                    c1[0]+10, c1[1]-25, text=name, fill='#ffffff', font='Arial 10 bold')
            else:
                canvas.create_text(int((cod[0]+cod[2])//2)+10, int(
                    (cod[1]+cod[3])//2)+10, text=name, fill='#ffffff', font='Arial 10 bold')

            for n1 in name.split(','):
                print("transction..", node1,n1, node2)
                transection_list.append([node1,n1,node2])
                
            print(transection_list)

        else:
            canvas.delete(f'a{count2-1}')
    else:
        canvas.delete(f'a{count2-1}')


def set_states_fi(e):
    global input_state, final_state
    con, node = chack_is_node(e.x, e.y)
    if(con):
        win1 = Toplevel()
        win1.geometry("180x120")
        win1.resizable(False, False)
        # win1.overrideredirect(1)
        win1.title("setting")

        def fbpress():
            final_state.append(node)
            canvas.itemconfig(node, fill='#00ff00')
            win1.destroy()

        def ibpress():
            global input_state
            input_state.append(node)
            canvas.itemconfig(node, fill='#0000ff')
            ist = canvas.create_line(canvas.coords(node)[0]-30, canvas.coords(node)[1]+10, canvas.coords(node)[0], canvas.coords(node)[1]+10, arrow=tk.LAST, fill='#ffffff')
            win1.destroy()
           
        def fibpress():
            global input_state, final_state
            canvas.create_line(canvas.coords(node)[0]-30, canvas.coords(node)[1]+10, canvas.coords(node)[0], canvas.coords(node)[1]+10, arrow=tk.LAST, fill='#ffffff')
            final_state.append(node)
            input_state.append(node)
            canvas.itemconfig(node, fill='#f0ff0f')
            win1.destroy()

        ib = Button(win1, text="INIT", command=ibpress)
        ib.place(x=20, y=30)
        fb = Button(win1, text="FINAL", command=fbpress)
        fb.place(x=120, y=30)
        fib = Button(win1, text="FINAL AND INIT", command=fibpress)
        fib.place(x=40, y=80)


canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)
canvas.bind("<Button-3>", set_states_fi)


root.mainloop()
