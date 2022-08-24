from tkinter import *

root=Tk()

root.title("Adding Frame") 
root.iconbitmap("images/ericsson-blue-e.ico")
frame=LabelFrame(root,padx=100,pady=10)  # Here padding gives the spacing inside the tkinter frame
frame2=LabelFrame(root,text="this is second frame",padx=100,pady=10) 
frame.pack(padx=10,pady=10)
frame2.pack(padx=100,pady=100)

b=Button(frame,text="Click me!")
b.grid(row=0,column=0,padx=5,pady=5)
b2=Button(frame2,text="Click me 2nd frame!")
b2.grid(row=1,column=0,padx=5,pady=5)

root.mainloop()