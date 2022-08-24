from doctest import OPTIONFLAGS_BY_NAME
from tkinter import *

root=Tk()
root.title("Creating the dropdown menus")
root.iconbitmap("images/ericsson-blue-e.ico")
root.geometry("480x240")

# drop down boxes
def show():
    Label(root,text=clicked.get()).pack()

"""
# we can add all the menu options for the dropdown menu
clicked=StringVar()
clicked.set("Select an option")     # gives default value to the dropdown menu
drop=OptionMenu(root,clicked,"Select an option","Monday","Tuesday","Thursday","Friday","Saturday").pack()

"""

# we can also make the options in the option menu to be a list to make the code easy to read and convinient to edit
options_available=["Monday","Tuesday","Thursday","Friday","Saturday"]

clicked=StringVar()
clicked.set("Select an option")     # gives default value to the dropdown menu
drop=OptionMenu(root,clicked,*options_available).pack()     # without the star in fromt of options_available list will not work as the intended way and will give the tuple of all the items in the list

button=Button(root,text="Click me to show the chose option",command=show).pack()

root.mainloop()