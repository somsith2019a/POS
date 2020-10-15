#GUIcalculator.py
from tkinter import *
from tkinter import ttk #theme for lable and entry
import csv
from datetime import datetime
font_title = ("arial", 22)
font_result= ("arial", 14)
GUI = Tk()
GUI.geometry('650x750+450+25') 

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
L0.pack(pady=10) # for c center aglin
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
    with open('EP3\data.csv', 'a', newline='', encoding='UTF-8') as file:
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
def ReadData():
    with open('EP3\data.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file)
        alldata = list(fr)
    return alldata

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
alldata = ReadData()
for dt in alldata:
    apB1.insert('', 'end', value=dt)
    
GUI.mainloop()