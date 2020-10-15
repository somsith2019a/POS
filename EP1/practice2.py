from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title("GUI Calculator Practice2")
GUI.geometry("400x500")

font1 = ("Arial", 22)

########## ROW1 ##########
v_product = StringVar()
L1 = Label(text="Product", font=font1)
B1 = ttk.Entry(GUI, textvariable=v_product)
L1.pack()
B1.pack()
########## ROW2 ##########
v_price = StringVar()
L2 = Label(text="Price", font=font1)
B2 = ttk.Entry(GUI, textvariable=v_price)
L2.pack()
B2.pack()
########## ROW3 ##########
v_amount = StringVar()
L3 = Label(text="Amount", font=font1)
B3 = ttk.Entry(GUI, textvariable=v_amount)
L3.pack()
B3.pack()
######### Button #########
def Calc():
    pd = v_product.get()
    pc = v_price.get()
    am = v_amount.get()
    cal = int(pc) * int(am)
    rs = f"Product : {pd}\nPrice : {pc}\namount : {am}\nTotal : {cal}" 
    v_result.set(rs)
    print(rs)

    
button1 = Button(text="Calculator", font=(font1[0], 14), command=Calc)
button1.pack(pady=10)
######### Result #########
v_result = StringVar()
v_result.set("######### Result #########")
result = Label(GUI, textvariable=v_result)
result.pack()



GUI.mainloop()