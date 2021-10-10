import tkinter as tk
def calculate():
    num_1 = float(num_1_in.get())
    num_2 = float(num_2_in.get())
    operation = operation_in.get()
    if operation == '+':
        output.configure(text=str(num_1 + num_2))
    elif operation == '-':
        output.configure(text=str(num_1 - num_2))
    elif operation == '*' or operation == 'x':
        output.configure(text=str(num_1 * num_2))
    elif operation == '/':
        output.configure(text=str(num_1 / num_2))
    else:
        output.configure(text="We don't understand.")

win = tk.Tk()
win.title('Calculator')
win.minsize(400, 400)
num_1_in = tk.Entry(win)
operation_in = tk.Entry(win)
num_2_in = tk.Entry(win)
calculate_bt = tk.Button(win, text='Calculate', command=calculate)
output = tk.Label(win)
num_1_in.pack()
operation_in.pack(pady=10)
num_2_in.pack()
calculate_bt.pack(pady=10)
output.pack()
win.mainloop()
