tkinter

GUI = Tk()
GUI.mainloop()

GUI.title(text="xxx")
GUI.geometry("[wide]x[height]+[positionX]+[positionY]")
x = Label(text="xxx", font=font)
x.pack()


v_p = StringVar() # ເກັບຄ່າ entry

b = Entry(GUI, textvariable=v_p)

pg = p.get() # get value from textbox

value.set("xxxxx") # set value for variable of StringVar()

