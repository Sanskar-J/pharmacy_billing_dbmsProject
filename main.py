from tkinter import *
from data import *
from tkinter import ttk
from datetime import datetime
import random
from PIL import ImageTk, Image
import os
import tkinter.font as font

print("dbms project")
selected_items = []
r = random.randint(10000, 999999)
print(r)


# Showing the list of deleted items
def saldellist(tree):
    tree.delete(*tree.get_children())
    rows = get_all_deleted()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))


# View deleted bills
def deleted_bills(tab_main, username):
    t = Frame(tab_main, background="white")
    tree = ttk.Treeview(t)
    b = Button(t, text="SHOW", command=lambda: saldellist(
        tree), fg="black", bg="white")
    tree["columns"] = ("one", "two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("one", text="EMPLOYEE ID")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b.pack()
    tree.pack()
    return t


# Check and delete bill
def delete_bill(ref):
    if ref and ref.isnumeric():
        delete_bill_db(int(ref))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Showing the list of sales for specific user
def sal_del(tree, username):
    tree.delete(*tree.get_children())
    rows = get_all_sales_related(int(username))
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[2], i[3]))


# Remove bill
def remove_bill(tab_main, username):
    t = Frame(tab_main, background="white")
    l = Label(t, text="ENTER REFNO:", fg="black", bg="white")
    e = Entry(t)
    b = Button(t, text="DELETE", fg="black", bg="white",
               command=lambda: delete_bill(e.get()))
    l.pack()
    e.pack()
    b.pack()
    tree = ttk.Treeview(t)
    tree["columns"] = ("two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b = Button(t, text="SHOW", command=lambda: sal_del(
        tree, username), fg="black", bg="white")
    b.pack()
    tree.pack()
    return t


# Check and edit price
def ck_and_edit_price(item, price):
    if item and price.isnumeric():
        update_price(item, int(price))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Change price of item
def change_price_of_item(tab_main, username):
    t = Frame(tab_main, background="white")
    rows = get_items()
    options = []
    for i in rows:
        options.append(i[1])
    clicked = StringVar()
    if(len(options)):
        clicked.set(options[0])
        drop = OptionMenu(t, clicked, *options)
        l = Label(t, text="ENTER NEW PRICE:", fg="black", bg="white")
        c = Entry(t)
        b = Button(t, text="UPDATE PRICE", command=lambda: ck_and_edit_price(
            clicked.get(), c.get()), fg="black", bg="white")
        drop.pack()
        l.pack()
        c.pack()
        b.pack()
    return t


# Check and delete item
def exec_del_item(iid):
    if iid.isnumeric():
        remove_item(int(iid))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Delete item
def delete_item(tab_main, username):
    t = Frame(tab_main, background="white")
    l1 = Label(t, text="Enter item id: ", fg="black", bg="white")
    e1 = Entry(t)
    b = Button(t, text="REMOVE", command=lambda: exec_del_item(
        e1.get()), fg="black", bg="white")
    l1.grid(row=0, column=0,padx=200,pady=(300,0))
    e1.grid(row=0, column=1,pady=(300,0))
    b.grid(row=2, column=1,pady=50)
    return t


# Check and delete user
def exec_del_user(uid):
    if uid.isnumeric():
        remove_user(int(uid))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Delete user
def delete_user(tab_main, username):
    t = Frame(tab_main, background="white")
    l1 = Label(t, text="Enter user id: ", fg="black", bg="white")
    e1 = Entry(t)
    b = Button(t, text="REMOVE", command=lambda: exec_del_user(
        e1.get()), fg="black", bg="white")
    l1.grid(row=0, column=0,padx=200,pady=(300,0))
    e1.grid(row=0, column=1,pady=(300,0))
    b.grid(row=2, column=1,pady=50)
    return t


# Validate and add item
def ck_and_add_item(itemid, name, cost):
    row = ck_item_exists(itemid)
    if name and itemid.isnumeric() and cost.isnumeric() and row == None:
        add_item_to_db_data(int(itemid), name, int(cost))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Add items to database
def add_item_to_db(tab_main, username):
    t = Frame(tab_main, background="white")
    l1 = Label(t, text="Enter item id: ", fg="black", bg="white")
    e1 = Entry(t)
    l2 = Label(t, text="Enter name: ", fg="black", bg="white")
    e2 = Entry(t)
    l3 = Label(t, text="Enter cost: ", fg="black", bg="white")
    e3 = Entry(t)
    b = Button(t, text="ADD", command=lambda: ck_and_add_item(e1.get(), e2.get(), e3.get()),
               fg="black", bg="white")
    l1.grid(row=0, column=0,padx=200,pady=(200,0))
    e1.grid(row=0, column=1,pady=(200,0))
    l2.grid(row=1, column=0,padx=200)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0,padx=200)
    e3.grid(row=2, column=1)
    b.grid(row=4, column=1,pady=50)
    return t


