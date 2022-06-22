import tkinter as tk
window = tk.Tk()
window.title("Miles to kilometres converter")
window.geometry("300x100")
window.config(padx=10,pady=10)
kilometres = 0

hello = tk.Label(text="Miles")
inputField = tk.Entry()
inputField.grid(column=2,row=0)
hello.grid(column=3,row=0)

equalTo = tk.Label(text="is equal to")
equalTo.grid(column=1, row=1)

kiloText = tk.Label(text=str(kilometres))
kiloText.grid(column=2,row=1)

km = tk.Label(text="km")
km.grid(column=3,row=1)

def buttonClick():
    kilometres = 1.6 * float(inputField.get())
    kiloText.config(text=str(kilometres))

calculate = tk.Button(text="Calculate!", command=buttonClick)
calculate.grid(column=2,row=2)

window.mainloop()
