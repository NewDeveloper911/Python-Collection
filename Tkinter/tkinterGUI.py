import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

hello = tk.Label(text="Hello world!",font=("Arial",24,"bold"))
hello.pack()

'''
    #Allows a window to get input from a window
    input = tk.Entry(width = 15)
    input.pack()
    #Needs to be event-triggered
'''


#Text works like Entry but allows for a larger input box for more text
text = tk.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tk.END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", tk.END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    minimum_value = 0
    maximum_value = 10
    if spinbox.get() >= minimum_value and spinbox.get() <= maximum_value:
        print(spinbox.get())
    
spinbox = tk.Spinbox(from_=minimum_value, to=maximum_value, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
    
#variable to hold on to checked state, 0 is off, 1 is on.
#IntVar is used to store integer values which can be gained or set
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobuttons work like MCQ choices. If one is selected, the others are turned off
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    #Behaves like a dictionary
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

#Button function triggered when a button is clicked
clicked = False
def button_click():
    global clicked
    if clicked == False:
        hello.config(text="Button got clicked")
        clicked = True
    else:
        hello.config(text="My new text")
        clicked = False

    #Input.get() only seems to work when triggered by an event, such as clicking a button
    hello.config(text=input.get())

button = tk.Button(text="Click me!", command=button_click)
button.pack()

#There are two ways to change label properties on a window
hello.config(text="My new text")
hello["text"] = "My new text"

#Checks for user input and refreshes the window accordingly
tk.mainloop()
