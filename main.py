from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 1)
    label_3.config(text=f"{ km}")

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=30, pady=30)

miles_input = Entry(width=10)
miles_input.grid(column=1, row= 0)

label_1 = Label(text= " Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text= "is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text= "0")
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

button = Button(text= "Calculate", command= miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
