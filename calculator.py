import tkinter as tk
from tkinter import *


window = tk.Tk()
window.geometry("900x400")

# def button_click(number):
#     print(number)

# operators = ['+','-','*','/','=']
# button = [' ','rt', 0, '**']
# num, num2 = len(operators), len(button)

# for i in range(num):
#     operand = tk.Button(text=operators[i])
#     operand.grid(column=5,row=i)

# for i in range(1,4):
#     # dic = {}
#     # dic.append(i)
#     for m in range(1,i+1):
#         text = tk.Label(text="#")
#         text.grid(column=m,row=0)
#     for l in range(1, num2):
#         accessory = tk.Button(window,text="   " + str(button[l]) + "   ",command=lambda:button_click(button[l]))
#         accessory.grid(column=l, row=4)
#     for j in range(1,i+1):
#         label2 = tk.Button(window,text="   " + str(j + 3) + "   ",command=lambda:button_click(j + 3))
#         label2.grid(column=j, row=2)
#     for k in range(1,i+1):
#         label3 = tk.Button(window,text="   " + str(k + 6) + "   ",command=lambda:button_click(k + 6))
#         label3.grid(column=k, row=3)
#     label = tk.Button(window,text="   " + str(i) + "   ",command=lambda:button_click(i))
#     label.grid(column=i, row=1)
#     # label.bind("<Button-1>", one)
    
    #label = tk.Button(window,text="   " + str(i) + "   ",command=lambda:button_click(i))
    #label.grid(column=i, row=1)
    # label.bind("<Button-1>", one)
buttons = [
    ['box','','','',],
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-',],
    ['7', '8', '9', '*',],
    ['=', '0', '**','/'],
    ]
trash = []
string = []
def create_button_action(button_name):
    def button_action():
        e.delete(0, END)
        string.append(button_name)
        
        try:
            num_value = int(button_name)
        except ValueError: # you know it's one of the operators
            if button_name == "=":
                string.pop()
                e.insert(0 ,eval("".join(string)))
            if button_name == "/":
                string.clear()
            pass
        e.insert(0,button_name)      
    return button_action

for r, row in enumerate(buttons):
    for c, button_name in enumerate(row):
        if button_name == ' ':
            label = tk.Label(window,text="  #  ")
            label.grid(column=c, row=r)
        elif button_name == '':
            trash.append(button_name)
        elif button_name == 'box':
            trash.append(button_name)
            # e = Entry(window)
            # e.grid(column=c, row=r)
   
        else:
            accessory = tk.Button(window, text=button_name, padx=60, pady=20, command=create_button_action(button_name))
            accessory.grid(column=c, row=r)

e = Entry(window, width=35, borderwidth=5)
e.grid(column=0, row=0, columnspan=5)

window.mainloop()
