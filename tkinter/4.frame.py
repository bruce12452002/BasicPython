import tkinter as tk

window = tk.Tk()
window.title("frame")  # 預設為 tk
window.geometry('300x200')  # 不可空格

f0 = tk.Frame(window)
f1 = tk.Frame(window)
f2 = tk.Frame(window)
f0.pack()
f1.pack(side='left')
f2.pack(side='right')

tk.Label(f0, text='label').pack()
tk.Button(f1, text="left button").pack(padx=30)
tk.Button(f2, text="right button").pack(padx=30)

window.mainloop()
