from tkinter import *

root=Tk()
root.title("Radio Buttons")
root.iconbitmap("images/ericsson-blue-e.ico")

#   to create single radio button Radiobutton(root, text="<text>",variable=<variable>,value=<value>).pack(anchor=W)
# to create multiple radio buttons we can do 

# first create a list or iterable collection with text and values
mode=[("pepperoni","pepperoni"),("cheese","cheese"),("mushroom","mushroom"),("onion","onion")]

pizza=StringVar()
pizza.set("pepperoni")

for text,value in mode:
    Radiobutton(root,text=text,variable=pizza,value=value).pack(anchor=W)

def clicked(value):
    Label(root,text=value).pack(anchor=E)

Button(root,text="Click Me!",command=lambda:clicked(pizza.get())).pack()
root.mainloop()