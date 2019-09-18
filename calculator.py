import tkinter as tk


window = tk.Tk()
window.geometry("300x200")

def button_click(number):
    print(number)



operators = ['+','-','*','/','=']
button = [' ','rt', 0, '**']
num, num2 = len(operators), len(button)

for i in range(num):
    operand = tk.Button(text=operators[i])
    operand.grid(column=5,row=i)

for i in range(1,4):
    dic = {}
    dic.append(i)
    for m in range(1,i+1):
        text = tk.Label(text="#")
        text.grid(column=m,row=0)
    for l in range(1, num2):
        accessory = tk.Button(window,text="   " + str(button[l]) + "   ",command=lambda:button_click(button[l]))
        accessory.grid(column=l, row=4)
    for j in range(1,i+1):
        label2 = tk.Button(window,text="   " + str(j + 3) + "   ",command=lambda:button_click(j + 3))
        label2.grid(column=j, row=2)
    for k in range(1,i+1):
        label3 = tk.Button(window,text="   " + str(k + 6) + "   ",command=lambda:button_click(k + 6))
        label3.grid(column=k, row=3)
    label = tk.Button(window,text="   " + str(i) + "   ",command=lambda:button_click(i))
    label.grid(column=i, row=1)
    # label.bind("<Button-1>", one)

window.mainloop()
