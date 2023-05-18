import tkinter as tk
window = tk.Tk()
window.title('label test')
window.geometry("300x200")

tk.Label(window, text='Hi').pack()

# foreground 可用 fg 代替； background 可用 bg 代替
tk.Label(window, text='嗨', foreground='blue', background='#0F0', font=('標楷體', 20)).pack()

tk.Label(window, text='寬高', width=1, height=5).pack()
tk.Label(window, text='Hi2', fg='#0000FF', bg='#00FF00', font=('Arial', 20)).pack()

tk.Label(window, text='aaa', padx=20, pady=10, bg='yellow').pack()

window.mainloop()
