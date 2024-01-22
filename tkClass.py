# from tkinter import *
# window = Tk()


# def add():
#     label.config(text=f"Selected: {var.get()}")


# label = Label(window, text="")
# label.pack()


# var = IntVar()  # state variable
# r1 = Radiobutton(window, text="male", variable=var, value='male', command=add)
# r1.pack(anchor=W)
# r2 = Radiobutton(window, text="female", variable=var, value='female', command=add)
# r2.pack(anchor=W)

# window.mainloop()


from tkinter import *
window = Tk()


def add():
    music = musicvar.get()
    sport = sportvar.get()
    label.config(text=f"Selected: {music} {sport}")


label = Label(window, text="")
label.pack()


musicvar = IntVar()  # state variable
sportvar = IntVar()  # state variabl

r1 = Checkbutton(window, text="music", variable=musicvar,
                 command=add)
r1.pack(anchor=W)

r2 = Checkbutton(window, text="sport", variable=sportvar,
                 command=add)
r2.pack(anchor=W)

window.mainloop()
