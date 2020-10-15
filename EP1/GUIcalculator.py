#GUIcalculator.py
from tkinter import *
from tkinter import ttk #theme for lable and entry

font_title = ("arial", 22)
font_result= ("arial", 14)
GUI = Tk()
GUI.title('Program calculator')
GUI.geometry('300x380+500+200') 

## Row1
L1 = ttk.Label(GUI, text='Product', font=font_title)
L1.pack(pady=10) # for c center aglin

v_product = StringVar() #String var คือกล่อง ใส่ตัวแปรที่เปี่ยนแปลงได้

B1 = ttk.Entry(GUI, textvariable=v_product) 
B1.pack()

## Row2
L2 = ttk.Label(GUI, text='Price', font=font_title)
L2.pack(pady=10) # for c center aglin

v_price = StringVar() #box2 

B2 = ttk.Entry(GUI, textvariable=v_price) 
B2.pack()

## Row3
L3 = ttk.Label(GUI, text='Amount', font=font_title)
L3.pack(pady=10) # for c center aglin

v_amount = StringVar() #box3

B3 = ttk.Entry(GUI, textvariable=v_amount) 
B3.pack()

#button

def Calc():
    pd = v_product.get() # .get() พนักงานเปีดกล่องดุว่ามีอะไรบ้างในนั้น
    pc = v_price.get()
    am = v_amount.get()
    cal = int(pc) * int(am)
    text_result = f'สินค้า : {pd}, ลาคา : {pc}, จำนวน : {am}'
    text_result = text_result + f'\nรวมคา {cal} '
    v_result.set(text_result)

But_1 = ttk.Button(GUI, text='calculate',command=Calc)
But_1.pack(ipadx=10, ipady=5, pady = 20)

#result
v_result = StringVar()
v_result.set("----------RESULT----------")

R1 = ttk.Label(GUI, textvariable=v_result,font=font_result) 
R1.pack()

GUI.mainloop()