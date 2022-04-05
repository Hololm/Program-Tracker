import tkinter as tk
from tkinter import ttk, Label
import os
import time
import psutil
import sys

minutes = 0
root = tk.Tk()
root.wm_title("CSP Tracker")
root.geometry("600x600")
a = Label(root)
a.pack()

def update(x):
    root.after(50, update)
    add = open('csp.txt', 'r')
    x = add.read()
    add.close()
    a['text'] = "current session: {}".format(x)
update(minutes)