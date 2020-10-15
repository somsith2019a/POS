from tkinter import *
from tkinter.ttk import Notebook
from tkinter import ttk
import csv

GUI = Tk()
GUI.title("POS practice3")
GUI.geometry("500x500+500+150")

#FONTS
FONT1= ("arial", 22)

####### TAB ########

TAB = Notebook()
F1 = Frame(TAB)
F2 = Frame(TAB)
F3 = Frame(TAB)
F4 = Frame(TAB)

TAB.add(F1, text="Sales")
TAB.add(F2, text="Add Product")
TAB.add(F3, text="All Products")
TAB.add(F4, text="History")
TAB.pack(expand=1, fill=BOTH)

####### TAB Add Product ########

#function to add products
def Addpd(): #Function to add products 
    bc = boxProduct_bc.get()
    pd = boxProduct_pd.get()
    pc = boxProduct_pc.get()
    qn = boxProduct_qn.get()
    total = int(pc) * int(qn)
    data = [bc,pd,pc,qn,total]
    rs = f'''
Done !!!
Barcode : {bc}, Product : {pd}, Price : {pc}, Quantity: {qn}
Total : {total}
    '''
    v_result.set(rs)
    SaveData(data)

#function to save product -->  xxx.csv file
def SaveData(listdata):
    with open('EP3\data.csv', 'a', newline='', encoding="utf-8") as file:
        fw = csv.writer(file)
        fw.writerow(listdata)
    print(f"Product : {boxProduct_pd.get()} has been saved!")


#Barcode row1
L1 = ttk.Label(F2, text="Barcode", font=FONT1)
L1.pack()
v_barcode = StringVar()
boxProduct_bc = ttk.Entry(F2, textvariable=v_barcode)
boxProduct_bc.pack(pady=10)
#Produt row2
L2 = ttk.Label(F2, text="Product", font=FONT1)
L2.pack()
v_product = StringVar()
boxProduct_pd = ttk.Entry(F2, textvariable=v_product)
boxProduct_pd.pack(pady=10)
#Price row3
L3 = ttk.Label(F2, text="Price", font=FONT1)
L3.pack()
v_price = StringVar()
boxProduct_pc = ttk.Entry(F2, textvariable=v_price)
boxProduct_pc.pack(pady=10)
#Quantity row4
L4 = ttk.Label(F2, text="Quantity", font=FONT1)
L4.pack()
v_quantity = StringVar()
boxProduct_qn = ttk.Entry(F2, textvariable=v_quantity)
boxProduct_qn.pack(pady=10)
##button
but1 = ttk.Button(F2, text="Add Product", command=Addpd)
but1.pack(ipadx=10,ipady=5, pady=10)
##result
v_result = StringVar()
v_result.set('-- status --')
result = Label(F2, textvariable=v_result,font=(FONT1[0],10))
result.pack()







GUI.mainloop()