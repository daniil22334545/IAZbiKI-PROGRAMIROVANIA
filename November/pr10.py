from tkinter import * 
import tkinter as tk                    
from tkinter import ttk
  
  
root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Calc')
tabControl.add(tab2, text ='Button')
tabControl.add(tab3, text ='Tab 3')
tabControl.pack(expand = 1, fill ="both")

root.geometry('260x360+100+200')
root.resizable(False, False)

 
val=""
A = 0
operator=""
 
def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)
 
def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
 
def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)
 
def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)
 
def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)
 
def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)
 
def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)
 
def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)
 
def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)
 
def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)
 
def btn_add_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)
 
def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)
 
def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)
 
def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)
 
def btn_equal_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)
 
def C_pressed():
    global A
    global operator
    global val
    val = ""
    A=0
    operator=""
    data.set(val)
 
 
def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x=int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val=str(c)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val=str(c)
    elif operator == "*":
        x=int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val=str(c)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.show("Error","Division by 0 Not Allowed")
            A==""
            val=""
            data.set(val)
        else:
            c=int(A/x)
            data.set(c)
            val=str(c)


data= StringVar()
lbl=Label(
    tab1,
    text="Label",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
)

lbl.pack(expand=True,fill="both",)

btnrow1=Frame(tab1,bg="#000000")

btnrow1.pack(expand=True,fill="both",)
 

btnrow2=Frame(tab1)
btnrow2.pack(expand=True,fill="both",)
 
btnrow3=Frame(tab1)
btnrow3.pack(expand=True,fill="both",)
 
btnrow4=Frame(tab1)
btnrow4.pack(expand=True,fill="both",)

btn1=Button(
    btnrow1,
    text = "1",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_1_isclicked,
)

btn1.pack(side=LEFT,expand=True,fill="both",)
 
btn2=Button(
    btnrow1,
    text = "2",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_2_isclicked,
)

btn2.pack(side=LEFT,expand=True,fill="both",)
 

btn3=Button(
    btnrow1,
    text = "3",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_3_isclicked,
)

btn3.pack(side=LEFT,expand=True,fill="both",)
 

btnadd=Button(
    btnrow1,
    text = "+",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_add_clicked,
)

btnadd.pack(side=LEFT,expand=True,fill="both",)
 
btn4=Button(
    btnrow2,
    text = "4",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_4_isclicked,
)

btn4.pack(side=LEFT,expand=True,fill="both",)
 
btn5=Button(
    btnrow2,
    text = "5",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_5_isclicked,
)

btn5.pack(side=LEFT,expand=True,fill="both",)
 
btn6=Button(
    btnrow2,
    text = "6",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_6_isclicked,
)

btn6.pack(side=LEFT,expand=True,fill="both",)
 
btnsub=Button(
    btnrow2,
    text = "-",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_sub_clicked,
)

btnsub.pack(side=LEFT,expand=True,fill="both",)
 
btn7=Button(
    btnrow3,
    text = "7",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_7_isclicked,
)

btn7.pack(side=LEFT,expand=True,fill="both",)
 
btn8=Button(
    btnrow3,
    text = "8",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_8_isclicked,
)

btn8.pack(side=LEFT,expand=True,fill="both",)
 
btn9=Button(
    btnrow3,
    text = "9",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_9_isclicked,
)

btn9.pack(side=LEFT,expand=True,fill="both",)
 
btnmul=Button(
    btnrow3,
    text = "*",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_mul_clicked,
)

btnmul.pack(side=LEFT,expand=True,fill="both",)
 
btnC=Button(
    btnrow4,
    text = "C",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = C_pressed,
)

btnC.pack(side=LEFT,expand=True,fill="both",)

btn0=Button(
    btnrow4,
    text = "0",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_0_isclicked,
)

btn0.pack(side=LEFT,expand=True,fill="both",)

btnequal=Button(
    btnrow4,
    text = "=",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command=result,
)

btnequal.pack(side=LEFT,expand=True,fill="both",)

btndiv=Button(
    btnrow4,
    text = "/",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_div_clicked,
     
)

btndiv.pack(side=LEFT,expand=True,fill="both",)

z = 0
def which_button(button_press):
    global z
    z = button_press
b1 = Button(tab2, text="1",
            command=lambda m="Первая кнопка":which_button(m))
 
b1.grid(padx=10, pady=10)

b2 = Button(tab2, text="2",
            command=lambda  m="Вторая кнопка":which_button(m))
b2.grid(padx=10, pady=10)

b3 = Button(tab2, text="3",
            command=lambda  m="Третья кнопка":which_button(m))
b3.grid(padx=10, pady=10)
b4 = Button(tab2, text="Result",
            command=lambda :messagebox.showinfo("Вы нажали",z))

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    with open(tf, "r") as f:
        Label(tab3, text=f.read()).pack()
b5 = Button(tab3,text="file",command=lambda:openFile())

b5.grid(padx=10,pady=10)
b4.grid(padx=10, pady=10)


root.mainloop()  
