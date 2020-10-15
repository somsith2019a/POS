#GUIproduct.py

from tkinter import * # * is all
from tkinter import ttk # ttk is theme of Tk
import csv
from tkinter import messagebox
from datetime import datetime

def Write(listdata):
	# listdata = 1 row .Ex. ['Apple',10]
	print('Writing...')
	with open('ELdata.csv','a',newline='',encoding='utf-8') as file:
		#fw = file writer
		# 'a' = append
		# 'w' = write (replace)
		fw = csv.writer(file)
		fw.writerow(listdata)


def ReadData():
	with open('EP6\data.csv',newline='',encoding='utf-8') as file:
		#fr = file reader
		fr = csv.reader(file)
		alldata = list(fr)
		#print(alldata)
	return alldata


def UpdateData(row,quantity):
	print('----before----')
	allstock = ReadData()
	print(allstock[row])

	#print('----after----')
	#print('----quan-----')
	allstock[row][4] = int(allstock[row][4]) - quantity
	#print(allstock[row])
	#print('----total-----')
	total = allstock[row][4] * int(allstock[row][3])
	allstock[row][5] = total
	#print('----after total----')
	#print(allstock[row])

	with open('data.csv','w',newline='',encoding='utf-8') as file:
		#fw = file writer
		fw = csv.writer(file)
		fw.writerows(allstock)

	print('-----data after change------')
	allstock = ReadData()
	print(allstock[row])



GUI = Tk() #ทีตัวใหญ่เคตัวเล็ก
GUI.title('โปรแกรมคำนวณ by Uncle Engineer')
GUI.geometry('900x600+0+0')

FONT1 = ('Angsana New',20)

########TAB#########
from tkinter.ttk import Notebook

Tab = Notebook(GUI)

F1 = Frame(Tab)
F2 = Frame(Tab)
F3 = Frame(Tab)
F4 = Frame(Tab)

Tab.add(F1,text='Sales')
Tab.add(F2,text='Add Product')
Tab.add(F4,text='All Product')
Tab.add(F3,text='History')

Tab.pack(fill=BOTH, expand=1)



######ROW1######


LB1 = ttk.Label(F2,text='Barcode',font=FONT1)
LB1.pack() 

v_barcode = StringVar() #BOX0


EB1 = ttk.Entry(F2,textvariable=v_barcode,font=FONT1)
EB1.pack()


L1 = ttk.Label(F2,text='สินค้า',font=FONT1)
L1.pack()

v_product = StringVar() #BOX1

E1 = ttk.Entry(F2,textvariable=v_product,font=FONT1)
E1.pack() # Textbox

######ROW2######
L2 = ttk.Label(F2,text='ราคา',font=FONT1)
L2.pack()

v_price = StringVar() #BOX2

E2 = ttk.Entry(F2,textvariable=v_price,font=FONT1)
E2.pack()
		   
######ROW3######
L3 = ttk.Label(F2,text='จำนวน',font=FONT1)
L3.pack()

v_quan = StringVar() #BOX3

E3 = ttk.Entry(F2,textvariable=v_quan,font=FONT1)
E3.pack()
#########BUTTON#########

def Calc():
	bc = v_barcode.get() # ดึงรหัสบาร์โค้ดลงมา
	pd = v_product.get() # .get() พนักงานเปิดกล่องดูว่ามีอะไรบ้างในนั้น
	pc = v_price.get()
	qn = v_quan.get()
	cal = int(pc) * int(qn) #total

	date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	data = [date,bc,pd,pc,qn,cal]
	Write(data)

	text_result = f'Barcode: {bc} สินค้า: {pd} ราคา: {pc} บาท มีทั้งหมด {qn} ชิ้น\n'
	# \n is newline
	text_result = text_result + f'รวมราคา {cal:,d} บาท'
	v_result.set(text_result) #พนักงานสรุปเขียนผลลัพท์ใหม่
	print(text_result)
	update_table()


