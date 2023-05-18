import tkinter as tk
window = tk.Tk()
window.title("label grid")
window.geometry('400x300')

label00 = tk.Label(window, text='00')
label01 = tk.Label(window, text='01')
label02 = tk.Label(window, text='02')
label10 = tk.Label(window, text='10')
label11 = tk.Label(window, text='11')
label12 = tk.Label(window, text='12')

label00.grid(row=0, column=0)
label01.grid(row=0, column=1)
label02.grid(row=0, column=2)
label10.grid(row=1, column=0)
label11.grid(row=1, column=1)
label12.grid(row=1, column=2)

window.mainloop()
