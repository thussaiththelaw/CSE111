import tkinter as tk
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
from tkinter import *
  
# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()