B1 = ttk.Button(F2,text='Add Product',command=Calc)
B1.pack(ipadx=20,ipady=10, pady=20)
#ipadx is internal padding x-axis for resize button

#########RESULT#########
v_result = StringVar() #BOX4
v_result.set('----------Result----------')

R1 = ttk.Label(F2,textvariable=v_result,font=FONT1,foreground='green')
R1.pack()

#StringVar คือ กล่องใส่ตัวแปรที่เปลี่ยนแปลงได้
#.pack() กลางบนลงมาด้านล่าง
#L1.place(x=300,y=100)


#################All Product################
header = ['Datetime','Barcode','Product','Price','Quantity','Total']
hw = [120,70,150,70,70,70]

table_product = ttk.Treeview(F4,height=20, column=header, show='headings')
table_product.pack()

for hd in header:
	table_product.heading(hd,text=hd)

for hd,w in zip(header,hw):
	table_product.column(hd,width=w)


##### การนำค่าลงตาราง treeview #####
def update_table():
	#สั่งเคลียร์ข้อมูลชุดเก่าออกไปก่อน
	table_product.delete(*table_product.get_children()) #clear all in table
	alldata = ReadData()
	for dt in alldata:
		table_product.insert('','end',value=dt) #ใส่ค่าเข้าไปทีละแถว

#First time run

##############SALES TAB#################

v_ref = StringVar()
v_ref.set('------Ref------')
lref = ttk.Label(F1,text='Ref: ').place(x=400,y=5)
LREF = ttk.Label(F1,textvariable=v_ref,foreground='green')
LREF.place(x=430,y=5)


current_stock = ReadData()
count = len(current_stock) #นับค่าแถวที่มีใน csv

header = ['Barcode','Product','Price','Quantity','Total']
hw = [70,150,70,70,70]

table_sales = ttk.Treeview(F1,height=20, column=header, show='headings')
table_sales.place(x=400,y=30)

for hd in header:
	table_sales.heading(hd,text=hd)

for hd,w in zip(header,hw):
	table_sales.column(hd,width=w)

#########ADJUST NUMBER RIGHT ALIGNMENT#########
table_sales.column('Product',anchor=CENTER)
table_sales.column('Price',anchor=E)
table_sales.column('Quantity',anchor=E)
table_sales.column('Total',anchor=E)


BF1 = Frame(F1)
BF1.place(x=20,y=20)

current_table = {} #เก็บค่าล่าสุดที่มีอยู่ในตารางขายสินค้า
index_table = {}
check_ref = False #สำหรับเช็คว่าตอนนี้สร้าง ref ไปแล้วยัง

def update_sales_table():
	table_sales.delete(*table_sales.get_children())
	for ct in current_table.values():
		table_sales.insert('','end',value=ct)

def update_total():
	total = sum([ int(ctp[-1]) for ctp in current_table.values()]) # -1 ดึงตัวสุดท้ายมา
	v_total.set(f'{total:,.2f}')

def Insert_Sales(pid):
	global check_ref #ทำให้สามารถแก้ไขตัวแปรภายนอกได้

	if check_ref == False:
		stamp = datetime.now().strftime('%Y%m%d%H%M%S')
		print('REF: ',stamp)
		v_ref.set(stamp)
		check_ref = True

	print(pid)
	dt = current_stock[pid][1:]
	dt[3] = 1
	dt[4] = dt[3] * int(dt[2])

	if pid not in current_table:
		table_sales.insert('','end',value=dt)
		current_table[pid] = dt #dt = ['1001','Apple']
		index_table[dt[0]] = pid
	else:
		print(current_table[pid])
		selected = current_table[pid]
		selected[3] = selected[3] + 1 #quantity edited 
		selected[4] = int(selected[2]) * selected[3]

		
		#table_sales.insert('','end',value=selected)
		update_sales_table()
			#index_table[ct[0]] = pid # ct = ['1001','Apple']

	print('Current_table')
	print(current_table)
	print('Index_table', index_table)
	update_total()
	


