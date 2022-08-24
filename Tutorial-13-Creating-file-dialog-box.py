from tkinter import *
from tkinter import filedialog
from tkinter.tix import Select
root=Tk()
root.title("Creating the file dialog box")
root.geometry("480x240")
root.iconbitmap("images/ericsson-blue-e.ico")

file=filedialog.askopenfilename(initialdir="images",title="Select a file", filetypes=(("PNG files","*.png"),("JPG files","*.jpg"),("ICO files","*.ico"),("all files","*.*")))      #filetypes creates a dropdown menu for filtering the files 
#filr=filedialog.asksaveasfilename(initialdir="images",title="Save as")     # for saving file
Label(root,text=file).pack()
root.mainloop()