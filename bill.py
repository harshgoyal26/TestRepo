from tkinter import* 
import math,random,os 
from tkinter import messagebox 
from datetime import datetime
from PIL import ImageTk,Image

root = Tk()

class Bill_App:
    def __init__(self,root):  
        self.root=root 
        self.root.geometry("1500x1000+0+0")  
        self.root.title("Billing Softwate ") 
        bg_color="light grey" 
        title=Label(self.root,text="INVOICE GENERATOR",bd=2,relief=SUNKEN,bg=bg_color,fg="darkturquoise",font=("comic sans ms",25,"bold"),pady=2).pack(fill=X) 
        
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        self.var5=IntVar()
        self.var6=IntVar() 
        self.var7=IntVar()
        self.var8=IntVar()
        self.var9=IntVar()
        self.var10=IntVar()
        self.var11=IntVar()
        self.var12=IntVar() 
        self.var13=IntVar()
        self.var14=IntVar()
        self.var15=IntVar()
        self.var16=IntVar()
        self.var17=IntVar()
        self.var18=IntVar()
        self.var19=IntVar()
        self.var20=IntVar()
        self.var21=IntVar()
        self.var22=IntVar()
        self.var23=IntVar()
        self.var24=IntVar()
        self.var25=IntVar()
        self.var26=IntVar()
        self.var27=IntVar()
        self.var28=IntVar()
        self.var29=IntVar()
        self.var30=IntVar()
        self.var31=IntVar()
        self.var32=IntVar()
        self.var33=IntVar()
        self.var34=IntVar()
        self.var35=IntVar()
        self.var36=IntVar()
        self.var37=IntVar()
        self.var38=IntVar()
 
        self.total_food_price=StringVar() 
        self.total_bill_amount=StringVar()
        self.total_tax=StringVar() 
        
        self.c_name=StringVar() 
        self.c_phon=StringVar() 
        self.bill_no=StringVar()
        x=random.randint(1,9999) 
        self.bill_no.set(str(x)) 
        self.search_bill=StringVar() 
 
#Frames Display Screen Division
        F1=LabelFrame(self.root,bd=2,relief=GROOVE,text="Customer Details",font=("comic sans ms",12,"bold"),fg="darkturquoise",bg=bg_color) 
        F1.place(x=0,y=755,relwidth=1,height=90) 
        
        F2=LabelFrame(self.root,bd=2,relief=GROOVE,text="ONE",font=("comic sans ms",12),fg="darkturquoise",bg=bg_color) 
        F2.place(x=0,y=65,width=245,height=510)
        
        F3=LabelFrame(self.root,bd=2,relief=GROOVE,text="TWO",font=("comic sans ms",12),fg="darkturquoise",bg=bg_color) 
        F3.place(x=245,y=65,width=245,height=510)
        
        F4=LabelFrame(self.root,bd=2,relief=GROOVE,text="THREE",font=("comic sans ms",12),fg="darkturquoise",bg=bg_color) 
        F4.place(x=490,y=65,width=245,height=510)
                
        F5=Frame(self.root,bd=2,relief=GROOVE) 
        F5.place(x=980 ,y=65,width=500,height=510) 
        
        F6=LabelFrame(self.root,bd=2,relief=GROOVE,text="Bill Amount",font=("comic sans ms",12),fg="darkturquoise",bg=bg_color) 
        F6.place(x=0,y=575,relwidth=1,height=180)
        
        F7=LabelFrame(self.root,bd=2,relief=GROOVE,text="FOUR",font=("comic sans ms",12),fg="darkturquoise",bg=bg_color) 
        F7.place(x=735,y=65,width=245,height=255)
        
        F8=LabelFrame(self.root,bd=2,relief=GROOVE,text="FIVE",font=("comic sans ms",12),fg="darkturquoise",bg=bg_color) 
        F8.place(x=735,y=320,width=245,height=255)
        
        F61=Frame(F6,bd=2,relief=GROOVE,bg=bg_color) 
        F61.place(x=910,width=540,height=70)
        
        F62=Frame(F6,bd=2,relief=GROOVE,bg=bg_color) 
        F62.place(x=910,y=75,width=540,height=70)        
        
