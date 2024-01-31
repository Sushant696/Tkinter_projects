from tkinter import *
import sqlite3

root = Tk()
root.title("Employee Management System")
lbl = Label(root, text="Employee Management System", font=("Arial", 50))
lbl.place(x=200, y=0)
root.geometry("1500x1000")
root.resizable(False, False)

all_employee_details = ""

label_Username = Label(root, text="Username", font=("Arial", 20))
label_Address = Label(root, text="Address", font=("Arial", 20))
label_Role = Label(root, text="Role", font=("Arial", 20))
label_Salary = Label(root, text="Salary", font=("Arial", 20))
label_Delete = Label(root, text="Delete Record", font=("Arial", 20))
label_Update = Label(root, text="Update Record", font=("Arial", 20))
all_employee_details_label = Label(text="")


def add_data():
    username_value = username.get()
    address_value = address.get()
    role_value = role.get()
    salary_value = salary.get()

    conn = sqlite3.connect("database.db")
    db = conn.cursor()

    db.execute(
        """INSERT INTO employee(userName, address, role, salary) 
        VALUES (?, ?, ?, ?)""",
        (username_value, address_value, role_value, salary_value),
    )
    conn.commit()
    conn.close()

    retrieve()

    username.delete(0, END)
    address.delete(0, END)
    role.delete(0, END)
    salary.delete(0, END)


def retrieve():
    global all_employee_details
    all_employee_details = ""
    conn = sqlite3.connect("database.db")
    db = conn.cursor()

    db.execute("SELECT * FROM employee")

    records = db.fetchall()

    for record in records:
        employeeDetails = ""
        for data in record:
            employeeDetails = employeeDetails + " " + str(data)
        all_employee_details = all_employee_details + "\n" + employeeDetails
    all_employee_details_label.config(text=all_employee_details)
    conn.close()


def delete():
    global all_employee_details
    all_employee_details = ""
    conn = sqlite3.connect("database.db")
    db = conn.cursor()

    db.execute("DELETE FROM employee WHERE employeeId =" + delete_box.get())
    conn.commit()
    conn.close()

    retrieve()

    delete_box.delete(0, END)


def edit():
    global editor
    editor = Tk()
    editor.title("Update Data")
    editor.geometry("370x480")
    editor.resizable(False, False)

    global username_editor
    global address_editor
    global role_editor
    global salary_edtior

    conn = sqlite3.connect("database.db")
    db = conn.cursor()

    db.execute("SELECT * FROM employee WHERE employeeId =" + update_box.get())

    record = db.fetchone()

    username_editor = Entry(editor, width=30)
    address_editor = Entry(editor, width=30)
    role_editor = Entry(editor, width=30)
    salary_edtior = Entry(editor, width=30)

    username_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    address_editor.grid(row=1, column=1)
    role_editor.grid(row=2, column=1)
    salary_edtior.grid(row=3, column=1)

    username_editor.insert(0, record[1])
    address_editor.insert(0, record[2])
    role_editor.insert(0, record[3])
    salary_edtior.insert(0, record[4])

    username_label = Label(editor, text="Username")
    username_label.grid(row=0, column=0, pady=(10, 0))

    address_label = Label(editor, text="Address")
    address_label.grid(row=1, column=0)

    role_label = Label(editor, text="Role")
    role_label.grid(row=2, column=0)

    salary_label = Label(editor, text="Salary")
    salary_label.grid(row=3, column=0)

    def update_data():
        conn = sqlite3.connect("database.db")
        db = conn.cursor()

        db.execute(
            """
        UPDATE employee
        SET userName = ?, address = ?, role = ?, salary = ?
        WHERE employeeId = ?
        """,
            (
                username_editor.get(),
                address_editor.get(),
                role_editor.get(),
                salary_edtior.get(),
                update_box.get(),
            ),
        )

        conn.commit()
        conn.close()
        editor.destroy()
        update_box.delete(0, END)
        retrieve()

    edit_button = Button(editor, text="SAVE", command=update_data)
    edit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


username = Entry(root, width=30)
address = Entry(root, width=30)
role = Entry(root, width=30)
salary = Entry(root, width=30)
delete_box = Entry(root, width=25)
update_box = Entry(root, width=25)

add_button = Button(text="Add Record", command=add_data)
retrieve_button = Button(text="Retrieve", command=retrieve)
delete_button = Button(text="Delete Record", command=delete)
update_button = Button(text="Update Record", command=edit)

label_Username.place(x=10, y=100)
label_Address.place(x=10, y=150)
label_Role.place(x=10, y=200)
label_Salary.place(x=10, y=250)
label_Delete.place(x=10, y=370)
label_Update.place(x=10, y=420)
all_employee_details_label.place(y=100, x=800)

username.place(x=170, y=100, height=30)
address.place(x=170, y=150, height=30)
role.place(x=170, y=200, height=30)
salary.place(x=170, y=250, height=30)
delete_box.place(x=200, y=370, height=30)
update_box.place(x=200, y=420, height=30)
add_button.place(x=170, y=300)
retrieve_button.place(x=320, y=300)
delete_button.place(x=420, y=370)
update_button.place(x=420, y=420)


conn = sqlite3.connect("database.db")
db = conn.cursor()

db.execute(
    """
CREATE TABLE IF NOT EXISTS employee(
employeeId INTEGER PRIMARY KEY AUTOINCREMENT,
userName varchar(255) NOT NULL,
address varchar(255) NOT NULL,
role varchar(255) NOT NULL,
salary varchar(255) NOT NULL
)
"""
)
conn.commit()
conn.close()
retrieve()
root.mainloop()