import tkinter as tk
top=tk.Tk()

# top.resizable(False,True)
top.geometry("500x400+600+400")
top.title("便捷水果店")
label1=tk.Label(top,text="请输入苹果的重量",bg="#eebb53",fg="#632b21")
label1.pack()
entry1=tk.Entry(top)
entry1.pack()
label2=tk.Label(top,text="请输入梨的重量",bg="#eebb53",fg="#632b21")
label2.pack()
entry2=tk.Entry(top)
entry2.pack()
label3=tk.Label(top,text="请输入香蕉的重量",bg="#eebb53",fg="#632b21")
label3.pack()
entry3=tk.Entry(top)
entry3.pack()
listbox=tk.Listbox(top)
listbox.pack()

def click():
    ap=5
    pp=6
    bp=7
    aw=float(entry1.get())
    pw=float(entry2.get())
    bw=float(entry3.get())
    listbox.insert(0,"名称  数量  价格")
    listbox.insert(1,f"梨     {aw}kg  {ap*aw}元")
    listbox.insert(2,f"苹果  {pw}kg  {pp*pw}元")
    listbox.insert(3,f"香蕉  {bw}kg  {bp*bw}元")
    listbox.insert(4,"{}")


btn=tk.Button(top,text='结算',bg='#f7b2a6',command=click)
btn.pack()
top.mainloop()