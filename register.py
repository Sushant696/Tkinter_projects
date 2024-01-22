from tkinter import *

def register_form(parent):
    register_window = Toplevel(parent)
    register_window.configure(bg="cyan")
    register_window.title("Registration Form")

    # Add widgets for the registration window
    username_label = Label(register_window, text="New Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    username_entry = Entry(register_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = Label(register_window, text="New Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    password_entry = Entry(register_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def register():
        # Perform registration logic here
        
        # Close the registration window
        register_window.destroy()

    register_button = Button(register_window, text="Register", command=register)
    register_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Run the registration window
    parent.destroy()  # Hide the main window
    register_window.mainloop()