# Showing the list of items
def show_item_list(tree):
    tree.delete(*tree.get_children())
    rows = get_items()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2]))


# List items
def list_items(tab_main, username):
    t = Frame(tab_main, background="white")
    tree = ttk.Treeview(t)
    b = Button(t, text="SHOW", command=lambda: show_item_list(
        tree), fg="black", bg="white")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="ID")
    tree.heading("one", text="NAME")
    tree.heading("two", text="COST")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    b.pack()
    tree.pack()
    return t


# Validate and add user
def ck_and_add(username, name, password, phno):
    row = get_user_details(username)
    if name and password and username.isnumeric() and phno.isnumeric() and row == None:
        add_user_to_db(int(username), name, password, int(phno))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Add user
def add_user(tab_main, username):
    t = Frame(tab_main, background="white")
    l1 = Label(t, text="Enter user id: ", fg="black", bg="white")
    e1 = Entry(t)
    l2 = Label(t, text="Enter name: ", fg="black", bg="white")
    e2 = Entry(t)
    l3 = Label(t, text="Enter user password: ", fg="black", bg="white")
    e3 = Entry(t)
    l4 = Label(t, text="Enter PHNO: ", fg="black", bg="white")
    e4 = Entry(t)
    b = Button(t, text="ADD", command=lambda: ck_and_add(e1.get(), e2.get(), e3.get(), e4.get()),
               fg="black", bg="white")
    l1.grid(row=0, column=0,padx=200,pady=(200,0))
    e1.grid(row=0, column=1,pady=(200,0))
    l2.grid(row=1, column=0,padx=200)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0,padx=200)
    e3.grid(row=2, column=1)
    l4.grid(row=3, column=0,padx=200)
    e4.grid(row=3, column=1)
    b.grid(row=4, column=1,pady=50)
    return t


# Showing the list of sales
def sal(tree):
    tree.delete(*tree.get_children())
    rows = get_all_sales()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))


# List sales
def sales(tab_main, username):
    t = Frame(tab_main, background="white")
    tree = ttk.Treeview(t)
    b = Button(t, text="SHOW", command=lambda: sal(
        tree), fg="black", bg="white")
    tree["columns"] = ("one", "two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("one", text="EMPLOYEE ID")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b.pack()
    tree.pack()
    return t


# Showing the list of employees
def s(tree):
    tree.delete(*tree.get_children())
    rows = get_all_employees()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[3]))


# List employees
def list_emp(tab_main, username):
    t = Frame(tab_main, background="white")
    tree = ttk.Treeview(t)
    b = Button(t, text="SHOW", command=lambda: s(
        tree), fg="black", bg="white")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="ID")
    tree.heading("one", text="NAME")
    tree.heading("two", text="PHNO")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    b.pack()
    tree.pack()
    return t


# Function for resetting the bill
def resetf():
    global selected_items
    global r
    selected_items.clear()
    r = random.randint(10000, 999999)


# Print/Show the bill
def get_bill(username):
    cost = 0
    items = []
    for i in selected_items:
        cost = cost + int(i[3])
        items.append(i[0])
    tax = round(cost * 0.2, 2)
    service = round(cost/99, 2)
    total_cost = round(cost+tax+service)
    t = Toplevel()
    t.geometry("350x700")
    t.title("BILL")
    t.configure(bg="white")
    date = Label(t, text="DATE: " +
                 datetime.now().strftime("%d-%m-%Y"), fg="black", bg="white")
    time = Label(t, text="TIME: "+datetime.now().strftime("%H:%M"),
                 fg="black", bg="white")
    ref = Label(t, text="REF NO: "+str(r), fg="black", bg="white")
    emp = Label(t, text="EMPLOYEE ID: "+str(username),
                fg="black", bg="white")
    costl = Label(t, text="COST: "+str(cost), fg="black", bg="white")
    taxl = Label(t, text="TAX: "+str(tax), fg="black", bg="white")
    servicel = Label(t, text="SERVICE CHARGES: " +
                     str(service), fg="black", bg="white")
    total_costl = Label(t, text="TOTAL COST: " +
                        str(total_cost), fg="black", bg="white")
    date.pack()
    time.pack()
    ref.pack()
    emp.pack()
    costl.pack()
    taxl.pack()
    servicel.pack()
    total_costl.pack()
    Label(t, text="ITEMS:", fg="black", bg="white").pack()
    for it in range(len(selected_items)):
        Label(t, text=selected_items[it][0] + "( X "+str(
            selected_items[it][1])+" )", fg="black", bg="white").pack()
    if total_cost:
        store(datetime.now(), username, total_cost, r)
    return t


