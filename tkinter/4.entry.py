import tkinter as tk


def click():
    print(entry1.get())


window = tk.Tk()
window.title("button")
window.geometry('400x300')

# txt = tk.StringVar
entry1 = tk.Entry(window, state='normal')
entry2 = tk.Entry(window, state='disabled')
entry3 = tk.Entry(window, state='readonly')

entry1.pack()
entry2.pack()
entry3.pack()
tk.Button(window, text="click", command=click).pack()

window.mainloop()
