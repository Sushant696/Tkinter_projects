# from tkinter import *


# def show_username():
#     """Display entered username"""
#     label_display.config(text="Entered username: " + entry_username.get())


# root = Tk()
# root.title('Interest Calculator')
# root.iconbitmap('./1.ico')
# root.maxsize(width=300, height=200)
# root.minsize(width=300, height=200)
# root.config(bg="#091")

# label_username = Text(root, text='Username:', bg="#091", fg="white")
# label_username.pack()
# entry_username = Entry(root)
# entry_username.pack(padx=10, pady=6)


# label_display = Label(root, text='', bg="#091", fg="white")
# label_display.pack()

# # Password label and entry
# label_password = Label(root, text='Password:', bg="#091", fg="white")
# label_password.pack()
# entry_password = Entry(root, show='*')
# entry_password.pack(padx=10, pady=6)

# # Button to simulate login
# login_button = Button(root, text='Login', fg="#000", command=show_username)
# login_button.pack()


# root.mainloop()


from tkinter import *


def show_username():
    """Display entered username"""
    label_display.config(text="Enter your message: " + entry_username.get())


root = Tk()
root.title('Interest Calculator')
root.iconbitmap('./1.ico')
root.maxsize(width=300, height=200)
root.minsize(width=300, height=200)
root.config(bg="#091")

# text area
messageBox = Label(root, text='Username:', bg="#091", fg="white")
messageBox.pack()
entryMessage = Text(root)
entryMessage.pack(padx=10, pady=6)


label_display = Label(root, text='', bg="#091", fg="white")
label_display.pack()


# Button to simulate login
displayButton = Button(root, text='submit', fg="#000", command=show_username)
displayButton.pack()


root.mainloop()
