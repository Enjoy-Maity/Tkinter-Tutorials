from posixpath import commonpath
from tkinter import *
from PIL import ImageTk,Image
import os

root=Tk()

img_list=os.listdir("images/")

for x in img_list:
    if x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".png"):
        continue
    elif x.endswith(".ico"):
        img_list.remove(x)
    else:
        img_list.remove(x)
print(img_list)

def forward(imagenum):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()          # pretty much like .delete(0,END) but specific for the grid
    my_img=ImageTk.PhotoImage(Image.open("images/{}".format(img_list[imagenum])))
    my_label=Label(root,image=my_img)
    my_label.image=my_img   # creating a reference so it does not show blank image
    my_label.grid(row=0,column=0,columnspan=3)
    print(img_list[imagenum])

    if imagenum == len(img_list)-1:
        button_forward=Button(root,text="Next >>",state=DISABLED)
    else:
        button_forward=Button(root,text="Next >>",command=lambda:forward(imagenum+1))
    button_back=Button(root,text="<< Back",command=lambda:back(imagenum-1))
    button_exit=Button(root,text="Exit",command=root.quit)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)

def back(imagenum):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_img=ImageTk.PhotoImage(Image.open("images/{}".format(img_list[imagenum])))
    my_label=Label(root,image=my_img)
    my_label.image=my_img
    my_label.grid(row=0,column=0,columnspan=3)
    if imagenum == 0:
        button_back=Button(root,text="<< Back",state=DISABLED)
    
    else:
        button_back=Button(root,text="<< Back",command=lambda:back(imagenum-1))

    button_forward=Button(root,text="Next >>",command=lambda:forward(imagenum+1))
    button_exit=Button(root,text="Exit",command=root.quit)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)

my_img=ImageTk.PhotoImage(Image.open(f"images/{img_list[0]}"))
my_label=Label(root,image=my_img)
my_label.grid(row=0,column=0,columnspan=3)

button_forward=Button(root,text="Next >>",command=lambda:forward(1))
button_forward.grid(row=1,column=2)
button_exit=Button(root,text="Exit",command=root.quit)
button_exit.grid(row=1,column=1)
button_back=Button(root,text="<< Back",command=back,state=DISABLED)
button_back.grid(row=1,column=0)

root.mainloop()