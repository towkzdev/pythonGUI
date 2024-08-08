#การสร้างเมนู (Menu)

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI_2")
root.geometry("500x500")

#สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)

#การสร้างหน้าต่างใหม่
def showWindow():
    window = Tk()
    window.title("หน้าต่างใหม่")
    window.mainloop()

def aboutProgramr():
    messagebox.showinfo("Dev.grrrrrr","สวัสดีครับ เทสๆ!!!!")

def exitPrograme():
    confirm = messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()

#การสร้างเมนูย่อย (Menu Item)
menuItem = Menu()
menuItem.add_command(label="New Window",command=showWindow)
menuItem.add_command(label="Open File")
menuItem.add_command(label="Save File")
menuItem.add_command(label="About",command=aboutProgramr)
menuItem.add_command(label="Exit",command=exitPrograme)

#เพิ่มเมนูหลัก
myMenu.add_cascade(label="File",menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

#message box


#ปิดโปรแกรมด้วย Destroy


root.mainloop()