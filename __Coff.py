# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# coding: utf-8

import sys,csv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap,QFont,QStandardItemModel,QStandardItem
from PyQt5.QtCore import QStringListModel,Qt,QDateTime
from fractions import Fraction
from math import ceil


# %%
CoffeeBeans = 'CoffeeBeans.csv'

PrintLabels = 'Roasted.tex'

PotsTemplate = 'PotsTemplate.tex'
DripTemplate = 'DripTemplate.tex'
PriceTemplate = 'PriceTemplate.tex'
PricePrevious = 'PricePrevious.tex'
FullInfo = 'FullInfo.tex'
DripInfo = 'DripInfo.tex'
RawInfo = 'RawInfo.tex'
PriceInfo = 'PriceInfo.tex'


# %%


getit=[]



class App(QWidget):
    
    
    Pots, FullCoffeeList, CoffeeList,Bills = [], [], [],[]
    daysto = -1
    disc = False
    Amount_Count = 0

    with open(CoffeeBeans, 'r',encoding="utf-8") as csvfile:
        Listing = csv.reader(csvfile, delimiter=',', quotechar='|')
        row_count = sum(1 for row in Listing)

    with open(CoffeeBeans, 'r',encoding="utf-8") as csvfile:
        Listing = csv.reader(csvfile, delimiter=',', quotechar='|')    
        count =0
        for row in Listing:
            #print ', '.join(row)
            count = count +1
            if count > row_count -50:
                if row[7] == '衣索比亞 耶加雪啡':
                    row[7] = '耶加雪啡'
                    row[8] = 'Yirgacheffe'
                temp = (row[7]+' '+row[9]).strip('\t')
                FullCoffeeList.append(row)
                CoffeeList.append(temp)
    
    

    
    def __init__(self):
        """
        Build App Shape And ShowUp Location
        """
        super().__init__()
        self.title = 'Coffee'
        self.left = 140
        self.top = 100
        self.width = 550
        self.height = 600
        self.initUI()
        


    def clickBox(self, state):
        """
        Discount Button, Only change Color
        """
        if state == Qt.Checked:
            self.dis_text.setStyleSheet("QLabel { color : red; }")
            self.dis_text.setText('Discounted')
            self.dis_text.setFont(QFont("Century Gothic", 14, QFont.Normal))
            self.disc = True
        else:
            self.dis_text.setText(' ')
            self.dis_text.setFont(QFont("Century Gothic", 14, QFont.Normal))
            self.disc = False

    def initUI(self):
        """
        Initial Sheets and Layouts
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        font = QFont("Century Gothic", 14, QFont.Normal)
        self.setFont(font)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setFont(font)
        self.tabs.setStyleSheet("QTabBar::tab{width:400;}")
        self.tab_bill = QWidget()
        self.tab_bill.setFont(font)
        self.tab_beans = QWidget()
        # elf.tabs.resize(800,200)

        """
        Add Tabs
        """
        self.tabs.addTab(self.tab_beans, "Beans")
        self.tabs.addTab(self.tab_bill, "Bills")

        # row1 : New, Name, Discount
        self.new_tex = QCheckBox("NewFile?", self)
        #self.label = QLabel('New File',self)

        self.bill_date = QDateEdit(self)
        self.bill_date.setDateTime(QDateTime.currentDateTime().addDays(-1))
        self.bill_date.setCalendarPopup(True)
        # self.default_date.calendarWidget().installEventFilter(self)
        self.name_text = QLineEdit(self)
        self.name_text.setFont(QFont("Microsoft JhengHei", 14, QFont.Normal))
        
        self.dis_text = QLabel('', self)
        self.dis_text.setFixedWidth(130)

        self.discount = QCheckBox("Discount?", self)
        self.discount.stateChanged.connect(self.clickBox)

        self.hbox_top = QHBoxLayout()

        self.hbox_top.addWidget(self.new_tex)
        self.hbox_top.addStretch(1)
        self.hbox_top.addWidget(self.bill_date)
        self.hbox_top.addStretch(1)
        self.hbox_top.addWidget(self.dis_text)
        self.hbox_top.addStretch(1)
        self.hbox_top.addWidget(self.discount)
        self.hbox_top.addStretch(1)
        self.hbox_top.addWidget(self.name_text)

        self.vbox_bill = QVBoxLayout()
        self.vbox_bill.addLayout(self.hbox_top)
        


        # bottom
        self.account = QCheckBox('Accounts?', self)

        self.shiping_text = QLabel('Shipping：')
        self.shiping = QSpinBox(self)
        self.shiping.setRange(0, 120)
        self.shiping.setSingleStep(5)
        self.shiping.setWrapping(True)
        self.shiping.setValue(60)


        self.pre_bill_text = QLabel('Previous Bill：')
        self.pre_bill = QSpinBox(self)
        self.pre_bill.setRange(-500, 10000)
        self.pre_bill.setSingleStep(5)
        self.pre_bill.setWrapping(True)
        self.pre_bill.setValue(0)
        
        self.some_text = QLabel('', self)
        self.some_text.setFixedWidth(120)

        self.hbox_bottom = QHBoxLayout()
        self.hbox_bottom.addWidget(self.account)
        self.hbox_bottom.addStretch(1)
        self.hbox_bottom.addWidget(self.some_text)
        self.hbox_bottom.addStretch(1)
        self.hbox_bottom.addWidget(self.shiping_text)
        self.hbox_bottom.addWidget(self.shiping)
        self.hbox_bottom.addStretch(1)

        self.hbox_bottom.addWidget(self.pre_bill_text)
        self.hbox_bottom.addWidget(self.pre_bill)

        self.b_to_tex = QPushButton('CloseToTex',self)
        self.b_to_tex.clicked.connect(self.Bills2Tex)
        self.hbox_bottom.addStretch(1)
        self.hbox_bottom.addWidget(self.b_to_tex)

        self.vbox_bill.addLayout(self.hbox_bottom)

        


        self.hbox_bean = QHBoxLayout()
    
        self.default_date = QDateEdit(self)
        self.default_date.setDateTime(QDateTime.currentDateTime().addDays(-1))
        self.default_date.setCalendarPopup(True)
        self.hbox_bean.addWidget(self.default_date)
        
        
        self.PotsAmount = QLabel('', self)
        self.PotsAmount.setStyleSheet("QLabel { color : blue; }")
        self.PotsAmount.setFixedWidth(60)
        self.hbox_bean.addWidget(self.PotsAmount)
        
        self.to_tex = QPushButton('CloseToTex',self)
        self.to_tex.clicked.connect(self.Pots2Tex)
        self.hbox_bean.addWidget(self.to_tex)


        self.grid_beans = QGridLayout()
        
        
        

        for ix in range(12):
            self.Pots.append(self.createPot())    
            self.grid_beans.addWidget(self.Pots[ix],int(ix/4),int(ix%4))



        self.tab_beans.layout = QVBoxLayout(self)
        #self.grid_beans.setFixedWidth(500)
        
        
        self.vbox_exit = QVBoxLayout()

        self.vbox_exit.addLayout(self.hbox_bean)
        self.vbox_exit.addLayout(self.grid_beans)
        self.tab_beans.setLayout(self.vbox_exit)
        
        
    
        self.grid_bills = QGridLayout()
        for ix in range(12):
            self.Bills.append(self.createBill())    
            self.grid_bills.addWidget(self.Bills[ix],int(ix/4),int(ix%4))
        self.vbox_bill.addLayout(self.grid_bills)
    

        
        # Create second tab
        self.tab_bill.layout = QVBoxLayout(self)
        self.tab_bill.setLayout(self.vbox_bill)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # self.setLayout(self.vbox)
        self.setFont(font)
        self.show()
        
        
    def closeEvent(self, event):
        self.Pots2Tex()
        self.Bills2Tex()

    def amountchange(self,):
        self.PotsAmount.setText('{:5d}'.format(int(self.getAmount())))
        #print(self.getAmount())




# %%


# #%%add_to App
def createBill(self):
    groupBox = QGroupBox("RoastBeans")


    def valuechange(self):
        if Ramount.value() >0:
            groupBox.setStyleSheet("""
                   QGroupBox 
                   { 
                       background-color: rgb(235, 255,255); 
                   }
                   """
            )
        else:
            groupBox.setStyleSheet("""
                   QGroupBox 
                   { 
                       background-color: rgb(255, 255,255); 
                   }
                   """
            )
#                       border:0.5px solid rgb(255, 170, 255); 

#     radio1 = QRadioButton("Whole")
#     radio2 = QRadioButton("Drip")
#     radio3 = QRadioButton("Raw")
#     radio1.setChecked(True)

    PotName = QComboBox(self)
    PotName.addItem('')
    for cof in self.CoffeeList[-40:]:
        PotName.addItem(cof)
    PotName.addItem('濾掛福袋x5')
    PotName.setStyleSheet("QComboBox { combobox-popup: 0; }");
    PotName.setMaxVisibleItems(30)
    #PotName.setFont(QFont("Century Gothic", 12, QFont.Normal))
    PotName.setObjectName('PotName')
    PotName.setFont(QFont("Microsoft JhengHei", 12, QFont.Normal))
    PotName.setFixedWidth(250)
    
    PotName_h = QHBoxLayout()
    PotName_ = QLabel('Product')
    #PotName_.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    PotName_h.addWidget(PotName_)
    PotName_h.addWidget(PotName)
    #     vbox_1.addWidget(radio1)
#     vbox_1.addWidget(radio2)
    



    Ramount_Roasted = QComboBox(self)
    Ramount_Roasted.addItem('')
    for d in ['1/2','1/3','1/4','1/6','1/8','1/10','1/12']:
        Ramount_Roasted.addItem(d)
    Ramount_Roasted.setObjectName('Ramount_Roasted')
    
    Ramount_Roasted_h = QHBoxLayout()
    Ramount_Roasted_ = QLabel('Pot')
    #Ramount_Roasted_.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    Ramount_Roasted_h.addWidget(Ramount_Roasted_)
    Ramount_Roasted_h.addWidget(Ramount_Roasted)
    
    
    
    
    Ramount_Raw = QComboBox(self)
    Ramount_Raw.addItem('')
    for d in ['1000g','750g','500g','375g','250g','125g']:
        Ramount_Raw.addItem(d)
    Ramount_Raw.setObjectName('Ramount_Raw')
    
    Ramount_Raw_h = QHBoxLayout()
    Ramount_Raw_ = QLabel('Raw')
    #Ramount_Raw_.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    Ramount_Raw_h.addWidget(Ramount_Raw_)
    Ramount_Raw_h.addWidget(Ramount_Raw)
    
    
    Ramount_Drip = QComboBox(self)
    Ramount_Drip.addItem('')
    for d in range(1,26):
        Ramount_Drip.addItem(str(d))
    Ramount_Drip.setObjectName('Ramount_Drip')
        
    Ramount_Drip_h = QHBoxLayout()
    Ramount_Drip_ = QLabel('Drip')
    #Ramount_Drip_.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    Ramount_Drip_h.addWidget(Ramount_Drip_)
    Ramount_Drip_h.addWidget(Ramount_Drip)


    vbox = QVBoxLayout()
    
    hbox = QHBoxLayout()
#     vbox_1.addWidget(radio1)
#     vbox_1.addWidget(radio2)
#     vbox_1.addWidget(radio3)
    vbox.addLayout(PotName_h)
    vbox.addStretch(1)
    vbox.addLayout(Ramount_Roasted_h)
    vbox.addStretch(1)
    vbox.addLayout(Ramount_Drip_h)
    vbox.addStretch(1)
    vbox.addLayout(Ramount_Raw_h)

#     vbox_2.addWidget(Rdate)
#     #vbox_2.addStretch(1)
#     vbox_2.addWidget(RoastD)
#     #vbox_2.addStretch(1)
#     vbox_2.addWidget(Ramount)

    groupBox.setLayout(vbox)

    return groupBox

#App.createPot = classmethod(createPot)
setattr(App, "createBill", createBill)

# %%


# #%%add_to App
def createPot(self):
    groupBox = QGroupBox("RoastBeans")


    def valuechange(self):
        if Ramount.value() >0:
            groupBox.setStyleSheet("""
                   QGroupBox 
                   { 
                       background-color: rgb(235, 255,255); 
                   }
                   """
            )
        else:
            groupBox.setStyleSheet("""
                   QGroupBox 
                   { 
                       background-color: rgb(255, 255,255); 
                   }
                   """
            )
#                       border:0.5px solid rgb(255, 170, 255); 

    radio1 = QRadioButton("Whole")
    radio2 = QRadioButton("Drip")
    radio3 = QRadioButton("Raw")
    radio1.setChecked(True)

    PotName = QComboBox(self)
    PotName.addItem('')
    for cof in self.CoffeeList[-40:]:
        PotName.addItem(cof)
    PotName.setStyleSheet("QComboBox { combobox-popup: 0; }");
    PotName.setMaxVisibleItems(30)
    PotName.setFont(QFont("Microsoft JhengHei", 12, QFont.Normal))
    PotName.setObjectName('PotName')
    PotName.setFixedWidth(250)

    

    Rdate = QDateEdit(self)
    Rdate.setDateTime(QDateTime.currentDateTime().addDays(-1))
    Rdate.setCalendarPopup(True)
    Rdate.setObjectName('Rdate')

    RoastD = QComboBox(self)
    RoastD.addItem('')
    RoastD.setFont(QFont("Microsoft JhengHei", 12, QFont.Normal))
    for d in ['淺焙','中淺焙','中焙略淺','中焙','中焙略深','中深焙']:
        RoastD.addItem(d)
    RoastD.setObjectName('RoastD')
        
    
    Ramount = QSpinBox(self)
    Ramount.setRange(0, 30)
    Ramount.setSingleStep(1)
    Ramount.setWrapping(True)
    Ramount.setValue(0)
    Ramount.valueChanged.connect(valuechange)
    Ramount.valueChanged.connect(self.amountchange)
    Ramount.setObjectName('Ramount')

    vbox_1 = QVBoxLayout()
    vbox_2 = QVBoxLayout()
    hbox = QHBoxLayout()
    vbox_1.addWidget(radio1)
    vbox_1.addWidget(radio2)
    vbox_1.addWidget(radio3)

    vbox_2.addWidget(PotName)
    #vbox_2.addStretch(1)
    vbox_2.addWidget(Rdate)
    #vbox_2.addStretch(1)
    vbox_2.addWidget(RoastD)
    #vbox_2.addStretch(1)
    vbox_2.addWidget(Ramount)



    hbox.addLayout(vbox_1)
    hbox.addStretch(0)
    hbox.addLayout(vbox_2)

    groupBox.setLayout(hbox)
#    groupBox.setFixedWidth(450)

    return groupBox

#App.createPot = classmethod(createPot)
setattr(App, "createPot", createPot)


# %%


def Close(self,):
    self.close()
    QApplication.quit()

setattr(App, "Close", Close)





def getAmount(self,):
    amount = 0.0
    for p in self.Pots:
        if p.findChildren(QRadioButton)[1].isChecked():
            amount += 0.5 * p.findChildren(QSpinBox)[0].value()
        else:
            amount += p.findChildren(QSpinBox)[0].value()
    return amount

setattr(App, "getAmount", getAmount)


def GetInfo(self, p):

    c_type = 0 if p.findChildren(QRadioButton)[0].isChecked(
    ) else 1 if p.findChildren(QRadioButton)[1].isChecked() else 2
    c_name = p.findChildren(QComboBox,'PotName')[0].currentText()
    c_roast = p.findChildren(QComboBox,'RoastD')[0].currentText()
    c_daysto = QDateTime.currentDateTime().date().daysTo(
        p.findChildren(QDateEdit,'Rdate')[0].date())
    c_amount = p.findChildren(QSpinBox,'Ramount')[0].value()
    return [c_type, c_name, c_roast, c_daysto, c_amount]

setattr(App, "GetInfo", GetInfo)



# %%




def MergeInfo_Full(self, p_list):
    with open(FullInfo, 'r',encoding='utf8') as InfoFile:
        Info=InfoFile.read()

    Idx = self.CoffeeList.index(p_list[0])  if p_list[0] in self.CoffeeList else 0
    
    #Name
    Info = Info.replace('%Name%',self.FullCoffeeList[Idx][7] +'\\large '+ self.FullCoffeeList[Idx][8]) 
    #Product1
    insert = '\\quad ' if len(self.FullCoffeeList[Idx][9]) < 8 else ''
    temp =  '\hspace*{'+str(float( 9 - len(self.FullCoffeeList[Idx][9]))/10)+'em} ' +insert+  self.FullCoffeeList[Idx][9]
    
    temp = temp + '\\quad' if len(self.FullCoffeeList[Idx][9]) < 5 else temp
    
    Info = Info.replace('%Product1%',temp)
    
    #Product2
    temp =  self.FullCoffeeList[Idx][10].strip(' ')+', '+self.FullCoffeeList[Idx][12]+' ' +self.FullCoffeeList[Idx][13] #Location英文

        
    if len(temp) >=35:
        Info = Info.replace('-0.05em%P2%','0.20em%P2%') 
        Info = Info.replace('0.11em%P2%','0.30em%P2%')
        temp = '\\footnotesize ' + temp
    elif len(temp) >=30:
        Info = Info.replace('-0.05em%P2%','0.15em%P2%') 
        Info = Info.replace('0.11em%P2%','0.25em%P2%')
        temp = ' \\small ' +  temp
    elif len(temp) >=25:
        temp = temp.split(', ')[0] + ' \\small ' + temp.split(', ')[1] 
    Info = Info.replace('%Product2%',temp)
    
    #Date
    Info = Info.replace('%date%',str(p_list[2]))
    
    
    #print(p_list)
    #Feed Roast
    if p_list[1] == '中深焙':
        Info = Info.replace('%Roast%',' \\small ' + p_list[1])
        Info = Info.replace('0%Feed%',str(3))
    elif p_list[1] == '中焙略深':
        Info = Info.replace('%Roast%',' \\footnotesize '+ p_list[1])
        Info = Info.replace('0%Feed%',str(3))
    elif p_list[1] == '中焙':
        Info = Info.replace('%Roast%',p_list[1])
        Info = Info.replace('0%Feed%',str(4))     
    elif p_list[1] == '中焙略淺':
        Info = Info.replace('%Roast%',' \\footnotesize '+ p_list[1])
        Info = Info.replace('0%Feed%',str(5))
    elif p_list[1] == '中淺焙':
        Info = Info.replace('%Roast%',' \\small ' + p_list[1])
        Info = Info.replace('0%Feed%',str(5)) 
    elif p_list[1] == '淺焙':
        Info = Info.replace('%Roast%',p_list[1])
        Info = Info.replace('0%Feed%',str(6)) 
    
    #Taste
    Info = Info.replace('%Taste%','\\\\\\tiny 風味參考: \\scriptsize ' + self.FullCoffeeList[Idx][14]) 
    
    return Info

setattr(App, "MergeInfo_Full", MergeInfo_Full)


# %%




def MergeInfo_Drip(self, p_list):
    with open(DripInfo, 'r',encoding='utf8') as InfoFile:
        Info=InfoFile.read()
    Idx = self.CoffeeList.index(p_list[0])
    #Name
    Info = Info.replace('0%Product%%',self.FullCoffeeList[Idx][7] +' '+ self.FullCoffeeList[Idx][9] + ' \\small '+ self.FullCoffeeList[Idx][11]) 

    
    #Date
    Info = Info.replace('0%Offset%%',str(p_list[2]+60))

    #Roast
    Info = Info.replace('%Roast%%',p_list[1])
    #Taste
    Info = Info.replace('%Flavor%%', self.FullCoffeeList[Idx][14]) 
    
    return Info

setattr(App, "MergeInfo_Drip", MergeInfo_Drip)

def MergeInfo_Raw(self, p_list):
    with open(RawInfo, 'r',encoding='utf8') as InfoFile:
        Info=InfoFile.read()
    Idx = self.CoffeeList.index(p_list[0])
    #Source
    Info = Info.replace('0%Source%%',self.FullCoffeeList[Idx][0] + ' '+self.FullCoffeeList[Idx][1]) 

    #Price
    Info = Info.replace('0%Price%%',str(int(self.FullCoffeeList[Idx][2])-7)) 

    
    #Product
    Info = Info.replace('0%Product1%%',self.FullCoffeeList[Idx][7] +' '+ self.FullCoffeeList[Idx][9]+' '+ self.FullCoffeeList[Idx][11]+' '+ self.FullCoffeeList[Idx][13]) 
    Info = Info.replace('0%Product2%%',self.FullCoffeeList[Idx][10]+' '+ self.FullCoffeeList[Idx][12]+' '+ self.FullCoffeeList[Idx][13]) 
    

    #Taste
    Info = Info.replace('%Flavor%%', self.FullCoffeeList[Idx][14]) 
    
    return Info

setattr(App, "MergeInfo_Raw", MergeInfo_Raw)


# %%



def Pots2Tex(self,):
    global getit
    getit = self.Pots.copy()

    Infos = []
    InfosD = []
    OnlyDrip=1
    
    Pots_list =[]
    
    for p in self.Pots:
        if p.findChildren(QSpinBox)[0].value() > 0:
            p_list = self.GetInfo(p)
            Pots_list.append(p_list)
            
    for p_list in Pots_list:
        OnlyDrip =  OnlyDrip * p_list[0]
        if p_list[0] == 1:
            for i in range(p_list[-1]):
                Info = self.MergeInfo_Drip(p_list[1:-1])
                InfosD.append(Info)
        if p_list[0] == 2:
            for i in range(p_list[-1]):
                Info = self.MergeInfo_Raw(p_list[1:-1])
                InfosD.append(Info)
    print(len(InfosD))
                
    if len(InfosD)%2 ==1:
        InfosD.append('\\vspace*{3em}')  
    for idx,drip in enumerate(InfosD[::2]):
        Infos.append(InfosD[idx*2]+'\n\\vspace*{0.83em}\\\\%\n'+'%'*20+'\n'+InfosD[idx*2+1])


    for p_list in Pots_list:
    #OnlyDrip =  OnlyDrip * p_list[0]
        if p_list[0] == 0:
            for i in range(p_list[-1]):
                Info = self.MergeInfo_Full(p_list[1:-1])
                Infos.append(Info)    

    with open(PotsTemplate, 'r',encoding='utf8') as TempFile:
        TempInfos=TempFile.read()
    if OnlyDrip >0 :
        with open(DripTemplate, 'r',encoding='utf8') as TempFile:
            TempInfos=TempFile.read()

#    with open(PotsTemplate, 'r',encoding='utf8') as TempFile:
#        TempInfos=TempFile.read()
    for i, info in enumerate(Infos[:21]):
        temp = '%%'+str((int(i/3)+1)*10+i%3+1)+'%%'
        TempInfos = TempInfos.replace(temp,info) 
    with open(PrintLabels, 'w',encoding='utf8') as PrintFile:
        PrintFile.write(TempInfos)   
#             print(p.findChildren(QComboBox)[0].currentText())
    print(self.getAmount())
    self.Close()
    
setattr(App, "Pots2Tex", Pots2Tex)




# %%
def MergeInfo_Bill(self, b):
    
    disc_ = 0.88 if self.disc else 1
    ProductName = b.findChildren(QComboBox,'PotName')[0].currentText()
    Idx = self.CoffeeList.index(ProductName)  if ProductName in self.CoffeeList else 0
    
    amount = b.findChildren(QComboBox,'Ramount_Roasted')[0].currentText()
    if len(amount)>0:
        temp = float(Fraction(amount))
        price = int(self.FullCoffeeList[Idx][5]) * 2 * temp if temp > 1/4 else int(self.FullCoffeeList[Idx][6]) * 4 * temp
        if self.disc:
            print(int(int(ceil(price/5)*5)))
            print(ceil(int(self.FullCoffeeList[Idx][4]) * 4 * temp /5 + 1)*5 )
            return 'Roasted', ProductName, amount+'磅' , int(int(ceil(price/5)*5)), ceil(int(self.FullCoffeeList[Idx][4]) * 4 * temp /5 + 1)*5 
        #return 'Roasted', ProductName, amount+'磅' , int(self.FullCoffeeList[Idx][5]) * 2, int(int(ceil(price/5)*5) * disc_)
        return 'Roasted', ProductName, amount+'磅' , 0, int(int(ceil(price/5)*5) )

        
        
    amount = b.findChildren(QComboBox,'Ramount_Raw')[0].currentText()
    if len(amount)>0:
        temp = int(amount[:-1])/1000.0
        price = int(self.FullCoffeeList[Idx][2]) * temp
        return 'Raw', ProductName, amount ,int(self.FullCoffeeList[Idx][2]),int(price)

    
    amount = b.findChildren(QComboBox,'Ramount_Drip')[0].currentText()
    if len(amount)>0:
        if ProductName == '濾掛福袋x5':
            return 'Roasted', ProductName, 1, int(140 * disc_)
        else:
            temp = int((int(self.FullCoffeeList[Idx][5]) +250)/19)
            price = temp * int(amount)
            return 'Drip', ProductName, int(amount) ,int(temp), int(int(price) * disc_)
    
    return '','',0,0
setattr(App, "MergeInfo_Bill", MergeInfo_Bill)
    
def Bills2Tex(self,):
    Bills_list =[]
    Total = 0
    for b in self.Bills:
        if b.findChildren(QComboBox,'PotName')[0].currentText() != '':
            Bills_list.append(self.MergeInfo_Bill(b)) 
            
    PriceTex = PriceTemplate if self.new_tex.isChecked() else PricePrevious
    with open(PriceTex,'r',encoding='utf8') as TempFile:
        TempPrices=TempFile.read()

            
    with open(PriceInfo, 'r',encoding='utf8') as Info:
        Infos=Info.read()
            
            

    Infos = Infos.replace('@@NAME@@',self.name_text.text())
    Infos = Infos.replace('0%Offset%%',str(QDateTime.currentDateTime().date().daysTo(self.bill_date.date())))
    
    pre_bills = self.pre_bill.value()
    if pre_bills >0:
        Infos = Infos.replace('\large @@TOTAL@@', '餘額  @@TOTAL@@')
        Infos = Infos.replace('%%PreBill%%','\\multicolumn{3}{|c|}{前次餘額}  & '+str(pre_bills) + '\\\\\\hline')
        
    
    ship_bills = self.shiping.value()
    if ship_bills !=0:
        Infos = Infos.replace('%%ShipBill%%','\\multicolumn{3}{|c|}{運費}  & '+str(ship_bills) + '\\\\\\hline')
        Total += ship_bills


    for b in Bills_list:        
        temp = str(b[3]) if b[3]>0 else ' '
        print(b)
        Infos = Infos.replace('%%OneBill%%',  b[1] + ' & '+ temp + ' & '+ str(b[2]) + ' & '+ str(b[4]) + '\\\\\\hline\n' +'%%OneBill%%')
        Total += b[4]
    
    if self.account.isChecked():
        Infos = Infos.replace('%%Account%%','')
        
    if pre_bills !=0:
        Total = pre_bills - Total
    Pre_Color = '\\color{red} ' if Total <0 else ''
    Infos = Infos.replace('@@TOTAL@@',Pre_Color + ' \\$ '+ str(Total))


    TempPrices = TempPrices.replace('%%BillsContents%%',  Infos +'\n\n\\bigskip\\bigskip\n\n'+ '%%BillsContents%%' )
    
    with open(PricePrevious, 'w',encoding='utf8') as PrintFile:
        PrintFile.write(TempPrices)  

    self.Close()
    
setattr(App, "Bills2Tex", Bills2Tex)

# %%


if not QApplication.instance():
    app = QApplication(sys.argv)
else:
    app = QApplication.instance() 
app.setFont(QFont("Century Gothic", 12, QFont.Normal))
app.setApplicationName("wtf")

window = App()
app.exec_()


# %%


# %%



