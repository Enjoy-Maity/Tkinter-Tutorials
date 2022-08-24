from os import popen
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Message Box")
root.iconbitmap("images/ericsson-blue-e.ico")

# messagebox disply types: showinfo("<title>","<info>"), showerror("<title>","<error>"), askquestion("<title>","<question>"), askokcancel("<title>","<question>"), askyesno("<title>","<question>")     

def popup():
    # messagebox.showinfo("You clicked the button","Succesfully clicked the button!")       # gives info after the i icon and it returns ok to the variable
    # messagebox.showwarning("You clicked the button","Succesfully clicked the button!")    # gives warning after the traingular danger sign icon and it returns ook to the variable
    # messagebox.showerror("You clicked the button","Succesfully clicked the button!")      # gives the error after the cross sign icon and it returns ok to the variable
    # messagebox.askquestion("You clicked the button","Succesfully clicked the button!")    # gives the question after the question mark icon and by default gives yes or no button and returns yes or no to the variable
    # messagebox.askokcancel("You clicked the button","Succesfully clicked the button!")    # gives the question after the question mark icon and gives only ok or cancel button and  returns 1 or 0 to the variable
    # messagebox.askyesno("You clicked the button","Succesfully clicked the button!")       # gives the question after the question mark icon and gives only yes or no button and return 1 or 0 to the variable

    response=messagebox.askyesno("You clicked the button","Succesfully clicked the button!") # messagebox returns the value of button clicked to the variable, and we're using variable to hold the value so that we can use it in other statements
    if response==1:
        Label(root,text="You clicked the yes button!").pack()
    if response==0:
        Label(root,text="You clicked the no button!").pack()
Button(root,text="Click me!",command=popup).pack(padx=50,pady=20)
root.mainloop()