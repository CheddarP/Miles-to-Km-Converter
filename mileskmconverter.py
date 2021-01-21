from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km_total = miles * 1.60934
    km_result_label.config(text=km_total)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50,pady=20)

is_equal_label = Label(text="is equal to: ")
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

miles_input = Entry(width=5)
miles_input.insert(END, string="")
miles_input.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()