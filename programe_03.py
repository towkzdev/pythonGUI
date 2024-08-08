from  tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My Gui 03")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    myLabel = Label(text="Hello Python",bg=color[1]).pack()

def selectFile():
    fileopen = askopenfile()
    myLabel = Label(text=fileopen).pack()

def selectFilename():
    fileopen = askopenfilename()
    fileContent = open(fileopen,encoding="utf8")
    myLabel = Label(text=fileContent.read()).pack()


#หน้าต่างเลือกสี (Color Chooser)
btn1 = Button(text="เลือกสี",command=selectColor).pack()

#หน้าต่างเลือกไฟล์ (File Dialog)
btn2 = Button(text="OpenFile",command=selectFile).pack()

#อ่านเนื้อหาจากไฟล์
btn3 = Button(text="OpenFileName",command=selectFilename).pack()


root.mainloop()