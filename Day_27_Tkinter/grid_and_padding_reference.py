import tkinter

"""Reference for widget.grid() and widget padx, pady parameters"""


def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    label.config(text=new_text)


window = tkinter.Tk()
window.title("Tkinter Project")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text="I'm a label.")
label.grid(row=0, column=0)
label.config(padx=50, pady=50)

button = tkinter.Button(text="Button", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=0, column=2)

entry = tkinter.Entry()
entry.grid(row=2, column=3)

tkinter.mainloop()