#Frame1
        
        f1t1=Label(F1,text="Customer Name",bg=bg_color,fg="blue",font=("comic sans ms",15)).grid(row=0,column=0,padx=20,pady=5) 
        f1e1=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=4,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10) 
 
        f1t2=Label(F1,text="Phone Number",bg=bg_color,fg="blue",font=("comic sans ms",15)).grid(row=0,column=2,padx=20,pady=5) 
        f1e2=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=4,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10) 
        f1a2=Label(F1,text="                                           ",bg=bg_color).grid(row=0,column=4,padx=20,pady=5)
        
        f1t3=Label(F1,text="Bill Number",bg=bg_color,fg="blue",font=("comic sans ms",15)).grid(row=0,column=5,padx=20,pady=5) 
        f1e3=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=4,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10) 
 
        search_btn=Button(F1,text="Search",command=self.find_bill,bg=bg_color,fg="darkturquoise",width=10,bd=2,font="arial 12 bold").grid(row=0,column=7,padx=10,pady=10) 
        #search_btn.bind("/",self.find_bill)
 
#Frame2 

        f2t1=Label(F2,text="ITEM 1",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=7,sticky="w") 
        f2e1=Entry(F2,width=5,textvariable=self.var1,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7) 
 
        f2t2=Label(F2,text="ITEM 2",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=8,sticky="w") 
        f2e2=Entry(F2,width=5,textvariable=self.var2,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=8) 
 
        f2t3=Label(F2,text="ITEM 3",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=7,sticky="w") 
        f2e3=Entry(F2,width=5,textvariable=self.var3,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=7) 
 
        f2t4=Label(F2,text="ITEM 4",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=3,column=0,padx=10,pady=8,sticky="w") 
        f2e4=Entry(F2,width=5,textvariable=self.var4,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=8) 
 
        f2t5=Label(F2,text="ITEM 5",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=4,column=0,padx=10,pady=8,sticky="w") 
        f2e5=Entry(F2,width=5,textvariable=self.var5,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8) 
 
        f2t6=Label(F2,text="ITEM 6",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=5,column=0,padx=10,pady=7,sticky="w") 
        f2e6=Entry(F2,width=5,textvariable=self.var6,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=7) 
        
        f2t7=Label(F2,text="ITEM 7",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=6,column=0,padx=10,pady=8,sticky="w") 
        f2e7=Entry(F2,width=5,textvariable=self.var7,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=8) 
        
        f2t8=Label(F2,text="ITEM 8",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=7,column=0,padx=10,pady=8,sticky="w") 
        f2e8=Entry(F2,width=5,textvariable=self.var8,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=8) 
 
        f2t9=Label(F2,text="ITEM 9",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=8,column=0,padx=10,pady=7,sticky="w") 
        f2e9=Entry(F2,width=5,textvariable=self.var9,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=7) 
  
        f2t10=Label(F2,text="ITEM 10",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=9,column=0,padx=10,pady=8,sticky="w") 
        f2e10=Entry(F2,width=5,textvariable=self.var10,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=8) 
     
#Frame3 
 
        f3t1=Label(F3,text="ITEM 11",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=7,sticky="w") 
        f3e1=Entry(F3,width=5,textvariable=self.var11,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7) 
 
        f3t2=Label(F3,text="ITEM 12",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=8,sticky="w") 
        f3e2=Entry(F3,width=5,textvariable=self.var12,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=7) 
 
        f3t3=Label(F3,text="ITEM 13",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=7,sticky="w") 
        f3e3=Entry(F3,width=5,textvariable=self.var13,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=7) 
 
        f3t4=Label(F3,text="ITEM 14",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=3,column=0,padx=10,pady=8,sticky="w") 
        f3e4=Entry(F3,width=5,textvariable=self.var14,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=8) 
 
        f3t5=Label(F3,text="ITEM 15",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=4,column=0,padx=10,pady=8,sticky="w") 
        f3e5=Entry(F3,width=5,textvariable=self.var15,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8) 
 
        f3t6=Label(F3,text="ITEM 16",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=5,column=0,padx=10,pady=7,sticky="w") 
        f3e6=Entry(F3,width=5,textvariable=self.var16,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=7) 
        
        f3t7=Label(F3,text="ITEM 17",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=6,column=0,padx=10,pady=8,sticky="w") 
        f3e7=Entry(F3,width=5,textvariable=self.var17,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=8) 
        
        f3t8=Label(F3,text="ITEM 18",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=7,column=0,padx=10,pady=8,sticky="w") 
        f3e8=Entry(F3,width=5,textvariable=self.var18,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=8) 
        
        f3t9=Label(F3,text="ITEM 19",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=8,column=0,padx=10,pady=7,sticky="w") 
        f3e9=Entry(F3,width=5,textvariable=self.var19,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=7) 
        
        f3t10=Label(F3,text="ITEM 20",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=9,column=0,padx=10,pady=8,sticky="w") 
        f3e10=Entry(F3,width=5,textvariable=self.var20,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=8) 
            