# Add items to the bill
def add_item(item, itemno):
    cost = get_cost(item)
    total=int(itemno)*int(cost)
    selected_items.append((item, itemno, cost, total))
    return


# Show the various items added to the bill when refresh is clicked
def two(tree):
    tree.delete(*tree.get_children())
    for row in selected_items:
        tree.insert("", 0, text=row[0], values=(row[1], row[2],row[3]))


# Show the various items added to the bill
def show_items(tab_main, username):
    t = Frame(tab_main, background="white")
    tree = ttk.Treeview(t)
    b = Button(t, text="REFRESH", command=lambda: two(
        tree), fg="black", bg="white")
    b2 = Button(t, text="SUBMIT", command=lambda: get_bill(
        username), fg="black", bg="white")
    reset = Button(t, text="RESET", command=lambda: resetf(),
                   fg="black", bg="white")
    tree["columns"] = ("one", "two","three")
    tree.heading("#0", text="NAME")
    tree.heading("one", text="QUANTITY")
    tree.heading("two", text="COST")
    tree.heading("three", text="TOTAL")
    tree.column("#0", anchor=CENTER)
    tree.column("one", anchor=CENTER)
    tree.column("two", anchor=CENTER)
    tree.column("three", anchor=CENTER)
    b.pack()
    b2.pack()
    reset.pack()
    tree.pack()
    return t


