#GUIcalculator.py
from tkinter import *
from tkinter import ttk #theme for lable and entry
from CRUD import *
import csv


from datetime import datetime
font_title = ("arial", 22)
font_result= ("arial", 14)
GUI = Tk()
GUI.title("pricetice4")
GUI.geometry('1050x750+450+25') 

## TAB 
from tkinter.ttk import Notebook

Tab = Notebook(GUI)
F1 = Frame(Tab)
F2 = Frame(Tab)
F4 = Frame(Tab)
F3 = Frame(Tab)

Tab.add(F1, text="Sales")
Tab.add(F2, text="Add Products")
Tab.add(F3, text="All Products")
Tab.add(F4, text="History")
Tab.pack(fill=BOTH, expand=1)


############## Add Product (Tab) ###################

## Row0
L0 = ttk.Label(F2, text='Barcode', font=font_title)
L0.pack(pady=10) # for c cen ter aglin
v_barcode = StringVar() 
B0 = ttk.Entry(F2, textvariable=v_barcode) 
B0.pack()

## Row1
L1 = ttk.Label(F2, text='Product', font=font_title)
L1.pack(pady=10) # for c center aglin
v_product = StringVar() #String var คือกล่อง ใส่ตัวแปรที่เปี่ยนแปลงได้
B1 = ttk.Entry(F2, textvariable=v_product) 
B1.pack()

## Row2
L2 = ttk.Label(F2, text='Price', font=font_title)
L2.pack(pady=10) # for c center aglin
v_price = StringVar() #box2 
B2 = ttk.Entry(F2, textvariable=v_price) 
B2.pack()

## Row3
L3 = ttk.Label(F2, text='Amount', font=font_title)
L3.pack(pady=10) # for c center aglin
v_amount = StringVar() #box3
B3 = ttk.Entry(F2, textvariable=v_amount) 
B3.pack()
#button

def Write(listdata): 
    print("Writing...")
    with open('EP6\data.csv', 'a', newline='', encoding='UTF-8') as file:
	    f = csv.writer(file)
	    f.writerow(listdata)
    print("Finished")

def Calc():
    bc = v_barcode.get()
    pd = v_product.get() # .get() พนักงานเปีดกล่องดุว่ามีอะไรบ้างในนั้น
    pc = v_price.get()
    am = v_amount.get()
    date = datetime.now().strftime("%a %d/%m/%y %I:%H:%M %p ")
    cal = int(pc) * int(am)
    Write([bc,pd,pc,am,cal,date])
    text_result = f'สินค้า : {pd}, ลาคา : {pc}, จำนวน : {am}'
    text_result = text_result + f'\nรวมคา {cal}\n{date} '
    v_result.set(text_result)
    apB1.insert('', 'end', value=[bc,pd,pc,am,cal,date])



But_1 = ttk.Button(F2, text='Add Product',command=Calc)
But_1.pack(ipadx=10, ipady=5, pady = 20)
#result
v_result = StringVar()
v_result.set("---- Status ----")
R1 = ttk.Label(F2, textvariable=v_result,font=font_result) 
R1.pack()



############### All Product (Tab) ###############

#function

apL1 = Label(F3, text="All Products", font=font_title)
apL1.pack()

## Treeview()##

header = ['Barcode','Products','Price','Amount','Total','Last Update']
w = [70,150,70,70,70,160]

apB1 = ttk.Treeview(F3, height=10, column=header, show="headings")
apB1.pack()
for hd in header:
    apB1.heading(hd, text=hd)
for hd,w in zip(header,w):
    apB1.column(hd, width=w)

## insert data ##
alldata = ReadData('EP6/data.csv')
for dt in alldata:
    apB1.insert('', 'end', value=dt)

############## Sales (Tab) ###################


BF1 = Frame(F1)
BF1.place(x=30, y=30)
current_product = {} 
total = 0
check_ref = False
    ##function
