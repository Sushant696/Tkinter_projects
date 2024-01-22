from tkinter import *
from register import register_form
from main import homePage

global login_status
login_status = False

def login():
    global login_status  # Declare as global to modify the global variable
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" or username == 'sushant' and password == "password" or password == 'mypassword':
        if not robot_auth_var.get():
            result_label.config(text="Human verification failed", fg="red")
        else:
            result_label.config(text='Login successful', fg='green')
            login_status = 'successful'
            home()  # Call the home function on successful login
    else:
        result_label.config(text="Login failed. Please enter valid credentials.", fg="red")

def register():
    register_form(root)  # passing the root component

def home():
    homePage(root, login_status)

# Create the main window
root = Tk()
root.configure(bg="cyan")
root.title("Login Form with Robot Authentication")

# Create and place widgets for the login window
username_label = Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

robot_auth_var = IntVar()
robot_auth_check = Checkbutton(root, text="I am not a robot", variable=robot_auth_var)
robot_auth_check.grid(row=2, columnspan=2, pady=5)

login_button = Button(root, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

register_button = Button(root, text="Register", command=register)
register_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