# Billing section
def bill(tab_main, username):
    t = Frame(tab_main, background="white")
    rows = get_items()
    options = []
    for i in rows:
        options.append(i[1])
    clicked = StringVar()
    if(len(options)):
        clicked.set(options[0])
        cl = IntVar()
        cl.set(1)
        drop = OptionMenu(t, clicked, *options)
        l = Label(t, text="SELECT QUANTITY:", fg="black", bg="white")
        q = OptionMenu(t, cl, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        b = Button(t, text="ADD", command=lambda: add_item(
            clicked.get(), cl.get()), fg="black", bg="white")
        reset = Button(t, text="RESET", command=lambda: resetf(),
                       fg="black", bg="white")
        drop.pack()
        l.pack()
        q.pack()
        b.pack()
        reset.pack()
    return t


# Employee details
def user_details(tab_main, username):
    t = Frame(tab_main, background="white")
    data = get_user_details(int(username))
    lname = Label(t, text="NAME: "+data[1], fg="black", bg="white")
    lid = Label(t, text="ID: "+str(data[0]), fg="black", bg="white")
    lphno = Label(t, text="PHNO: "+str(data[2]), fg="black", bg="white")
    lname.config(font=("Courier", 34))
    lid.config(font=("Courier", 34))
    lphno.config(font=("Courier", 34))
    lname.pack()
    lid.pack()
    lphno.pack()
    img = ImageTk.PhotoImage(Image.open(r"img\bill.png"))
    panel = Label(t, image=img,bg="white")
    panel.photo = img
    panel.pack()
    return t


# Admin details
def admin_details(tab_main, username):
    t = Frame(tab_main, background="white")
    data = get_admin_details(int(username))
    lname = Label(t, text="NAME: "+data[1], fg="black", bg="white")
    lid = Label(t, text="ID: "+str(data[0]), fg="black", bg="white")
    lphno = Label(t, text="PHNO: "+str(data[2]), fg="black", bg="white")
    lname.config(font=("Courier", 44))
    lid.config(font=("Courier", 44))
    lphno.config(font=("Courier", 44))
    lname.pack()
    lid.pack()
    lphno.pack()
    img = ImageTk.PhotoImage(Image.open(r"img\admin.png"))
    panel = Label(t, image=img,bg="white")
    panel.photo = img
    panel.pack()
    return t


# POPUP for displaying errors
def popup(msg):
    pop = Toplevel()
    pop.geometry("200x60")
    pop.title("MESSAGE")
    pop.configure(bg="white")
    l = Label(pop, text=msg, fg="black", bg="white")
    exitb = Button(pop, text="OK", fg="black", bg="white",
                   command=lambda: pop.destroy())
    l.pack()
    exitb.pack()


# Employee dashboard
def ud(username):
    ud = Toplevel()
    ud.geometry("900x800")
    ud.title("USER DASH")
    ud.configure(bg="white")
    tab_main = ttk.Notebook(ud)
    t1 = user_details(tab_main, username)
    t2 = bill(tab_main, username)
    t3 = show_items(tab_main, username)
    t4 = remove_bill(tab_main, username)
    tab_main.add(t1, text="USER DETAILS")
    tab_main.add(t2, text="BILLING")
    tab_main.add(t3, text="VIEW BILL")
    tab_main.add(t4, text="REMOVE BILL")
    tab_main.pack(expand=1, fill='both')


# Admin dashboard
def ad(username):
    ad = Toplevel()
    ad.geometry("900x800")
    ad.title("ADMIN DASH")
    ad.configure(bg="white")
    tab_main = ttk.Notebook(ad)
    t1 = admin_details(tab_main, username)
    t2 = list_emp(tab_main, username)
    t3 = sales(tab_main, username)
    t4 = add_user(tab_main, username)
    t5 = list_items(tab_main, username)
    t6 = add_item_to_db(tab_main, username)
    t7 = delete_user(tab_main, username)
    t8 = delete_item(tab_main, username)
    t9 = change_price_of_item(tab_main, username)
    t10 = deleted_bills(tab_main, username)
    tab_main.add(t1, text="ADMIN DETAILS")
    tab_main.add(t2, text="ALL USER DETAILS")
    tab_main.add(t3, text="TOTAL SALES")
    tab_main.add(t4, text="CREATE NEW USER")
    tab_main.add(t5, text="SHOW ALL ITEMS")
    tab_main.add(t6, text="ADD NEW ITEM")
    tab_main.add(t7, text="DELETE USER")
    tab_main.add(t8, text="DELETE ITEM")
    tab_main.add(t9, text="UPDATE PRICE")
    tab_main.add(t10, text="DELETED BILLS")
    tab_main.pack(expand=1, fill='both')


# Employee authentication
def user_auth(username, password):
    if username and password and username.isnumeric():
        if ck_details_emp(int(username), password):
            ud(username)
        else:
            popup("ERROR WRONG DETAILS")
    else:
        popup("ERROR WRONG DETAILS")


# Admin authentication
def admin_auth(username, password):
    if username and password and username.isnumeric():
        if ck_details_admin(int(username), password):
            ad(username)
        else:
            popup("ERROR WRONG DETAILS")
    else:
        popup("ERROR WRONG DETAILS")


# Employee login
def user_login():
    ul = Toplevel()
    ul.geometry("300x130")
    ul.title("USER LOGIN")
    ul.configure(bg="white")
    l1 = Label(ul, text="EID: ", fg="black", bg="white")
    e1 = Entry(ul)
    l2 = Label(ul, text="PASSWORD: ", fg="black", bg="white")
    e2 = Entry(ul, show="*")
    sb = Button(ul, text="LOGIN", fg="black", bg="white",
                command=lambda: user_auth(e1.get(), e2.get()))
    ul.bind('<Return>', lambda event: user_auth(e1.get(), e2.get()))
    l1.grid(row=0, column=0,pady=10)
    e1.grid(row=0, column=1,pady=10)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    sb.grid(row=2, column=1,pady=10)


# Admin login
def admin_login():
    al = Toplevel()
    al.geometry("300x130")
    al.title("ADMIN LOGIN")
    al.configure(bg="white")
    l1 = Label(al, text="AID: ", fg="black", bg="white")
    e1 = Entry(al)
    l2 = Label(al, text="PASSWORD: ", fg="black", bg="white")
    e2 = Entry(al, show="*")
    sb = Button(al, text="LOGIN", fg="black", bg="white",
                command=lambda: admin_auth(e1.get(), e2.get()))
    al.bind('<Return>', lambda event: admin_auth(e1.get(), e2.get()))
    l1.grid(row=1, column=0,pady=10)
    e1.grid(row=1, column=1, pady=10)
    l2.grid(row=2, column=0)
    e2.grid(row=2, column=1)
    sb.grid(row=3, column=1, pady=10)
    # al.mainloop()


# Initial setup
root = Tk()
root.geometry("1000x1000")
root.title("Medical Shop Billing System")
root.configure(bg="white")
myFont = font.Font(size=30)
admin_img=PhotoImage(file='img\d_login.png')
adminB = Button(root, fg="black", bg="white", padx=16,
                pady=8, bd=5, anchor="center", command=admin_login, image=admin_img, borderwidth = 5)
user_img=PhotoImage(file='img\login.png')
userB = Button(root, fg="black", bg="white", padx=16,
               pady=8, bd=5, anchor="center", command=user_login, image=user_img, borderwidth = 5)
close_img = PhotoImage(file='img\close.png')

close_button = Button(root,  fg="black", bg="white", padx=16,
               pady=8, bd=5,  anchor="center", command=root.quit, image=close_img,borderwidth = 0)
# close_button['font'] = myFont
adminB.grid(row=2, column=0, pady=0)
userB.grid(row=3, column=0,pady=20)
close_button.grid(row=4, column=0)


img = ImageTk.PhotoImage(Image.open(r"img\pharmacy.png"))
panel = Label(root, image=img, width=1000, height=750,bg="white")
panel.photo = img
panel.grid(row=1, column=0)

# close button
root.overrideredirect(True)


# close_button.pack(pady=100)


root.mainloop()




