from tkinter import *

def login():
    username = username_entry.get() #getting user input using get metho
    password = password_entry.get()

    # Simple validation for demonstration purposes
    if username == "admin" and password == "password" and not robot_auth_var.get(): #if checked robot_auth_var.get returns 1 otherwise 0
        result_label.config(text="Login successful!", fg="green")
    else:
        result_label.config(text="Login failed. Please confirm that you are not a robot.", fg="red")

# Create the main window
root = Tk()
root.title("Login Form with Robot Authentication")

# Create and place widgets
username_label = Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

password_entry = Entry(root, show="*")  # Use show="*" to hide password
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Checkbox for robot authentication
robot_auth_var = IntVar()
robot_auth_check = Checkbutton(root, text="I am not a robot", variable=robot_auth_var)
robot_auth_check.grid(row=2, columnspan=2, pady=5)

login_button = Button(root, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Start the main loop
root.mainloop()


# intVar is a special variable that can be associated with widget like radio button and check buttons. This stored the state of the widget