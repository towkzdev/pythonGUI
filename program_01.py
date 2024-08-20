from tkinter import *

root = Tk() #หน้าต่างโปรแกรม widget
root.title("My GUI")


#กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x400+0+0")

#การแสดงผลข้อความ
myLabel = Label(root,text="Hello World",fg="blue",font=20,bg="grey").pack()
myLabel = Label(root,text="Satjaphon Panyafu").pack()

#จัดเรียง Widget ด้วย Place และ Grid
myLabel = Label(root,text="DevGr").place(x=0,y=0)
myLabel = Label(root,text="Computer Engineering").place(x=50,y=200)
#myLabel = Label(root,text="Naresuan University").grid(row=4,column=4)

#การสร้างปุ่ม (Button)
btn1 = Button(text="บันทึก",fg="white",bg="green").pack()
btn2 = Button(text="ยกเลิก",fg="white",bg="red").pack()

#Button Command
def showMessage():
    Label(root,text="Hello DevGr",font=20,fg="red",bg="black").pack()

btn3 = Button(text="ShowMessage",command=showMessage).pack()
#twersds
#การสร้างหน้าจอหลายๆหน้า
def openWindow():
    #หน้าจอที่ 2
    myWindow = Tk()
    myWindow.title("รายงานผล")
    myWindow.geometry("500x300")

    Label(myWindow,text="Hello DevGr",font=20,fg="red",bg="black").pack()
    myText = Entry(myWindow,textvariable=txt).pack()
    
#การสร้างกล่องข้อความ (TextBox)
def addMessage():
    message = txt.get()
    print(message)
    Label(root,text=message,font=20,fg="red",bg="black").pack()

    
txt = StringVar()
myText = Entry(root,textvariable=txt).pack()
btn3 = Button(text="AddMessage",command=addMessage).pack()
btn3 = Button(text="เปิดรายงาน",command=openWindow).pack()

#การสร้างเมนู (Menu)



root.mainloop()