def Insert_Sales(i):
    global total
    if i not in current_product:
        dt = current_stock[i] 
        dt[3] = 1 
        dt[4] = dt[3] * int(dt[2])
        dt[4] = f'{dt[4]:,.2f}'
        table_sales.insert('', 'end', value=dt)
        current_product[i] = dt
        total += int(dt[2]) 
    else : 
        current_product[i][3] = current_product[i][3] + 1
        current_product[i][4] = current_product[i][3] * int(current_product[i][2])
        current_product[i][4] = f'{current_product[i][4]:,.2f}'

        table_sales.delete(*table_sales.get_children())
        for ct in current_product.values():
            table_sales.insert('','end', value=ct)
        total += int(current_product[i][2])
    global check_ref
    if check_ref == False:
        ref_id = datetime.now().strftime('%d%m%y%I%H%M%S')
        v_REF.set(ref_id)
        check_ref = True
    v_total.set(f'{total:,.2f}')

def cash_but():
    global total
    total = 0

################
    ###read data
current_stock = ReadData('EP6/data.csv')
row_count = 0

    #### Button
for bt_product in range(len(current_stock)): #product's button
    B1 = ttk.Button(BF1,text=current_stock[bt_product][1],command=lambda x=bt_product : Insert_Sales(x))
    if bt_product % 3 == 0:        
        B1.grid(row=row_count, column=0,ipady=10,padx=20,pady=5)
    elif bt_product % 3 == 1:        
        B1.grid(row=row_count, column=1, ipady=10, padx=5, pady=5)
    elif bt_product % 3 == 2:
        B1.grid(row=row_count, column=2, ipady=10, padx=20, pady=5)   
        row_count += 1 
BSF = Frame(F1)
BSF.place(x=764, y=270)


    ## reference
ref = Label(F1, text="Ref :")
ref.place(x=430, y=5)

v_REF = StringVar()
v_REF.set("______ Reference ______")
REF = Label(F1, textvariable=v_REF, foreground='gray')
REF.place(x=455, y=5)
    
    ## Treeview()##
header = ['Barcode','Products','Price','Amount','Total']
w = [70,150,70,70,70]

table_sales = ttk.Treeview(F1, height=10, column=header, show="headings")
table_sales.place(x=430, y=30)

for hd in header:
    table_sales.heading(hd, text=hd)
for hd,w in zip(header,w):
    table_sales.column(hd, width=w)

table_sales.column('Barcode', anchor=CENTER)
table_sales.column('Products', anchor=CENTER)
table_sales.column('Price', anchor=E)
table_sales.column('Amount', anchor=E)
table_sales.column('Total', anchor=E)


    ## Total
L_total1 = ttk.Label(F1, text="Total : ",font=font_title)
L_total1.place(x=430, y=268)
v_total = StringVar()
v_total.set('---')
L_total2 = ttk.Label(F1, textvariable=v_total,font=(font_title[0],19), foreground="green")
L_total2.place(x=525, y=272.5)
    
    ## cash
bt_cash = ttk.Button(BSF, text="Cash") #cash's button
bt_cash.pack(ipadx=12, ipady=5)

def ChangeQuantity(event=None): 
    select = table_sales.selection() #return I001
    data = table_sales.item(select)  #return {'text': '', 'image': '', 'values': [11103, 'toy', 150, 1, '150.00', 'Mon 28/09/20 02:02:04 AM '], 'open': 0, 'tags': ''}
    editdata = data['values'][0:-2]  #return [11103, 'toy', 150, 1]
    # editdata[3] = 10
    print(editdata)

    #New Winndow for edit quantity
    GUI2 = Toplevel()
    GUI2.geometry('300x200+800+160')
    GUI2.title('Edit quantity of product')
    
    def Change(event=None):
        editdata[3] = int(v_newquantity.get())
        print(editdata)

    v_newquantity = StringVar()
    EA1 = ttk.Entry(GUI2, textvariable=v_newquantity)
    EA1.pack(pady=20,ipady=5)

    EA1.focus()
    EA1.bind('<Return>', Change)

    bt_change = ttk.Button(GUI2, text="Change", command=Change) #Change's button
    bt_change.pack(ipadx=12, ipady=5)
    

    GUI2.mainloop()

table_sales.bind('e',ChangeQuantity)



GUI.mainloop()