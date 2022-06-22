import tkinter as tk

window = tk.Tk()
window.title("Hello wold")
window.geometry("500x300")
#Can use .config and pad to add padding to objects
window.config(padx=20,pady=40)

#Label
hello = tk.Label(text="Hello world!", font=("Arial",14, "bold"))
hello.grid(column=0, row=0)

#Two ways to change label properties
hello["text"] = "My new text"
hello.config(text="My new text")

#Button
def button_click():
  new_text = input.get()
  hello.config(text=new_text)

button = tk.Button(text="Click me!", command=button_click)
#Use grid for more accurate, responsive placement of items. Use grid instead of pack()
button.grid(column=1, row=1)

new_button = tk.Button(text="Also click me!", command=button_click)
new_button.grid(column=2, row=0)

#Entry
input = tk.Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

tk.mainloop()
