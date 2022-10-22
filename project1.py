#scool marksheet
from tkinter.messagebox import askyesno,showerror
from tkinter import *
from PIL import ImageTk,Image
a = Tk()
def test():
    showerror(title="ERROR", message="PLEASE ENTER YOUR NAME")

def python():
    name = var1.get()
    h1 = var2.get()
    en1 = var3.get()
    sc1 = var4.get()
    math = var5.get()
    sst = var6.get()
    total = h1 + en1 + sc1 + math + sst 
    per = (total/500)*100
    div = ""
    if name == "":
        test()
    else:
        if per>=80 and per<101:
            div = "1st "
        elif per<80 and per>=60:
            div = "2nd "
        elif per<60 and per>=35:
            div = "3rd "
        else:
            div = "you are fail"
        message(name, total, per, div)
def message(a_1,b,c,d):
    print_1 = f'''
                      NAME :- {a_1}
                      TOTAL MARKS :- {b}
                      PERCENTAGE :- {c}
                      DIVISION :-  {d}'''
    var_1 =askyesno(title="CAN YOU WANT YOUR SCORE CARD",message=print_1)
    if var_1:
        result(a_1,b,c,d)
    else:
        pass
def result(a_1,b,c,d):
    tp = Toplevel(a)
    tp.title("YOUR SCORE CARD")
    tp.config(bg="CadetBlue2")
    #---------------------------------
    scool_name = Label(tp,text="HARE KRISHANA SCHOOL",font=("Times New Roman",40,"bold"),bg="CadetBlue2")
    scool_name.place(x=350,y=20,height=80,width=800)

    scool_name = Label(tp,text="PRIMARY SCHOOL OF GOVERMENT PVT.",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    scool_name.place(x=320,y=110,height=50,width=800)
    #------------------------------------------
    img = ImageTk.PhotoImage(Image.open(r"1_11.jpg"))
    lb= Label(tp,image=img)
    lb.place(x=50,y=600,height=50,width=300)

    st5_name = Label(tp,text="PRINCIPLE",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    st5_name.place(x=50,y=700,height=30,width=300)

    img = ImageTk.PhotoImage(Image.open(r"2_2.jpg"))
    lb= Label(tp,image=img)
    lb.place(x=500,y=630,height=50,width=300)

    st5_name = Label(tp,text="HEAD OF DEPARTMENT",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    st5_name.place(x=500,y=700,height=30,width=350)

    img = ImageTk.PhotoImage(Image.open(r"3.jpg"))
    lb= Label(tp,image=img)
    lb.place(x=950,y=630,height=50,width=300)

    st5_name = Label(tp,text="OVER ALL CO-NAME",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    st5_name.place(x=950,y=700,height=30,width=350)
    #------------------------------------------
    img = ImageTk.PhotoImage(Image.open(r"l7.jpg"))
    lb= Label(tp,image=img,bg="CadetBlue2")
    lb.place(x=150,y=5,height=230,width=150)
    #------------------------------------------
    lb = Label(tp, text=f"NAME OF STUDENT :-    {a_1}",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    lb.place(x=200,y=230,height=50,width=1000)
    lb = Label(tp, text=f"TOTAL MARKS     :-     {b}  ",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    lb.place(x=200,y=300,height=50,width=800)
    lb = Label(tp, text=f"PERCENTAGE      :- {c} ",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    lb.place(x=200,y=370,height=50,width=800)
    lb = Label(tp, text=f"DIVISION        :-  {d} ",font=("Times New Roman",20,"bold"),bg="CadetBlue2")
    lb.place(x=200,y=440,height=50,width=800)   
    tp.mainloop()
        
    
var1 = StringVar()#it is used to get string value 
var2 = DoubleVar()#it is used to get integer
var3 = DoubleVar()
var4 = DoubleVar()
var5 = DoubleVar()
var6 = DoubleVar()
#----------------------------------------
a.config(bg="aquamarine1")
a.title("HARE KRISHANA SCHOOL MARKSHEET")
a.iconbitmap("R.png")
a.geometry("600x700")
#a.resizable(False,False)
#------------------------------------------
scool_name = Label(a,text="HARE KRISHANA SCHOOL",font=("Times New Roman",40,"bold"),bg="blueviolet")
scool_name.place(x=350,y=20,height=100,width=800)
#-------------------------------------------
st_name = Label(a,text="STUDENT NAME :- ",font=("Times New Roman",20,"bold"),bg="aquamarine1")
st_name.place(x=300,y=180,height=30,width=300)

st_entry = Entry(a,font=("Times New Roman",20,"bold"),bg="aquamarine1",textvariable=var1)
st_entry.place(x=800,y=180,height=30,width=400)
#----------------------------------------------
scool_name1 = Label(a,text="SUBJECT NAME",font=("Times New Roman",30,"bold"),bg="aquamarine1")
scool_name1.place(x=500,y=230,height=50,width=400)
#----------------------------------------------
l = ["Hindi", "English", "Science", "Math", "SST"]

s1_name = Label(a,text="HINDI",font=("Times New Roman",20,"bold"),bg="aquamarine1")
s1_name.place(x=300,y=300,height=30,width=300)

s1_entry = Entry(a,font=("Times New Roman",20,"bold"),bg="aquamarine1",textvariable=var2)
s1_entry.place(x=800,y=300,height=30,width=400)
#---------------------------------------------
s2_name = Label(a,text="ENGLISH",font=("Times New Roman",20,"bold"),bg="aquamarine1")
s2_name.place(x=300,y=350,height=30,width=300)

s2_entry = Entry(a,font=("Times New Roman",20,"bold"),bg="aquamarine1",textvariable=var3)
s2_entry.place(x=800,y=350,height=30,width=400)
#----------------------------------------------
st3_name = Label(a,text="SCIENCE",font=("Times New Roman",20,"bold"),bg="aquamarine1")
st3_name.place(x=300,y=400,height=30,width=300)

st3_entry = Entry(a,font=("Times New Roman",20,"bold"),bg="aquamarine1",textvariable=var4)
st3_entry.place(x=800,y=400,height=30,width=400)
#-----------------------------------------------
st4_name = Label(a,text="MATHEMATHICS",font=("Times New Roman",20,"bold"),bg="aquamarine1")
st4_name.place(x=300,y=450,height=30,width=300)

st4_entry = Entry(a,font=("Times New Roman",20,"bold"),bg="aquamarine1",textvariable=var5)
st4_entry.place(x=800,y=450,height=30,width=400)
#------------------------------------------------
st5_name = Label(a,text="SST",font=("Times New Roman",20,"bold"),bg="aquamarine1")
st5_name.place(x=300,y=500,height=30,width=300)

st5_entry = Entry(a,font=("Times New Roman",20,"bold"),bg="aquamarine1",textvariable=var6)
st5_entry.place(x=800,y=500,height=30,width=400)
#-------------------------------------------------

#---------------------------------------------------
but = Button(a,text="SUBMIT",font=(50),command=python)
but.place(x=950,y=550,height=50,width=100)

a.mainloop()