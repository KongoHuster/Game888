import tkinter as tk

window = tk.Tk()
window.title('888龙')
window.geometry('400x400')
e = tk.Entry(window, show=None)
e.pack(side="top")


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=15,
               height=2, command=insert_point)

b1.pack(side="left")
b2 = tk.Button(window, text='insert end',
               command=insert_end)
b2.pack(side="right")
t = tk.Text(window, width=20, height=20)
t.pack(side="right")

window.mainloop()
