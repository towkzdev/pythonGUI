from tkinter import *
from tkinter import ttk
root = Tk()
root.title("ComboBox")

Label(text="ที่อยู่",font=20).grid(row=0,column=0)
choice = StringVar(value="เลือกจังหวัดของคุณ")
combo = ttk.Combobox(textvariable=choice)
combo["value"] = ("กรุงเทพ","เชียงใหม่","กระบี่")
combo.grid(row=0,column=1)

root.mainloop()