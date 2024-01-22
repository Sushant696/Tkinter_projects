from tkinter import *


def homePage(parent, login_status):

    homeWindow = Toplevel(parent)
    homeWindow.configure(bg="cyan")
    homeWindow.title("Home window")

    username_label = Label(homeWindow, text="Welcome to HomePage")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    if login_status == 'successful':
        parent.destroy()  # Hide the main window
        homeWindow.mainloop()