#Frame4 
 
        f4t1=Label(F4,text="ITEM 21",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=7,sticky="w") 
        f4e1=Entry(F4,width=5,textvariable=self.var21,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=7) 

        f4t2=Label(F4,text="ITEM 22",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=8,sticky="w") 
        f4e2=Entry(F4,width=5,textvariable=self.var22,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=8) 
 
        f4t3=Label(F4,text="ITEM 23",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=7,sticky="w") 
        f4e3=Entry(F4,width=5,textvariable=self.var23,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=7) 
 
        f4t4=Label(F4,text="ITEM 24",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=3,column=0,padx=10,pady=8,sticky="w") 
        f4e4=Entry(F4,width=5,textvariable=self.var24,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=7) 
 
        f4t5=Label(F4,text="ITEM 25",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=4,column=0,padx=10,pady=8,sticky="w") 
        f4e5=Entry(F4,width=5,textvariable=self.var25,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8) 
 
        f4t6=Label(F4,text="ITEM 26",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=5,column=0,padx=10,pady=7,sticky="w") 
        f4e6=Entry(F4,width=5,textvariable=self.var26,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=7) 
        
        f4t7=Label(F4,text="ITEM 27",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=6,column=0,padx=10,pady=8,sticky="w") 
        f4e7=Entry(F4,width=5,textvariable=self.var27,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=8) 
        
        f4t8=Label(F4,text="ITEM 28",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=7,column=0,padx=10,pady=8,sticky="w") 
        f4e8=Entry(F4,width=5,textvariable=self.var28,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=8) 
        
        f4t9=Label(F4,text="ITEM 29",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=8,column=0,padx=10,pady=7,sticky="w") 
        f4e9=Entry(F4,width=5,textvariable=self.var29,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=7) 
        
        f4t10=Label(F4,text="ITEM 30",font=("comic sans ms",14),bg=bg_color,fg="blue").grid(row=9,column=0,padx=10,pady=8,sticky="w") 
        f4e10=Entry(F4,width=5,textvariable=self.var30,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=8) 
 
#Frame 5 BILL AREA 
         
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X) 
        scrol_y=Scrollbar(F5,orient=VERTICAL) 
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set) 
        scrol_y.pack(side=RIGHT,fill=Y) 
        scrol_y.config(command=self.txtarea.yview) 
        self.txtarea.pack(fill=BOTH,expand=1) 
 
