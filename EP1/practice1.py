from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title("Practice Calculator EP1")
GUI.geometry("200x400+600+200")
Font1 = ("arial", 22)

####### Row 1 #######
L1 = ttk.Label(text="Product", font = Font1)
L1.pack()

v_product = StringVar() 

B1 = ttk.Entry(GUI, textvariable=v_product)
B1.pack(pady= 10)

####### Row 2 #######
L2 = ttk.Label(text="Price", font = Font1)
L2.pack()

v_price = StringVar()
v_price.set(0)
B2 = ttk.Entry(GUI, textvariable=v_price)
B2.pack(pady= 10)

####### Row 3 #######
L3 = ttk.Label(text="Amount", font = Font1)
L3.pack()

v_amount = StringVar()
v_amount.set("0")
B3 = ttk.Entry(GUI, textvariable=v_amount)
B3.pack(pady= 10)

####### Button ######

def Calc():
    pd = v_product.get()
    pc = v_price.get()
    am = v_amount.get()
    total = int(pc) * int(am)
    v_result.set(f"Product : {pd}\nPrice : {pc}\nAmount : {am}\nTotal : {total}")

but1 = ttk.Button(text="Calculate",command=Calc)
but1.pack(pady=10)


####### RESULT #######
v_result = StringVar()
v_result.set("----- Result -----")
R1 = ttk.Label(GUI, textvariable=v_result)
R1.pack(pady= 10)




GUI.mainloop()