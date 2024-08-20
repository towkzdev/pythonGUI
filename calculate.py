from tkinter import *
root = Tk()
root.title("เครื่องคิดเลข")
#test
#test2
#asd
#test001
content = "" #เก็บสมการ
txt_input = StringVar(value="0") #นำสมการมาใช้งาน

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content=""

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")

#การแสดงผล 5x4
display = Entry(font=('arial',30,'bold'),fg="white",bg="green",textvariable=txt_input,justify="right")
display.grid(columnspan=4)

#การรับค่าผ่านปุ่ม

#row 1
btn7=Button(fg="black",font=('arial',30,'bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
btn8=Button(fg="black",font=('arial',30,'bold'),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
btn9=Button(fg="black",font=('arial',30,'bold'),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
btnc=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="C",command=clear,padx=30,pady=15).grid(row=1,column=3)
#row 2
btn4=Button(fg="black",font=('arial',30,'bold'),text="4",command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
btn5=Button(fg="black",font=('arial',30,'bold'),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
btn6=Button(fg="black",font=('arial',30,'bold'),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
btnplus=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="+",command=lambda:btn("+"),padx=30,pady=15).grid(row=2,column=3)
#row 3
btn1=Button(fg="black",font=('arial',30,'bold'),text="1",command=lambda:btn(1),padx=30,pady=15).grid(row=3,column=0)
btn2=Button(fg="black",font=('arial',30,'bold'),text="2",command=lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
btn3=Button(fg="black",font=('arial',30,'bold'),text="3",command=lambda:btn(3),padx=30,pady=15).grid(row=3,column=2)
btnminus=Button(fg="black",bg="orange",font=('arial',50,'bold'),text="-",command=lambda:btn("-"),padx=35,pady=15).grid(row=3,column=3)
#row 4
btnDOT=Button(fg="black",font=('arial',30,'bold'),text=".",command=lambda:btn("."),padx=35,pady=15).grid(row=4,column=0)
btn0=Button(fg="black",font=('arial',30,'bold'),text="0",command=lambda:btn(0),padx=30,pady=15).grid(row=4,column=1)
btn3division=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="/",command=lambda:btn("/"),padx=35,pady=15).grid(row=4,column=2)
btnmultiply=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="X",command=lambda:btn("*"),padx=30,pady=15).grid(row=4,column=3)
#row 5
btnequal=Button(fg="black",bg="cyan",font=('arial',30,'bold'),text="=",command=equal,padx=95,pady=15).grid(row=5,column=2,columnspan=2)
btnopen=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="(",command=lambda:btn("("),padx=30,pady=15).grid(row=5,column=0)
btnclose=Button(fg="black",bg="orange",font=('arial',30,'bold'),text=")",command=lambda:btn(")"),padx=35,pady=15).grid(row=5,column=1)

root.mainloop()
