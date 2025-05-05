from tkinter import *


window = Tk()
window.minsize(width=500, height=400)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

# Mile Entry
mile_entry = Entry(width=15)
mile_entry.grid(column=1, row=0)

# Mile Label
mile_label = Label(text="Miles", font=("Arial", 12, "normal"))
mile_label.grid(column=2, row=0)
mile_label.config(padx=10)

equal_label = Label(text="is equal to ", font=("Arial", 12, "normal"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

km_value = Label(text="", font=("Arial", 12, "normal"))
km_value.grid(column=1, row=1)
km_value.config(padx=20, pady=10)

km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=10)


def calculate_km():
    mile = mile_entry.get()
    if not float(mile):
        return 0
    calculated_km = round(float(mile) * 1.6, 1)
    print(calculated_km)
    km_value.config(text=calculated_km)


calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)


window.mainloop()