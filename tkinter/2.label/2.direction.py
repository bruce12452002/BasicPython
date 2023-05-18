import tkinter as tk
window = tk.Tk()
window.title("label direction")
window.geometry('500x600')

png = tk.PhotoImage(file='../../download/1.png')
label1 = tk.Label(window, image=png)
label1.pack(side='right')  # top bottom left right

window.mainloop()
