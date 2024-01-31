from tkinter import *
import sqlite3

root = Tk()
root.title("Employee Management System")
root.geometry("800x600")
root.resizable(0, 0)

connect = sqlite3.connect('employee.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employee(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,

               uname        TEXT,
               adr          TEXT,
               rl           TEXT,
               slr          INT
)""")

connect.commit()
connect.close()


def add():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    c.execute("INSERT INTO employee(uname, adr, rl, slr) VALUES(?,?,?,?)",
              (username.get(), address.get(), role.get(), salary.get()))
    conn.commit()
    conn.close()
    username.delete(0, END)
    address.delete(0, END)
    role.delete(0, END)
    salary.delete(0, END)
    retrieve_records()


def delete():

    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    #
    #  c.execute("DELETE FROM employee WHERE ID=" + delete_box.get())
    c.execute("DELETE FROM employee WHERE ID =" + delete_box.get())

    conn.commit()
    conn.close()
    retrieve_records()
    delete_box.delete(0, END)



def retrieve_records():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()
    # execute a SELECT query to  retrieve all records from the 'employee' table
    c.execute("SELECT *FROM employee")

    # fetch all records returned by the query

    records = c.fetchall()
    print_records = ''

    for record in records:
        print_records += (
            f"id:{record[0]} name:{record[1]} \n Address : {record[2]},\n Role: {record[3]},\n Salary: {record[4]}\n\n\n"
        )

    query_label = Label(root, text=print_records)
    query_label.place(x=450, y=40)
    conn.close()


def update():

    global editor
    editor = Tk()
    editor.title("update Data")
    editor.geometry('300x400')
    conn = sqlite3.connect('employee.db')
    c = conn.cursor()
    record_id = update_box.get()
    c.execute('SELECT * FROM  employee WHERE ID=?', (record_id,))
    records = c.fetchall()
    print(records)

    global username_editor
    global address_editor
    global role_editor
    global salary_editor

    username_editor = Entry(editor, width=30)
    username_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=1, column=1)

    role_editor = Entry(editor, width=30)
    role_editor.grid(row=2, column=1)

    salary_editor = Entry(editor, width=30)
    salary_editor.grid(row=3, column=1)


# lables
    username_label = Label(editor, text='username')
    username_label.grid(row=0, column=0, pady=(10, 0))

    address_label = Label(editor, text='address')
    address_label.grid(row=1, column=0)

    role_label = Label(editor, text='role')
    role_label.grid(row=2, column=0)

    salary_label = Label(editor, text='salary')
    salary_label.grid(row=3, column=0)

    for record in records:
        username_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        role_editor.insert(0, record[3])
        salary_editor.insert(0, record[4])

# button

    update_button = Button(editor, text='Update',
                           command=lambda: updateData(record_id))
    update_button.grid(row=6, column=0, columnspan=2,
                       pady=10, padx=10, ipadx=125)


def updateData(record_id):
    conn = sqlite3.connect('employee.db')

    c = conn.cursor()
    c.execute('''
    UPDATE employee SET 
        uname     =:u,
        adr         = :a,
        rl          =:r,
        slr         =:s
        WHERE ID = :id
    ''',
              {
                  'u': username_editor.get(),
                  'a': address_editor.get(),
                  'r': role_editor.get(),
                  's': salary_editor.get(),
                  'id': record_id,
              })

    conn.commit()
    conn.close()
    editor.destroy()
    retrieve_records()


# Labels
Label(root, text="Username", font=("Arial Bold", 14)).grid(
    row=0, column=0, padx=10, pady=10, sticky=W)
Label(root, text="Address", font=("Arial Bold", 14)).grid(
    row=1, column=0, padx=10, pady=10, sticky=W)
Label(root, text="Role", font=("Arial Bold", 14)).grid(
    row=2, column=0, padx=10, pady=10, sticky=W)
Label(root, text="Salary", font=("Arial Bold", 14)).grid(
    row=3, column=0, padx=10, pady=10, sticky=W)
# Label(root, text="Delete Record", font=("Arial Bold", 14)).grid(
#     row=7, column=0, padx=10, pady=10, sticky=W)

# Entry widgets
username = Entry(root, width=30)
username.grid(row=0, column=1, pady=10)

address = Entry(root, width=30)
address.grid(row=1, column=1, pady=10)

role = Entry(root, width=30)
role.grid(row=2, column=1, pady=10)

salary = Entry(root, width=30)
salary.grid(row=3, column=1, pady=10)

delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=2, pady=10)

update_box = Entry(root, width=30)
update_box.grid(row=9, column=2, pady=10)

# Buttons
Button(root, text="Add", font=("Arial Bold", 14), command=add).grid(
    row=4, column=0, columnspan=2, pady=10)
Button(root, text="Retrieve", font=("Arial Bold", 14),
       command=retrieve_records).grid(row=4, column=1, columnspan=2, pady=10)
Button(root, text="Delete", font=("Arial Bold", 14), command=delete).grid(
    row=8, column=0, columnspan=2, pady=10)
Button(root, text="Update", font=("Arial Bold", 14), command=update).grid(
    row=9, column=0, columnspan=2, pady=10)

root.mainloop()
