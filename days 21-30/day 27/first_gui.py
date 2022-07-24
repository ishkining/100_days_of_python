import tkinter

my_window = tkinter.Tk()
my_window.config(width=300, height=200, padx=15, pady=20)
my_window.title("Mein first GUI")

# TODO 1: Make all Labels

label1 = tkinter.Label(text='is equal to', padx=10, pady=10)
label1.grid(column=0, row=1)

label2 = tkinter.Label(text='miles', padx=10, pady=10)
label2.grid(column=2, row=0)

label3 = tkinter.Label(text='km', padx=10, pady=10)
label3.grid(column=2, row=1)

label_of_result = tkinter.Label(text='0', padx=10, pady=10)
label_of_result.grid(column=1, row=1)

# TODO 2: Make Entry

entry_of_miles = tkinter.Entry(width=10)
entry_of_miles.grid(column=1, row=0)


# TODO 3: Make Button and onclick function

def convert_miles_to_km():
    label_of_result.config(text=str(int(float(entry_of_miles.get()) * 1.6)))


button_convert_miles = tkinter.Button(text='Calculate', command=convert_miles_to_km)
button_convert_miles.grid(column=1, row=2)

my_window.mainloop()