row_count = 0
for i in range(count):
	# i = [0,1,2,3....ตามจำนวนของสินค้า]
	B1 = ttk.Button(BF1,text=current_stock[i][2],width=15)
	print('Button',i)
	if i % 3 == 0:
		B1.grid(row=row_count,column=0,ipady=10)
	elif i % 3 == 1:
		B1.grid(row=row_count,column=1,ipady=10)
	elif i % 3 == 2:
		B1.grid(row=row_count,column=2,ipady=10)
		row_count = row_count + 1
	else:
		pass
	B1.configure(command=lambda x=i: Insert_Sales(x))
	#B1.place(x=50,y=50 * (i+1))

FONT2 = (None,20,'bold')

v_total = StringVar()
v_total.set('------Total------')
ltotal = ttk.Label(F1,text='Total:',font=FONT2).place(x=400,y=480)

ftotal = Frame(F1)
ftotal.place(x=500,y=480)

LTOTAL = ttk.Label(ftotal,textvariable=v_total,foreground='red',font=FONT2,width=12,anchor=E)
LTOTAL.pack()


def WriteTransaction(listdata):
	# listdata = 1 row .Ex. ['Apple',10]
	print('Writing...')
	with open('transaction.csv','a',newline='',encoding='utf-8') as file:
		#fw = file writer
		# 'a' = append
		# 'w' = write (replace)
		fw = csv.writer(file)
		fw.writerow(listdata)

def Cash():
	global current_table
	allproduct = list(current_table.values())
	print(allproduct)
	stamp = datetime.now().strftime('%Y%m%d-%H:%M:%S')
	ref = v_ref.get()
	for apd in allproduct:
		record = [ref,stamp]
		record.extend(apd)
		WriteTransaction(record)
	
	current_table = {}
	index_table = {}
	update_sales_table()
	update_total()
	global check_ref
	check_ref = False
	v_ref.set('------Ref------')


BSF = Frame(F1)
BSF.place(x=700,y=480)
BS1 = ttk.Button(BSF,text='Cash',command=Cash)
BS1.pack(ipadx=20,ipady=10)



########Change Quantity##########

def ChangeQuantity(event=None):
	try:
		select = table_sales.selection()
		data = table_sales.item(select)
		editdata = data['values']
		editdata[3] = 10
		print(editdata)

		#New window for edit quantity
		def Change(event=None):
			editdata[3] = int(v_newquan.get())
			editdata[4] = editdata[3] * editdata[2]
			print(editdata)
			current_table[index_table[str(editdata[0])]] = editdata
			# index_table = ['1001':0,'1002':1]
			update_sales_table()
			update_total()
			GUI2.withdraw()


		GUI2 = Toplevel()
		GUI2.geometry('300x200')
		GUI2.title('แก้ไขจำนวนสินค้า')

		v_newquan = StringVar()
		E1 = ttk.Entry(GUI2,textvariable=v_newquan,font=FONT1)
		E1.pack(padx=20,pady=20)

		E1.focus()
		E1.bind('<Return>',Change)

		B1 = ttk.Button(GUI2,text='Change',command=Change)
		B1.pack()

		GUI2.mainloop()
	except:
		messagebox.showerror('Select Error','กรุณาเลือกสินค้าที่ต้องการแก้ไขจำนวน')


def DeleteSalesTable(event=None):
	try:
		select = table_sales.selection()
		data = table_sales.item(select)
		deleteid = str(data['values'][0])
		del current_table[index_table[deleteid]]
		del index_table[deleteid]
		update_sales_table()
		update_total()
	except Exception as e:
		print(e)
		messagebox.showerror('Select Error','กรุณาเลือกสินค้าที่ต้องการลบ')

table_sales.bind('<F12>',ChangeQuantity)
table_sales.bind('<Double-1>',ChangeQuantity)
table_sales.bind('<Delete>',DeleteSalesTable)

update_table()
GUI.mainloop()