import tkinter as tk
import webbrowser

#event handler function
def goku (event):
    print("You have Super Saiyan God Goku")

def vegeta (event):
    print("you have Super Saiyan God vegeta")

def open_cp(event):
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=YJHjjsckD30")

def open_cp2(event):
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=0QAN9fAQYEI")

window = tk.Tk()
window.geometry("400x400")

alabel = tk.Label(text="ssg goku")
alabel.grid(column=0,row=0)

blabel = tk.Label(text="ssg vegeta")
blabel.grid(column=1,row=0)

button = tk.Button(window, text="download")
button.grid(column=0)

button2 = tk.Button(window, text="download")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="View")
button3.grid(column=0)

button4 = tk.Button(window, text="View ")
button4.grid(column=1, row=2)

# bind is for your mouse and makes function work
button.bind("<Button-1>",goku)
button2.bind("<Button-1>",vegeta)
button3.bind("<Button-1>",open_cp)
button4.bind("<Button-1>",open_cp2)

window.mainloop()