#Frame6 & Button 
 
        f6t1=Label(F6,text="Total Item Price",bg=bg_color,fg="blue",font=("comic sans ms",14)).grid(row=0,column=0,padx=20,pady=1,sticky="w") 
        f6e1=Entry(F6,width=18,textvariable=self.total_food_price,font="aria 10 bold",bd=4,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=20) 
 
        f6t=Label(F6,text="Total Bill Amount",bg=bg_color,fg="blue",font=("comic sans ms",14)).grid(row=1,column=0,padx=20,pady=1,sticky="w") 
        f6e=Entry(F6,width=18,textvariable=self.total_bill_amount,font="aria 10 bold",bd=4,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=20) 
 
        f6t2=Label(F6,text="Total Tax",bg=bg_color,fg="blue",font=("comic sans ms",14)).grid(row=0,column=2,padx=20,pady=1,sticky="w") 
        f6e2=Entry(F6,width=18,textvariable=self.total_tax,font="aria 10 bold",bd=4,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=20) 
 
        total_btn=Button(F61,command=self.total,text="Total",bg=bg_color,fg="blue",bd=2,pady=5,width=8,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5) 
 
        Gbill_btn=Button(F61,command=self.bill_area,text="Generate Bill",bg=bg_color,fg="blue",bd=2,pady=5,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5) 
 
        Clear_btn=Button(F61,command=self.clear_data,text="Clear",bg=bg_color,fg="blue",bd=2,pady=5,width=8,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5) 
 
        aExit_btn=Button(F61,command=self.Exit_app,text="Exit",bg=bg_color,fg="blue",bd=2,pady=5,width=8,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5) 
        
        extra1=Button(F62,command=self.pay,text="Payment",bg=bg_color,fg="blue",bd=2,pady=5,width=20,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        
        #extra2=Button(F62,command=self.cod,text="COD",bg=bg_color,fg="spring green",bd=2,pady=5,width=20,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
                
        self.welcome_bill() 
        
#Frame 7
        
        f7t1=Label(F7,text="ITEM 31",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=10,sticky="w") 
        f7e1=Entry(F7,width=5,textvariable=self.var31,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10) 
 
        f7t2=Label(F7,text="ITEM 31",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=10,sticky="w") 
        f7e2=Entry(F7,width=5,textvariable=self.var32,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10) 
 
        f7t3=Label(F7,text="ITEM 33",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=10,sticky="w") 
        f7e3=Entry(F7,width=5,textvariable=self.var33,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10) 
 
        f7t4=Label(F7,text="ITEM 34",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=3,column=0,padx=10,pady=10,sticky="w") 
        f7e4=Entry(F7,width=5,textvariable=self.var34,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10) 
        
#Frame 8
        
        f8t1=Label(F8,text="ITEM 35",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=10,sticky="w") 
        f8e1=Entry(F8,width=5,textvariable=self.var35,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10) 
 
        f8t2=Label(F8,text="ITEM 36",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=10,sticky="w") 
        f8e2=Entry(F8,width=5,textvariable=self.var36,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10) 
 
        f8t3=Label(F8,text="ITEM 37",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=10,sticky="w") 
        f8e3=Entry(F8,width=5,textvariable=self.var37,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10) 
 
        f8t4=Label(F8,text="ITEM 38",font=("comic sans ms",15),bg=bg_color,fg="blue").grid(row=3,column=0,padx=10,pady=10,sticky="w") 
        f8e4=Entry(F8,width=5,textvariable=self.var38,font=("times new roman",11,"bold"),bd=2,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10) 

    def total(self): 
 
        self.f1=self.var1.get()*250
        self.f2=self.var2.get()*150
        self.f3=self.var3.get()*250
        self.f4=self.var4.get()*150
        self.f5=self.var5.get()*200
        self.f6=self.var6.get()*250
        self.f7=self.var7.get()*250
        self.f8=self.var8.get()*100
        self.f9=self.var9.get()*250
        self.f10=self.var10.get()*300
        self.f11=self.var11.get()*180
        self.f12=self.var12.get()*120
        self.f13=self.var13.get()*90
        self.f14=self.var14.get()*70
        self.f15=self.var15.get()*45
        self.f16=self.var16.get()*90
        self.f17=self.var17.get()*50
        self.f18=self.var18.get()*90
        self.f19=self.var19.get()*120
        self.f20=self.var20.get()*280
        self.f21=self.var21.get()*350
        self.f22=self.var22.get()*410
        self.f23=self.var23.get()*370
        self.f24=self.var24.get()*450
        self.f25=self.var25.get()*450
        self.f26=self.var26.get()*370
        self.f27=self.var27.get()*345
        self.f28=self.var28.get()*390
        self.f29=self.var29.get()*310
        self.f30=self.var30.get()*400
        self.f31=self.var31.get()*80
        self.f32=self.var32.get()*140
        self.f33=self.var33.get()*200
        self.f34=self.var34.get()*150
        self.f35=self.var35.get()*150
        self.f36=self.var36.get()*120
        self.f37=self.var37.get()*75
        self.f38=self.var38.get()*90
        
        self.one=float(self.f1+self.f2+self.f3+self.f4+self.f5+self.f6+self.f7+self.f8+self.f9+self.f10) 
        self.two=float(self.f11+self.f12+self.f13+self.f14+self.f15+self.f16+self.f17+self.f18+self.f19+self.f20)
        self.three=float(self.f21+self.f22+self.f23+self.f24+self.f25+self.f26+self.f27+self.f28+self.f29+self.f30)
        self.four=float(self.f31+self.f32+self.f33+self.f34)
        self.five=float(self.f35+self.f36+self.f37+self.f38)
        
        self.total_price=float(self.one+self.two+self.three+self.four+self.five)
        self.total_food_price.set("Rs." + str(self.total_price))
        
        self.tax=round((self.total_price*0.05),2) 
        self.total_tax.set("Rs."+str(self.tax)) 
  
        self.total_amount = float(self.total_price+self.tax) 
        self.total_bill_amount.set("Rs."+str(self.total_amount))
        #self.bill_area() 

    def welcome_bill(self):
        today = datetime.now()
        self.txtarea.delete('1.0',END) 
        self.txtarea.insert(END,f" Thanks for your visit :)  {today} \n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}") 
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}") 
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()}") 
        self.txtarea.insert(END,f"\n=========================================================") 
        self.txtarea.insert(END,f"\n Products \t\tPrice \t\tQuantity \t\tAmount ") 
        self.txtarea.insert(END,f"\n=========================================================\n")  
 
    def bill_area(self): 
        if self.c_name.get()=="" or self.c_phon.get()=="": 
            messagebox.showerror("Error","Customer Details are must") 
        else: 
            self.welcome_bill() 
            
            if self.var1.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 1\t\t250 \t\t{self.var1.get()}\t\t{self.f1}") 
 
            if self.var2.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 2\t\t150 \t\t{self.var2.get()}\t\t{self.f2}") 
 
            if self.var3.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 3\t\t250 \t\t{self.var3.get()}\t\t{self.f3}") 
 
            if self.var4.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 4\t\t150 \t\t{self.var4.get()}\t\t{self.f4}") 
 
            if self.var5.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 5\t\t200 \t\t{self.var5.get()}\t\t{self.f5}") 
 
            if self.var6.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 6\t\t250 \t\t{self.var6.get()}\t\t{self.f6}") 
 
            if self.var7.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 7\t\t250 \t\t{self.var7.get()}\t\t{self.f7}") 
 
            if self.var8.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 8\t\t100 \t\t{self.var8.get()}\t\t{self.f8}") 
 
            if self.var9.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 9\t\t250 \t\t{self.var9.get()}\t\t{self.f9}") 
 
            if self.var10.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 10\t\t300 \t\t{self.var10.get()}\t\t{self.f10}") 
 
            if self.var11.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 11\t\t180 \t\t{self.var11.get()}\t\t{self.f11}") 
 
            if self.var12.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 12\t\t120 \t\t{self.var12.get()}\t\t{self.f12}") 

            if self.var13.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 13\t\t90 \t\t{self.var13.get()}\t\t{self.f13}") 
 
            if self.var14.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 14\t\t70 \t\t{self.var14.get()}\t\t{self.f14}") 
 
            if self.var15.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 15\t\t45 \t\t{self.var15.get()}\t\t{self.f15}") 
 
            if self.var16.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 16\t\t90 \t\t{self.var16.get()}\t\t{self.f16}") 
 
            if self.var17.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 17\t\t50 \t\t{self.var17.get()}\t\t{self.f17}") 
 
            if self.var18.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 18\t\t90 \t\t{self.var18.get()}\t\t{self.f18}")
                
            if self.var19.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 19\t\t120 \t\t{self.var19.get()}\t\t{self.f19}")
                
            if self.var20.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 20\t\t280 \t\t{self.var20.get()}\t\t{self.f20}")
                
            if self.var21.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 21\t\t350 \t\t{self.var21.get()}\t\t{self.f21}")
                
            if self.var22.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 22\t\t410 \t\t{self.var22.get()}\t\t{self.f22}")
                
            if self.var23.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 23\t\t370 \t\t{self.var23.get()}\t\t{self.f23}")
                
            if self.var24.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 24\t\t450 \t\t{self.var24.get()}\t\t{self.f24}")
                
            if self.var25.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 25\t\t450 \t\t{self.var25.get()}\t\t{self.f25}")
                
            if self.var26.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 26\t\t370 \t\t{self.var26.get()}\t\t{self.f26}")
             
            if self.var27.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 27\t\t345 \t\t{self.var27.get()}\t\t{self.f27}")
                
            if self.var28.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 28\t\t390 \t\t{self.var28.get()}\t\t{self.f28}")    
                
            if self.var29.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 29\t\t310 \t\t{self.var29.get()}\t\t{self.f29}")
                
            if self.var30.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 30\t\t400 \t\t{self.var30.get()}\t\t{self.f30}")
                
            if self.var31.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 31\t\t80 \t\t{self.var31.get()}\t\t{self.f31}")
                
            if self.var32.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 32\t\t140 \t\t{self.var32.get()}\t\t{self.f32}")
                
            if self.var33.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 33\t\t200 \t\t{self.var33.get()}\t\t{self.f33}")
                
            if self.var34.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 34\t\t150 \t\t{self.var34.get()}\t\t{self.f34}")
                
            if self.var35.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 35\t\t150 \t\t{self.var35.get()}\t\t{self.f35}")
                
            if self.var36.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 36\t\t120 \t\t{self.var36.get()}\t\t{self.f36}")
                
            if self.var37.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 37\t\t75 \t\t{self.var37.get()}\t\t{self.f37}")
                
            if self.var38.get()!=0: 
                self.txtarea.insert(END,f"\n ITEM 38\t\t90 \t\t{self.var38.get()}\t\t{self.f38}")    
                
            self.txtarea.insert(END,f"\n---------------------------------------------------------") 
            
            if self.total_food_price.get()!="Rs.0.0": 
                self.txtarea.insert(END,f"\n Total ITEM Price: \t\t\t\t\tRs. {self.total_price}") 
             
            if self.total_tax.get()!="Rs.0.0": 
                self.txtarea.insert(END,f"\n Total Tax: \t\t\t\t\tRs. {self.tax}") 
 
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t\t\tRs. {self.total_amount}") 
            self.txtarea.insert(END,f"\n---------------------------------------------------------") 
            
            self.save_bill() 
 
    def save_bill(self): 
        op=messagebox.askyesno("Save Bill","Do you want to save the bill") 
        if op>0: 
            self.bill_data=self.txtarea.get('1.0',END) 
            f1=open("C:\\Users\\Harsh\\Desktop\\savedbill/"+str(self.bill_no.get())+".txt","w") 
            f1.write(self.bill_data) 
            f1.close() 
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully") 
        else: 
            return 
 
    def find_bill(self): 
        present="a" 
        for i in os.listdir("C:\\Users\\Harsh\\Desktop\\savedbill/"): 
            if i.split(".")[0]==self.search_bill.get(): 
                f1=open(f"C:\\Users\\Harsh\\Desktop\\savedbill\\{i}","r") 
                self.txtarea.delete("1.0",END) 
                for d in f1: 
                    self.txtarea.insert(END,d)
                messagebox.showinfo("Showing",f"Bill no. : {self.search_bill.get()} showing")
                f1.close() 
                present="b" 
        if present=="a": 
            messagebox.showerror("Error","Invalid Bill Number") 
 
    def clear_data(self): 
        op=messagebox.askyesno("Clear","Do you want to Clear") 
        if op>0: 
            
            self.var1.set(0) 
            self.var2.set(0) 
            self.var3.set(0) 
            self.var4.set(0) 
            self.var5.set(0) 
            self.var6.set(0) 
            self.var7.set(0) 
            self.var8.set(0) 
            self.var9.set(0) 
            self.var10.set(0) 
            self.var11.set(0) 
            self.var12.set(0) 
            self.var13.set(0) 
            self.var14.set(0) 
            self.var15.set(0) 
            self.var16.set(0) 
            self.var17.set(0) 
            self.var18.set(0)
            self.var19.set(0)
            self.var20.set(0)
            self.var21.set(0)
            self.var22.set(0)
            self.var23.set(0)
            self.var24.set(0)
            self.var25.set(0)
            self.var26.set(0)
            self.var27.set(0)
            self.var28.set(0)
            self.var29.set(0)
            self.var30.set(0)
            self.var31.set(0)
            self.var32.set(0)
            self.var33.set(0)
            self.var34.set(0)
            self.var35.set(0)
            self.var36.set(0)
            self.var37.set(0)
            self.var38.set(0)
 
            self.total_food_price.set("") 
            self.total_bill_amount.set("") 
 
            self.total_tax.set("")  

            self.c_name.set("") 
            self.c_phon.set("") 
            self.bill_no.set("") 
            x=random.randint(1,9999) 
            self.bill_no.set(str(x)) 
            self.search_bill.set("")
            
            self.welcome_bill() 
 
    def Exit_app(self): 
        op=messagebox.askyesno("Exit","Do you want to exit") 
        if op>0: 
            self.root.destroy() 
            
    def pay(self):
        import ig



        
obj = Bill_App(root) 
root.mainloop()
