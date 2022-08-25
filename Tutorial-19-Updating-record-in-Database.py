from tkinter import *
import sqlite3

root=Tk()
root.title("    Deleting a record from database")
root.iconbitmap("images/ericsson-logo.ico")
root.geometry("490x520")

def update(record_id):
    conn=sqlite3.connect("address.db")

    #   Creating a cursor : a cursor is used to execute the commands for us so that the code doesn't come to us to manually execute the command
    c=conn.cursor()

    c.execute("""UPDATE address SET 
    first_name=:f_name,
    last_name=:l_name,
    city=:city,
    state=:state,
    pincode=:pincode
    
    WHERE oid = :oid""",
    {'f_name':f_name.get(),
    'l_name':l_name.get(),
    'city':city.get(),
    'state':state.get(),
    'pincode':pincode.get(),
    'oid':record_id
    })

    f_name.delete(0,END)
    l_name.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    pincode.delete(0,END)

    conn.commit()
    conn.close()


def edit():
    record_id=del_box.get()
    root.destroy()
    editor=Tk()
    editor.title("  Updating a record")
    editor.iconbitmap("images/ericsson-logo.ico")
    editor.geometry("490x520")
    conn=sqlite3.connect("address.db")

    #   Creating a cursor : a cursor is used to execute the commands for us so that the code doesn't come to us to manually execute the command
    c=conn.cursor()
    c.execute("SELECT *,oid FROM address WHERE oid="+record_id)
    records=c.fetchall()    # c.fetchone() fetches only one record , c.fetchmany(<number>) fetches the <number> of records, c.fetchall() fteches all the records
    
    # query_label=Label(text=print_records)
    # query_label.grid(row=12,column=0,columnspan=2,pady=10,ipadx=100)
    global f_name;f_name=Entry(editor,width=20)
    f_name.grid(row=0,column=1, padx=20)        # in entry case we can't write grid with the entry variable declaration so we need to define grid in next line as grid returns None value
    f_name_labl=Label(editor,text="First Name").grid(row=0,column=0)

    global l_name;l_name=Entry(editor,width=20)
    l_name.grid(row=1,column=1)
    l_name_labl=Label(editor,text="Last Name").grid(row=1,column=0)

    global city;city=Entry(editor,width=20)
    city.grid(row=2,column=1)
    city_labl=Label(editor,text="City").grid(row=2,column=0)

    global state;state=Entry(editor,width=20)
    state.grid(row=3,column=1)
    state_labl=Label(editor,text="State").grid(row=3,column=0)

    global pincode;pincode=Entry(editor,width=20)
    pincode.grid(row=4,column=1)
    pincode_labl=Label(editor,text="Pincode").grid(row=4,column=0)

    # looping through the records
    for record in records:
        f_name.insert(0,record[0])
        l_name.insert(0,record[1])
        city.insert(0,record[2])
        state.insert(0,record[3])
        pincode.insert(0,record[4])



    btn=Button(editor,text="Click Me to add data to database",command=submit).grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=90) # *ipady is used to stretch the button

    query_btn=Button(editor,text="Click me to show all the records",command=query).grid(row=6,column=0,columnspan=2,pady=10,ipadx=90,padx=10)
    #print(record_id)
    save_btn=Button(text="Click me to edit or update a record",command=lambda:update(record_id))
    save_btn.grid(row=18,column=0,columnspan=2,pady=10,ipadx=90)

    conn.commit()
    conn.close()

    editor.mainloop()


def delete():
    
    conn=sqlite3.connect("address.db")

    #   Creating a cursor : a cursor is used to execute the commands for us so that the code doesn't come to us to manually execute the command
    c=conn.cursor()


    f_name.delete(0,END)
    l_name.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    pincode.delete(0,END)

    c.execute("DELETE FROM address WHERE oid= "+del_box.get())
    conn.commit()   # commit saves all the manipulation to the database we are doing in the above code
    conn.close()    # closing the database


def submit():
    # we always need to define the connection to the DB inside the function 
    conn=sqlite3.connect("address.db")

    #   Creating a cursor : a cursor is used to execute the commands for us so that the code doesn't come to us to manually execute the command
    c=conn.cursor()

    c.execute("INSERT INTO address VALUES(:f_name,:l_name,:city,:state,:pincode)",
        {'f_name':f_name.get(),
        'l_name':l_name.get(),
        'city':city.get(),
        'state':state.get(),
        'pincode':pincode.get()}

    )
    conn.commit()
    f_name.delete(0,END)
    l_name.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    pincode.delete(0,END)

    conn.commit()   # commit saves all the manipulation to the database we are doing in the above code
    conn.close()    # closing the database

# Create query
def query():
    conn=sqlite3.connect("address.db")

    #   Creating a cursor : a cursor is used to execute the commands for us so that the code doesn't come to us to manually execute the command
    c=conn.cursor()
    c.execute("SELECT *,oid FROM address")
    records=c.fetchall()    # c.fetchone() fetches only one record , c.fetchmany(<number>) fetches the <number> of records, c.fetchall() fteches all the records
    # print(records)

    print_records=""
    for record in records:
        print_records+=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+" "+str( record[5])+ "\n"
    
    query_label=Label(text=print_records)
    query_label.grid(row=12,column=0,columnspan=2,pady=10,ipadx=100)
    conn.commit()   # commit saves all the manipulation to the database we are doing in the above code
    conn.close()    # closing the database




f_name=Entry(root,width=20)
f_name.grid(row=0,column=1, padx=20)        # in entry case we can't write grid with the entry variable declaration so we need to define grid in next line as grid returns None value
f_name_labl=Label(root,text="First Name").grid(row=0,column=0)

l_name=Entry(root,width=20)
l_name.grid(row=1,column=1)
l_name_labl=Label(root,text="Last Name").grid(row=1,column=0)

city=Entry(root,width=20)
city.grid(row=2,column=1)
city_labl=Label(root,text="City").grid(row=2,column=0)

state=Entry(root,width=20)
state.grid(row=3,column=1)
state_labl=Label(root,text="State").grid(row=3,column=0)

pincode=Entry(root,width=20)
pincode.grid(row=4,column=1)
pincode_labl=Label(root,text="Pincode").grid(row=4,column=0)




btn=Button(root,text="Click Me to add data to database",command=submit).grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=90) # *ipady is used to stretch the button

query_btn=Button(root,text="Click me to show all the records",command=query).grid(row=6,column=0,columnspan=2,pady=10,ipadx=90,padx=10)

del_box=Entry(root,width=30)
del_box.grid(row=8,column=0)


# Create a delete button

del_btn=Button(root,text="Click me to delete a record",command=delete)
del_btn.grid(row=9,column=0,columnspan=2,pady=10,ipadx=90)


del_label=Label(root,text="ID Number")
del_label.grid(row=8,column=1,columnspan=2,pady=10,ipadx=40)


# create update button

update_btn=Button(root,text="Click me to edit or update a record",command=edit)
update_btn.grid(row=10,column=0,columnspan=2,pady=10,ipadx=90)
root.mainloop()