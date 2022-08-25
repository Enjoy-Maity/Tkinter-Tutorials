from os import stat
from tkinter import *
import sqlite3

root=Tk()
root.title("Using databases")
root.iconbitmap("images/ericsson-blue-e.ico")
root.geometry("480x240")

#   Databases

#   Creating a database or connecting to pre-existing one
# conn=sqlite3.connect("address.db")

# #   Creating a cursor : a cursor is used to execute the commands for us so that the code doesn't come to us to manually execute the command
# c=conn.cursor()

# create table 
# Sqlite has 5 datatypes :- 1. text     2. integers     3. real (real nos. i.e float)   4. blobs (image file,video file)    5. Null
# c.execute("""
# CREATE TABLE address(
#     first_name text,
#     last_name text,
#     city text,
#     state text,
#     pincode integer
# )

# """)

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
        print_records+=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+ "\n"
    
    query_label=Label(root,text=print_records)
    query_label.grid(row=7,column=0,columnspan=2,pady=10,ipadx=100)
    root.geometry("480x520")
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




btn=Button(root,text="Click Me to add data to database",command=submit).grid(row=5,column=0,columnspan=2,pady=10,ipadx=100) # *ipady is used to stretch the button

query_btn=Button(root,text="Click me to show all the records",command=query).grid(row=6,column=0,columnspan=2,pady=10,ipadx=100)
root.mainloop()