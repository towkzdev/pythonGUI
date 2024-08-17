#1 บาทไทย = 0.026 EUR(ยูโร)
#1 บาทไทย = 3.486 JPY(เยล)
#1 บาทไทย = 0.031 USD(ดอลล่า)
#1 บาทไทย = 0.023 GBP(ปอนด์)

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")

#input
money = IntVar()
Label(text="จำนวนเงิน(THB)",padx=10,font=20).grid(row=0,sticky=W)
et1=Entry(font=30,width=30)
et1.grid(row=0,column=1)
#
choice = StringVar(value="โปรดเลือกสกุเงิน")
Label(text="เลือกสกุลเงิน",padx=10,font=20).grid(row=1,sticky=W)
combo=ttk.Combobox(width=30,font=30,textvariable=choice)
combo["value"]=("EUR","JPY","USD","GBP")
combo.grid(row=1,column=1)

#output
Label(text="ผลการคำนวน",padx=10,font=30).grid(row=2,sticky=W)
et2=Entry(font=30,width=30)
et2.grid(row=2,column=1)

def calcuLate():
    amount = money.get()
    currency = choice.get()
    
    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.026),"EUR (ยูโร)")
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = ((amount*3.486),"JPY (เยล)")
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = ((amount*0.031),"USD (ดอลล่า)")
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = ((amount*0.023),"GBP (ปอนด์)")
        et2.insert(0,result)
    else:
        et2.delete(0,END)
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

Button(text="คำนวน",font=30,width=15,command=calcuLate).grid(row=3,column=1,sticky=W)
Button(text="ล้าง",font=30,width=15,command=deleteText).grid(row=3,column=1,sticky=E)

root.mainloop()