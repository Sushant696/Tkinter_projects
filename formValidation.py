from tkinter import *  # import all classes and function from tkinter

root = Tk()  # Tk is a class that represent the main window of the application the playground

# pack geometry method -- organize widget in a block

root.geometry('500x400')

# Label and Entry for Username
username_label = Label(root, text='UserName')
username_label.grid(row=0, column=1)

username_entry = Entry(root)
username_entry.grid(row=0, column=2)

# Label and Entry for Password
password_label = Label(root, text='Password')
password_label.grid(row=1, column=5)

password_entry = Entry(root)
password_entry.grid(row=1, column=6)
button = Button(root,text='Click me').grid(row = 4, column = 5)

# button.pack(side=TOP,fill = X , expand = True)


root.mainloop()  # This starts the main loop. This loop runs indefinitely until the user closes the application window. The event loop is responsible for handling user inputs, events, and updating the GUI


# tkinter provider 3 geometry managers to arranging things within a container
