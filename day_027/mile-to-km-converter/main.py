from tkinter import *

FONT = ("Arial", 15, "normal")
window = Tk()
# window.minsize(width=500, height=300)
window.title("Mile to km Converter")
window.config(padx=20, pady=20)


def calculate():
    miles_input_value = miles_input.get()
    output = int(miles_input_value) * 1.609344
    result_label.config(text=round(output))


miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)
miles_input.focus()
miles_input.insert(END, string="0")


miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)


is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)


result_label = Label(text=0, font=FONT)
result_label.grid(column=1, row=1)


km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

button = Button(text="Calculate", font=FONT, command=calculate)
button.grid(column=1, row=2)













window.mainloop()