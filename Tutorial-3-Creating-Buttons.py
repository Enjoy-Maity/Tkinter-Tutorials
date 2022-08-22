from tkinter import *

root=Tk()

def myclick():
    mylabel = Label(root, text="Look! I clicked a Button!")
    mylabel.pack()

# mybutton=Button(root,text="Click Me!",state=DISABLED) # state defines default state of the button 
# mybutton=Button(root,text="Click Me!",padx=50, pady=50) #  padx and pady  gives the spacing between the text and the outer border in xaxis and y axis respectively

# mybutton=Button(root,text="Click Me!", command=myclick) # command gives the function or method to call when clicked
mybutton=Button(root,text="Click Me!", command=myclick,fg="white",bg="red") # fg gives color to the text and bg gives color to the background
 
mybutton.pack()
root.mainloop()