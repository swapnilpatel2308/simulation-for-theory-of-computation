

import tkinter as tk
from tkinter import *
from tkinter.simpledialog import askstring
import math
from tkinter import messagebox


def nfa_to_dfa(nfa_transitions, nfa_initial_state, nfa_accepting_states):
    dfa_transitions = []
    dfa_states = [nfa_initial_state]
    queue = [nfa_initial_state]

    while queue:
        current_state = queue.pop(0)
        for symbol in set([transition[1] for transition in nfa_transitions if transition[0] in current_state]):
            next_state = set()
            for transition in nfa_transitions:
                if transition[0] in current_state and transition[1] == symbol:
                    next_state.add(transition[2])
            dfa_transitions.append([current_state, symbol, next_state])
            if next_state not in dfa_states:
                dfa_states.append(next_state)
                queue.append(next_state)

    dfa_accepting_states = [state for state in dfa_states if any(accept_state in state for accept_state in nfa_accepting_states)]

    return dfa_transitions, nfa_initial_state, dfa_accepting_states



root = tk.Tk()
root.geometry("1000x700+0+0")
root.resizable(False, False)
root.title("NFA TO DFA")

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

    print(input_state)
    print(final_state)
    print(transection_list)

    if(len(input_state)==1 and len(final_state)!=0 and len(transection_list)!=0):
        ists = list(set(input_state))
        dfa_transitions, dfa_initial_state, dfa_accepting_states = nfa_to_dfa(transection_list,ists,list(set(final_state)))
        print(dfa_accepting_states)
        print(dfa_initial_state)
        print(dfa_transitions)
        text = f'Init state = {dfa_initial_state}\nFinal states = {dfa_accepting_states}\nTransetions = \n'
        for t1 in dfa_transitions:
            text = text + str(t1)
            text = text + '\n'

        win = Toplevel()
        win.geometry("400x400")
        win.resizable(False,False)

        a = tk.Text(win,width=45,height=24,background="#999999")
        a.insert(INSERT,text)
        a.place(x=0,y=0)
    else:
        messagebox.showerror("Error","Your automata is not define properly.")


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
