import tkinter as tk


def click():
    lbl['text'] = 'show'


def cancel():
    lbl['text'] = ''


window = tk.Tk()
window.title("button")
window.geometry('300x200')

lbl = tk.Label(window, text='hello')
tk.Button(window, text="click", command=click).pack()
tk.Button(window, text="cancel", command=cancel).pack()

lbl.pack()

window.mainloop()
