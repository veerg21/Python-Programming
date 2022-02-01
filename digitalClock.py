from tkinter import *
from time import strftime
root=Tk()
root.title("Digital Clock")
root.configure(background="gold")
root.geometry("400x250+100+100")
def clock():
    # print(strftime("%X"))
    tick=strftime("%X")
    label.config(text=tick)
    label.after(1000, clock)
label1=Label(root, font=("Arial", 72), text="Clock", background="silver", foreground="magenta")
label=Label(root, font=("Arial", 72), background="silver", foreground="magenta")
label1.pack()
label.pack()
# label.place(x=100, y=100)
# label.grid(row=1, column=2)
clock()
root.mainloop()