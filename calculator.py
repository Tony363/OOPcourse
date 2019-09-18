import tkinter as tk


window = tk.Tk()
window.geometry("300x200")

operators = ['+','-','*','/','=']
button = [' ','rt', 0, '**']
num, num2 = len(operators), len(button)

for i in range(num):
    operand = tk.Button(text=operators[i])
    operand.grid(column=5,row=i)

for i in range(1,4):
    for m in range(1,i+1):
        text = tk.Label(text="#")
        text.grid(column=m,row=0)
    for l in range(1, num2):
        accessory = tk.Button(text="   " + str(button[l]) + "   ")
        accessory.grid(column=l, row=4)
    for j in range(1,i+1):
        label2 = tk.Button(text="   " + str(j + 3) + "   ")
        label2.grid(column=j, row=2)
    for k in range(1,i+1):
        label3 = tk.Button(text="   " + str(k + 6) + "   ")
        label3.grid(column=k, row=3)
    label = tk.Button(text="   " + str(i) + "   ")
    label.grid(column=i, row=1)
window.mainloop()
