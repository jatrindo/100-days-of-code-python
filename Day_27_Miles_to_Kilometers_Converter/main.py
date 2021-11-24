import tkinter as tk


def calculate():
    miles = entry.get()
    if miles:
        result = round(int(miles) * 1.689, 2)
        output_label.config(text=result)


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

entry = tk.Entry(width=7)
entry.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

equalto_label = tk.Label(text="is equal to")
equalto_label.grid(row=1, column=0)

output_label = tk.Label(text="0")
output_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

calc_button = tk.Button(text="Calculate", command=calculate)
calc_button.grid(row=2, column=1)

tk.mainloop()
