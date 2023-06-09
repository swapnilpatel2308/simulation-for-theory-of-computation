from tkinter import *
import tkinter as tk
import subprocess

root =tk.Tk()

root.geometry("300x520")
root.resizable(False,False)
root.title("TOC Simulator")
root.configure(background="#00ffff")

def run_is_fa():
    subprocess.call(['python', 'is_fa.py'])
is_fa = Button(root,width=25,height=3,text="Is Finite Automaton",font='Arial 10 bold',command=run_is_fa)
is_fa.place(x=50,y=20)

def run_is_dfa():
    subprocess.call(['python', 'is_dfa.py'])
is_dfa = Button(root,width=25,height=3,text="Is DFA",font='Arial 10 bold',command=run_is_dfa)
is_dfa.place(x=50,y=90)

def run_is_nfa():
    subprocess.call(['python', 'is_nfa.py'])
is_nfa = Button(root,width=25,height=3,text="Is NFA",font='Arial 10 bold',command=run_is_nfa)
is_nfa.place(x=50,y=160)

def run_acc():
    subprocess.call(['python', 'Accepted.py'])
acc = Button(root,width=25,height=3,text="String Accepted..",font='Arial 10 bold',command=run_acc)
acc.place(x=50,y=230)

def run_nfatodfa():
    subprocess.call(['python', 'nfa_to_dfa.py'])
nfatodfa = Button(root,width=25,height=3,text="NFA TO DFA",font='Arial 10 bold',command=run_nfatodfa)
nfatodfa.place(x=50,y=300)

def run_melay():
    subprocess.call(['python', 'MelayMachine.py'])
melay = Button(root,width=25,height=3,text="Melay Machine",font='Arial 10 bold',command=run_melay)
melay.place(x=50,y=370)

def run_moore():
    subprocess.call(['python', 'MooreMachine.py'])
moore = Button(root,width=25,height=3,text="Moore Machine",font='Arial 10 bold',command=run_moore)
moore.place(x=50,y=440)

root.mainloop()