from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

def button_clicked():
    my_label["text"] = form.get()

my_label = Label(text="Hi there", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


form = Entry(width=10)
form.grid(column=3, row=2)




window.mainloop()