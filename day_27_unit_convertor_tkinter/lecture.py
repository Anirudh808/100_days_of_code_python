from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Buttons
def button_clicked():
    print("I got clicked!")
    new_text = input_entry.get()
    my_label["text"] = new_text


button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input_entry = Entry(width=20)
input_entry.grid(column=3, row=2)


window.mainloop()
