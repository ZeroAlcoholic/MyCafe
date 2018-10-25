# -*- coding: utf-8 -*-  
import sys, re, string
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import csv
import datetime          # for date count
import codecs
import math

global CoffeeList,DEFAULT_OPTION,DateList,DateNumList


Current = datetime.date.today()
Current -= datetime.timedelta(days=23)
DateList = []
DateNumList = []
DateNumListF = []

for i in range(25):
    Current += datetime.timedelta(days=1)
    DateList.append(str(Current.month)+' / '+str(Current.day))
    DateNumList.append(i+45-22)
    DateNumListF.append(i-22)

    #無論掛耳或熟豆都先用45

Todaystr = str(datetime.date.today().month)+' / '+str(datetime.date.today().day)
#print DateList
#print DateNumList

DEFAULT_OPTION = 'Choose an Option:'
CoffeeList = []
FullCoffeeList = []

with open('../CoffeeBeans.csv', 'r',encoding="utf-8") as csvfile:
    Listing = csv.reader(csvfile, delimiter=',', quotechar='|')
    global DEFAULTVALUE_OPTION
    for row in Listing:
        if len(row)>8:
            if row[7] == '衣索比亞 耶加雪啡':
                row[7] = '耶加雪啡'
#                row[8] = 'Yirgacheffe'
                
            FullCoffeeList.append(row)
    #        temp = (row[3]+' '+row[5]+' '+row[9]).strip('   ')
            temp = (row[7]+' '+row[9]).strip('   ')
            CoffeeList.append(temp)
        #printtemp

FullCoffeeList=FullCoffeeList[-42:]
CoffeeList = CoffeeList[-42:]
CoffeeList[0]= DEFAULT_OPTION
#CoffeeList = tuple([DEFAULT_OPTION]+CoffeeList[1:])
#tuple(CoffeeList)


class Demo(Frame):
   def __init__(self, master):
      Frame.__init__(self, master, relief=RAISED, bd=2)
      l = Label(self, text=self.label, font=('Helvetica', 6, 'italic bold'),
              background='dark slate blue', foreground='white')
      l.pack(side=TOP, expand=NO, fill=BOTH, padx=1, pady=1, ipadx=1, ipady=1)

class ReliefDemo(Demo):
   label = 'Relief types: Label widgets with 2d/3d borders'
   def __init__(self, master):
      Demo.__init__(self, master)
      for relief in [RAISED, SUNKEN, RIDGE, GROOVE, FLAT, SOLID]:
         l = Label(self, text=relief, relief=relief, bd=4)
         l.pack(side=LEFT, expand=YES, fill=BOTH,
               padx=4, pady=1, ipadx=4, ipady=1)

class OptionCoffee1(Demo):
   label = 'Select Coffee 01:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC1, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='RawBean: ').pack(side=LEFT)
      op = OptionMenu(f, app.RawBeanR1, '250','333.3', '500', '666.6', '750', '1000','1333.3','1500','2000')
      Label(f, text=' g').pack(side=RIGHT)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roasted: ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastedR1, '1/10', '1/6','1/4', '1/3', '1/2' )
      Label(f, text=' 磅').pack(side=RIGHT)
      op.pack()
      f.pack()


      
      f = Frame(self)
      Label(f, text='Drip Amount:').pack(side=LEFT)
      op = OptionMenu(f, app.DripD1, *range(30))
      #op1 = OptionMenu(f, app.AmountA1_2, *range(10))
      op.pack(side=LEFT)
      #op1.pack(side=RIGHT)
      f.pack()


class OptionCoffee2(Demo):
   label = 'Select Coffee 01:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC2, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='RawBean: ').pack(side=LEFT)
      op = OptionMenu(f, app.RawBeanR2, '250','333.3', '500', '666.6', '750', '1000','1333.3','1500','2000')
      Label(f, text=' g').pack(side=RIGHT)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roasted: ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastedR2, '1/10', '1/6','1/4', '1/3', '1/2' )
      Label(f, text=' 磅').pack(side=RIGHT)
      op.pack()
      f.pack()


      
      f = Frame(self)
      Label(f, text='Drip Amount:').pack(side=LEFT)
      op = OptionMenu(f, app.DripD2, *range(30))
      #op1 = OptionMenu(f, app.AmountA1_2, *range(10))
      op.pack(side=LEFT)
      #op1.pack(side=RIGHT)
      f.pack()

class OptionCoffee3(Demo):
   label = 'Select Coffee 01:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC3, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='RawBean: ').pack(side=LEFT)
      op = OptionMenu(f, app.RawBeanR3, '250','333.3', '500', '666.6', '750','1000','1333.3','1500','2000')
      Label(f, text=' g').pack(side=RIGHT)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roasted: ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastedR3, '1/10', '1/6','1/4', '1/3', '1/2' )
      Label(f, text=' 磅').pack(side=RIGHT)
      op.pack()
      f.pack()


      
      f = Frame(self)
      Label(f, text='Drip Amount:').pack(side=LEFT)
      op = OptionMenu(f, app.DripD3, *range(30))
      #op1 = OptionMenu(f, app.AmountA1_2, *range(10))
      op.pack(side=LEFT)
      #op1.pack(side=RIGHT)
      f.pack()


class OptionCoffee4(Demo):
   label = 'Select Coffee 01:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC4, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='RawBean: ').pack(side=LEFT)
      op = OptionMenu(f, app.RawBeanR4, '250','333.3', '500', '666.6', '750','1000','1333.3','1500','2000')
      Label(f, text=' g').pack(side=RIGHT)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roasted: ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastedR4,'1/10', '1/6','1/4', '1/3', '1/2' )
      Label(f, text=' 磅').pack(side=RIGHT)
      op.pack()
      f.pack()


      
      f = Frame(self)
      Label(f, text='Drip Amount:').pack(side=LEFT)
      op = OptionMenu(f, app.DripD4, *range(30))
      #op1 = OptionMenu(f, app.AmountA1_2, *range(10))
      op.pack(side=LEFT)
      #op1.pack(side=RIGHT)
      f.pack()



class OptionCoffee5(Demo):
   label = 'Select Coffee 05:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC5, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='RawBean: ').pack(side=LEFT)
      op = OptionMenu(f, app.RawBeanR5, '250','333.3', '500', '666.6', '750', '1000','1333.3','1500','2000')
      Label(f, text=' g').pack(side=RIGHT)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roasted: ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastedR5, '1/10', '1/6','1/4', '1/3', '1/2' )
      Label(f, text=' 磅').pack(side=RIGHT)
      op.pack()
      f.pack()


      
      f = Frame(self)
      Label(f, text='Drip Amount:').pack(side=LEFT)
      op = OptionMenu(f, app.DripD5, *range(30))
      #op1 = OptionMenu(f, app.AmountA1_2, *range(10))
      op.pack(side=LEFT)
      #op1.pack(side=RIGHT)
      f.pack()


class OptionCoffee6(Demo):
   label = 'Select Coffee 01:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC6, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='RawBean: ').pack(side=LEFT)
      op = OptionMenu(f, app.RawBeanR6, '250','333.3', '500', '666.6', '750', '1000','1333.3','1500','2000')
      Label(f, text=' g').pack(side=RIGHT)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roasted: ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastedR6, '1/10', '1/6','1/4', '1/3', '1/2' )
      Label(f, text=' 磅').pack(side=RIGHT)
      op.pack()
      f.pack()


      
      f = Frame(self)
      Label(f, text='Drip Amount:').pack(side=LEFT)
      op = OptionMenu(f, app.DripD6, *range(30))
      #op1 = OptionMenu(f, app.AmountA1_2, *range(10))
      op.pack(side=LEFT)
      #op1.pack(side=RIGHT)
      f.pack()


class TextName(Demo):
   label = 'Name:'
   def __init__(self, master):
      Demo.__init__(self, master)
      
      f = Frame(self)
      op = Checkbutton(f, text="Discount", variable=app.Discount)
      op.pack()
      f.pack(side=LEFT)

      f = Frame(self)
      Label(f, text='Name').pack(side=LEFT)
      op = Entry(f,textvariable=app.Name,bd =1)
      op.pack()
      f.pack()
      


	  



class OptionDemo2(Demo):
   label = 'OptionMenu2:'
   def __init__(self, master):
      Demo.__init__(self, master)

      f = Frame(self)
      Label(f, text='Justify').pack(side=LEFT)
      op = OptionMenu(f, app.justifyVar2, 'left', 'center', 'right')
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Fit to').pack(side=LEFT)
      op = OptionMenu(f, app.sizeVar2, 'minimum', 'maximum')
      op.pack()
      f.pack()

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Fit to').pack(side=LEFT)
      op = OptionMenu(f, app.Testing2, *temp)
      op.pack()
      f.pack()


class CanvasDemo(Demo):
   label = 'Canvas widget with simple animation:'
   def __init__(self, master):
      Demo.__init__(self, master)
      self.canvas = Canvas(self, relief=SUNKEN, bd=2, background='gray65',
                      width=100, height=100)
      self.canvas.pack(side=TOP, expand=YES, fill=BOTH)
      self.arc = self.canvas.create_arc(0,0, 1,1)

      self.start, self.extent = 90,0

   def configure(self, event=None):
      fillColor = ''
      if app.fillVar.get(): fillColor = app.colorVar.get()

      outlineColor = ''
      if app.outlineVar.get(): outlineColor = 'black'
      
      self.canvas.itemconfigure(self.arc, style=app.styleVar.get())
      self.canvas.itemconfigure(self.arc, fill=fillColor)
      self.canvas.itemconfigure(self.arc, outline=outlineColor)
      
   def animate(self):
      w,h = self.canvas.winfo_width(), self.canvas.winfo_height()

      if app.sizeVar2.get() == 'minimum':
         s = min(w,h)
      else:
         s = max(w,h)

      if app.justifyVar2.get() == 'left':
         x0,x1 = 10, s-10
      elif app.justifyVar2.get() == 'center':
         x0,x1 = (w-s+20)/2, (w+s-20)/2
      else:
         x0,x1 = w-s+10, w-10

      y0, y1 = (h-s+20)/2, (h+s-20)/2

      self.canvas.coords(self.arc, x0,y0, x1,y1)
      self.start  = self.start  - app.animateSpeed1.get()
      self.extent = self.extent - app.animateSpeed2.get()
      self.canvas.itemconfigure(self.arc,start=self.start,extent=self.extent)
      root.after(10, self.animate)

# A small collection (about 16%) of the colors found in the usual X11 color
# data base:  .../lib/X11/rgb.txt

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
        'old lace', 'linen', 'antique white', 'papaya whip',
        'blanched almond', 'bisque', 'peach puff', 'navajo white',
        'moccasin', 'cornsilk', 'ivory', 'lemon chiffon', 'seashell',
        'honeydew', 'mint cream', 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'white', 'black', 'dark slate gray',
        'dark slate grey', 'dim gray', 'dim grey', 'slate gray',
        'slate grey', 'light slate gray', 'light slate grey', 'gray',
        'grey', 'light grey', 'light gray', 'midnight blue', 'navy',
        'navy blue', 'cornflower blue', 'dark slate blue', 'slate blue',
        'medium slate blue', 'light slate blue', 'medium blue',
        'royal blue', 'blue', 'dodger blue', 'deep sky blue', 'sky blue',
        'light sky blue', 'steel blue', 'light steel blue', 'light blue',
        'powder blue', 'pale turquoise', 'dark turquoise',
        'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue',
        'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green',
        'light sea green', 'pale green', 'spring green', 'lawn green',
        'green', 'chartreuse', 'medium spring green', 'green yellow',
        'lime green', 'yellow green', 'forest green', 'olive drab',
        'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod',
        'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown',
        'sienna', 'peru', 'burlywood', 'beige', 'wheat', 'sandy brown',
        'tan', 'chocolate', 'firebrick', 'brown', 'dark salmon', 'salmon',
        'light salmon', 'orange', 'dark orange', 'coral', 'light coral',
        'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink',
        'light pink', 'pale violet red', 'maroon', 'medium violet red',
        'violet red', 'magenta', 'violet', 'plum', 'orchid',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet',
        'purple', 'medium purple', 'thistle', 'dark grey', 'dark gray',
        'dark blue', 'dark cyan', 'dark magenta', 'dark red', 'light green']

#COLORS.sort(lambda a,b: cmp(string.split(a)[-1], string.split(b)[-1]))

class ListboxDemo(Demo):
   label = 'Listbox, Entry, Button,\nand Scrollbar widgets:'
   def __init__(self, master):
      Demo.__init__(self, master)

      e = Entry(self, textvariable=app.colorVar)
      e.pack(side=TOP, fill=X)
      e.bind('<Return>', self.enterColor)
      
      b = Button(self, text='Select color', command=self.selectColor)
      b.pack(side=BOTTOM, fill=X)
      
      self.colorList = Listbox(self, height=6)
      self.colorList.pack(side=LEFT, expand=YES, fill=BOTH)
#      for color in COLORS:
#         self.colorList.insert(AtEnd(), color)
      self.colorList.selection_set(COLORS.index(app.colorVar.get()))

      scrollbar = Scrollbar(self)
      self.colorList.configure(yscrollcommand=(scrollbar, 'set'))
      scrollbar.configure(command=(self.colorList, 'yview'))
      scrollbar.pack(side=LEFT, fill=Y)

      self.colorList.bind("<Double-Button-1>", self.selectColor)

   def enterColor(self, event=None):
      app.canvasDemo.configure()

   def selectColor(self, event=None):
      colorIndex = map(string.atoi, app.listDemo.colorList.curselection())
      if not colorIndex: return
      app.colorVar.set(app.listDemo.colorList.get(colorIndex[0]))
      app.canvasDemo.configure()

def Char(c): return '0.0+%d char' % c
def Options(**kw): return kw

class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError( "cannot use pack with this widget")
    def place(self, **kw):
        raise TclError( "cannot use place with this widget")
		
class TextDemo(Demo):
   label = 'Text widget displaying source with cheap syntax highlighting:\n'+\
         '(Move mouse over text and watch indent-structure highlighting.)'
   font = ('Courier', 10, 'normal')
   bold = ('Courier', 10, 'bold')
   Highlights = {'#.*': Options(foreground='red'),
              r'\'.*?\'': Options(foreground='yellow'),
              r'\bdef\b\s.*:':Options(foreground='blue', spacing1=2),
              r'\bclass\b\s.*\n':Options(background='pink', spacing1=5),
              r'\b(class|def|for|in|import|from|break|continue)\b':
               Options(font=bold)
              }
   
   def __init__(self, master):
      Demo.__init__(self, master)
      self.text = ScrolledText(self, width=80, height=20,
                         font=self.font, background='gray65',
                         spacing1=1, spacing2=1, tabs='24')
      self.text.pack(side=TOP, expand=YES, fill=BOTH)

      content = open(sys.argv[0], 'r').read()
      self.text.insert(AtEnd(), content)

      reg = re.compile('([\t ]*).*\n')
      pos = 0
      indentTags = []
      while 1:
         match = reg.search(content, pos)
         if not match: break
         indent = match.end(1)-match.start(1)
         if match.end(0)-match.start(0) == 1:
            indent = len(indentTags)
         tagb = 'Tagb%08d' % match.start(0)
         tagc = 'Tage%08d' % match.start(0)
         self.text.tag_configure(tagc, background='', relief=FLAT, borderwidth=2)
         self.text.tag_add(tagb, Char( match.start(0)), Char(match.end(0)))
         self.text.tag_bind(tagb, '<Enter>',
                        lambda e,self=self,tagc=tagc: self.Enter(tagc))
         self.text.tag_bind(tagb, '<Leave>',
                        lambda e,self=self,tagc=tagc: self.Leave(tagc))
         del indentTags[indent:]
         indentTags.extend( (indent-len(indentTags))*[None] )
         indentTags.append(tagc)
         for tag in indentTags:
            if tag:
               self.text.tag_add(tag, Char(match.start(0)),
                             Char(match.end(0)))
         pos = match.end(0)

      for key,kw in self.Highlights.items():
         self.text.tag_configure(key, cnf=kw)
         reg = re.compile(key)
         pos = 0
         while 1:
            match = reg.search(content, pos)
            if not match: break
            self.text.tag_add(key, Char(match.start(0)),Char(match.end(0)))
            pos = match.end(0)

   def Enter(self, tag):
      self.text.tag_raise(tag)
      self.text.tag_configure(tag, background='gray80', relief=RAISED)

   def Leave(self, tag):
      self.text.tag_configure(tag, background='', relief=FLAT)

MessageText = '''All the controls in this block control some aspect of the animation in the Canvas widget.  Most should be self explanitory.  To choose the fill color, do one of (a) type a color name into the Entry widget and RETURN, (b) select a color in the Listbox and hit "Select color" Button, or (c) double-click a color in the Listbox.'''

class MessageDemo(Demo):
   label = 'Message widget:'
   def __init__(self, master):
      Demo.__init__(self, master)
      self.message =  Message(self, text=MessageText)
      self.message.pack(side=TOP, expand=YES, fill=BOTH)
      self.message.bind('<Configure>', self.redoAspectRatio)
   def redoAspectRatio(self, event=None):
      w,h = self.message.winfo_width(), self.message.winfo_height()
      self.message.configure(aspect=(100*w)/h)

class RadiobuttonDemo(Demo):
   label = 'Radiobutton:'
   def __init__(self, master):
      Demo.__init__(self, master)
      self.count = IntVar()
      self.count.set(1)
      Radiobutton(self, text='Pie Slice',
               variable=app.styleVar, value='pieslice',
               command=app.canvasDemo.configure).pack(anchor=W)
      Radiobutton(self, text='Chord',
               variable=app.styleVar, value='chord',
               command=app.canvasDemo.configure).pack(anchor=W)
      Radiobutton(self, text='Arc only',
               variable=app.styleVar, value='arc',
               command=app.canvasDemo.configure).pack(anchor=W)

			   
class RadiobuttonAccount(Demo):
   label = 'Continuous Selection:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Add Account',
               variable=app.AccountVar, value='2',
               command=app.canvasDemo.configure).pack(anchor=W)
      Radiobutton(self, text='No Account',
               variable=app.AccountVar, value='1',
               command=app.canvasDemo.configure).pack(anchor=W)			   
			   
class RadiobuttonNewTable(Demo):
   label = 'Continuous Selection:'
   #label = ' '
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Create New File',
               variable=app.ContVar, value='2',
               command=app.canvasDemo.configure).pack(anchor=W)
      Radiobutton(self, text='Continue Previous File',
               variable=app.ContVar, value='1',
               command=app.canvasDemo.configure).pack(anchor=W)


class RadiobuttonCoffee1(Demo):
   label = 'CoffeeType1:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='RoastedBeans',
          variable=app.TypeVar1, value='1').pack(anchor=W)
      Radiobutton(self, text='RawBeans',
          variable=app.TypeVar1, value='2').pack(anchor=W)
      Radiobutton(self, text='DripCoffee',
          variable=app.TypeVar1, value='3').pack(anchor=W)


class RadiobuttonCoffee2(Demo):
   label = 'CoffeeType2:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='RoastedBeans',
          variable=app.TypeVar2, value='1').pack(anchor=W)
      Radiobutton(self, text='RawBeans',
          variable=app.TypeVar2, value='2').pack(anchor=W)
      Radiobutton(self, text='DripCoffee',
          variable=app.TypeVar2, value='3').pack(anchor=W)


class RadiobuttonCoffee3(Demo):
   label = 'CoffeeType3:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='RoastedBeans',
          variable=app.TypeVar3, value='1').pack(anchor=W)
      Radiobutton(self, text='RawBeans',
          variable=app.TypeVar3, value='2').pack(anchor=W)
      Radiobutton(self, text='DripCoffee',
          variable=app.TypeVar3, value='3').pack(anchor=W)


class RadiobuttonCoffee4(Demo):
   label = 'CoffeeType4:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='RoastedBeans',
          variable=app.TypeVar4, value='1').pack(anchor=W)
      Radiobutton(self, text='RawBeans',
          variable=app.TypeVar4, value='2').pack(anchor=W)
      Radiobutton(self, text='DripCoffee',
          variable=app.TypeVar4, value='3').pack(anchor=W)


class RadiobuttonCoffee5(Demo):
   label = 'CoffeeType5:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='RoastedBeans',
          variable=app.TypeVar5, value='1').pack(anchor=W)
      Radiobutton(self, text='RawBeans',
          variable=app.TypeVar5, value='2').pack(anchor=W)
      Radiobutton(self, text='DripCoffee',
          variable=app.TypeVar5, value='3').pack(anchor=W)


class RadiobuttonCoffee6(Demo):
   label = 'CoffeeType6:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='RoastedBeans',
          variable=app.TypeVar6, value='1').pack(anchor=W)
      Radiobutton(self, text='RawBeans',
          variable=app.TypeVar6, value='2').pack(anchor=W)
      Radiobutton(self, text='DripCoffee',
          variable=app.TypeVar6, value='3').pack(anchor=W)

class TextTransport(Demo):
   label = 'Transport:'
   def __init__(self, master):
      Demo.__init__(self, master)

      f = Frame(self)
      Label(f, text='運費:').pack(side=LEFT)

      op = Entry(f,textvariable=app.Transport,bd =5)
      
      op.pack()
      f.pack()

class TextRemainder(Demo):
   label = 'Remainder:'
   def __init__(self, master):
      Demo.__init__(self, master)

      f = Frame(self)
      Label(f, text='前次餘額:').pack(side=LEFT)

      op = Entry(f,textvariable=app.Remainder,bd =5)
      
      op.pack()
      f.pack()      
		  

class CheckbuttonDemo(Demo):
   label = 'Checkbutton:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Checkbutton(self, text='Fill', variable=app.fillVar,
               command=app.canvasDemo.configure).pack(anchor=W)
      Checkbutton(self, text='Outline', variable=app.outlineVar,
               command=app.canvasDemo.configure).pack(anchor=W)

class ScaleDemo(Demo):
   label = 'Scale:\n(animation speed)'
   def __init__(self, master):
      Demo.__init__(self, master)
      s1 = Scale(self, from_=-6.0, to=6.0,
               resolution=0.1,
               label='Start angle increment:',
               orient=HORIZONTAL,
               variable=app.animateSpeed1)
      s1.pack(side=TOP, expand=YES, fill=X)
      s2 = Scale(self, from_=-6.0, to=6.0,
               resolution=0.1,
               label='Extent angle increment:',
               orient=HORIZONTAL,
               variable=app.animateSpeed2)
      s2.pack(side=TOP, expand=YES, fill=X)

class MenubarDemo:

   def __init__(self, master):
      # Create the menu widgets, and register with their parents.
      menubar = Menu(root)
      master.config(menu=menubar)
   
      controlmenu = Menu(menubar)
      menubar.add_cascade(label='Controls', menu=controlmenu)
      
      radiomenu = Menu(menubar)
      controlmenu.add_cascade(label='Radiobutton menu', menu=radiomenu)
   
      checkmenu = Menu(menubar)
      controlmenu.add_cascade(label='Checkbutton menu', menu=checkmenu)
   
      # Add the command(s) to the menu(s)
      controlmenu.add_command(label='Exit', foreground='red',
                        command=menubar.quit)

      radiomenu.add_radiobutton(label='Pie Slice', command=self.notify,
                          variable=app.styleVar, value='pieslice')
      radiomenu.add_radiobutton(label='Chord', command=self.notify,
                          variable=app.styleVar, value='chord')
      radiomenu.add_radiobutton(label='Arc only', command=self.notify,
                          variable=app.styleVar, value='arc')

      checkmenu.add_checkbutton(label='Fill', command=self.notify,
                          variable=app.fillVar, onvalue=1, offvalue=0)
      checkmenu.add_checkbutton(label='Outline', command=self.notify,
                          variable=app.outlineVar,onvalue=1,offvalue=0)
         
                       
   def notify(self):
      app.canvasDemo.configure()

                     
   

class Application:
   def __init__(self):
      root.title('Pricing Beans Bills v20180514')
      self.styleVar = StringVar();      self.styleVar.set('pieslice')
      self.fillVar = BooleanVar();      self.fillVar.set(1)
      self.outlineVar = BooleanVar();      self.outlineVar.set(1)
      self.animateSpeed1 = DoubleVar();   self.animateSpeed1.set(1.0)
      self.animateSpeed2 = DoubleVar();   self.animateSpeed2.set(1.0)
      self.colorVar = StringVar();      self.colorVar.set('aquamarine')
      
      self.Discount = BooleanVar(); self.Discount.set(0)
      self.Name = StringVar(); self.Name.set(' ')
      self.ContVar = IntVar(); self.ContVar.set('1')
      self.AccountVar = IntVar(); self.AccountVar.set('1')
      self.Transport = IntVar(); self.Transport.set(0)
      self.Remainder = IntVar(); self.Remainder.set(0)

	  
      self.TypeVar1 = IntVar();  self.TypeVar1.set('1')
#---------------------------------------Coffee 01------------------------------------------
      self.CoffeeC1 = StringVar();      self.CoffeeC1.set(DEFAULT_OPTION)
      self.RawBeanR1 = StringVar();         self.RawBeanR1.set('1000')
      self.DripD1 = IntVar();      self.DripD1.set(0)
      self.RoastedR1 = StringVar();    self.RoastedR1.set('1/2');
     
      

      self.TypeVar2 = IntVar();  self.TypeVar2.set('1')
#---------------------------------------Coffee 02------------------------------------------
      self.CoffeeC2 = StringVar();      self.CoffeeC2.set(DEFAULT_OPTION)
      self.RawBeanR2 = StringVar();         self.RawBeanR2.set('1000')
      self.DripD2 = IntVar();      self.DripD2.set(0)
      self.RoastedR2 = StringVar();    self.RoastedR2.set('1/2');

	  
      self.TypeVar3 = IntVar();  self.TypeVar3.set('1')
#---------------------------------------Coffee 03------------------------------------------
      self.CoffeeC3 = StringVar();      self.CoffeeC3.set(DEFAULT_OPTION)
      self.RawBeanR3 = StringVar();         self.RawBeanR3.set('1000')
      self.DripD3 = IntVar();      self.DripD3.set(0)
      self.RoastedR3 = StringVar();    self.RoastedR3.set('1/2');
     
      

      self.TypeVar4 = IntVar();  self.TypeVar4.set('1')
#---------------------------------------Coffee 04------------------------------------------
      self.CoffeeC4 = StringVar();      self.CoffeeC4.set(DEFAULT_OPTION)
      self.RawBeanR4 = StringVar();         self.RawBeanR4.set('1000')
      self.DripD4 = IntVar();      self.DripD4.set(0)
      self.RoastedR4 = StringVar();    self.RoastedR4.set('1/2');

      self.TypeVar5 = IntVar();  self.TypeVar5.set('1')
#---------------------------------------Coffee 05------------------------------------------
      self.CoffeeC5 = StringVar();      self.CoffeeC5.set(DEFAULT_OPTION)
      self.RawBeanR5 = StringVar();         self.RawBeanR5.set('1000')
      self.DripD5 = IntVar();      self.DripD5.set(0)
      self.RoastedR5 = StringVar();    self.RoastedR5.set('1/2');
     
      

      self.TypeVar6 = IntVar();  self.TypeVar6.set('1')
#---------------------------------------Coffee 06------------------------------------------
      self.CoffeeC6 = StringVar();      self.CoffeeC6.set(DEFAULT_OPTION)
      self.RawBeanR6 = StringVar();         self.RawBeanR6.set('1000')
      self.DripD6 = IntVar();      self.DripD6.set(0)
      self.RoastedR6 = StringVar();    self.RoastedR6.set('1/2');


      
      self.justifyVar2 = StringVar();      self.justifyVar2.set('center')
      self.sizeVar2 = StringVar();         self.sizeVar2.set('minimum')
      self.Testing2 = StringVar();      self.Testing2.set(DEFAULT_OPTION)
   
      
   def Go(self):
      MenubarDemo(root)
      self.reliefDemo = ReliefDemo(root)
      #self.messageDemo = MessageDemo(root)
      self.canvasDemo = CanvasDemo(root)

      #self.vscrollbar = AutoScrollbar(root)
      #self.vscrollbar.grid(row=0, column=1, sticky=N+S)
        
	  
      self.TextName = TextName(root)
      self.NewTable = RadiobuttonNewTable(root)
      self.Account = RadiobuttonAccount(root)
#---------------------------------------------------------
      self.CoffeeType1 =  RadiobuttonCoffee1(root)
      self.CoffeeType2 =  RadiobuttonCoffee2(root)
      self.CoffeeType3 =  RadiobuttonCoffee3(root)
      self.CoffeeType4 =  RadiobuttonCoffee4(root)
      self.CoffeeType5 =  RadiobuttonCoffee5(root)
      self.CoffeeType6 =  RadiobuttonCoffee6(root)
      
      self.optionCoffee1 = OptionCoffee1(root)
      self.optionCoffee2 = OptionCoffee2(root)
      self.optionCoffee3 = OptionCoffee3(root)
      self.optionCoffee4 = OptionCoffee4(root)
      self.optionCoffee5 = OptionCoffee5(root)
      self.optionCoffee6 = OptionCoffee6(root)
      self.TextTransport = TextTransport(root)
      self.TextRemainder = TextRemainder(root)

      self.optionDemo2 = OptionDemo2(root)
      self.listDemo = ListboxDemo(root)
      self.radioDemo = RadiobuttonDemo(root)
      self.checkDemo = CheckbuttonDemo(root)
      #self.scaleDemo = ScaleDemo(root)
      #self.textDemo = TextDemo(root)

      

      

      self.PackAll(
      [   [[self.NewTable,self.TextName]],
          [[self.CoffeeType1,self.optionCoffee1,self.CoffeeType2,self.optionCoffee2]],
          [[self.CoffeeType3,self.optionCoffee3,self.CoffeeType4,self.optionCoffee4]],
          [[self.CoffeeType5,self.optionCoffee5,self.CoffeeType6,self.optionCoffee6]],
	  [[self.Account,self.TextTransport,self.TextRemainder]]              
      ])
#      [[self.reliefDemo]],
#          [[self.messageDemo,self.listDemo,self.scaleDemo],
#          [self.canvasDemo,self.radioDemo,self.checkDemo,self.optionDemo]],
#         [[self.textDemo]]



      self.canvasDemo.configure()
      self.canvasDemo.animate()
   

      
      root.mainloop()

   def PackAll(self, batches):
      for batch in batches:
         b = Frame(root, bd=5, relief=GROOVE,bg='ivory')
         for row in batch:
            f = Frame(b)
            for widget in row:
               widget.pack(in_=f, side=LEFT, expand=YES, fill=BOTH)
               widget.tkraise()
            f.pack(side=TOP, expand=YES, fill=BOTH)
         b.pack(side=TOP, expand=YES, fill=BOTH)
       # 


root = Tk()










if __name__ == '__main__':
    app = Application()
    app.Go()
	
    TheName = app.Name.get()
    Discount = app.Discount.get()
    Cont = app.ContVar.get()
    Account = app.AccountVar.get()
    Transport = app.Transport.get()
    Remainder = app.Remainder.get()
#----------------------------------------------------------------
    TypeT1 = app.TypeVar1.get()
    CoffeeC1 =  app.CoffeeC1.get()
    RawBeanR1 =  app.RawBeanR1.get()
    DripD1 = app.DripD1.get()
    RoastedR1 = app.RoastedR1.get()

        

    TypeT2 = app.TypeVar2.get()
    CoffeeC2 =  app.CoffeeC2.get()
    RawBeanR2 =  app.RawBeanR2.get()
    DripD2 = app.DripD2.get()
    RoastedR2 = app.RoastedR2.get()

#----------------------------------------------------------------
    TypeT3 = app.TypeVar3.get()
    CoffeeC3 =  app.CoffeeC3.get()
    RawBeanR3 =  app.RawBeanR3.get()
    DripD3 = app.DripD3.get()
    RoastedR3 = app.RoastedR3.get()

        

    TypeT4 = app.TypeVar4.get()
    CoffeeC4 =  app.CoffeeC4.get()
    RawBeanR4 =  app.RawBeanR4.get()
    DripD4 = app.DripD4.get()
    RoastedR4 = app.RoastedR4.get()
#----------------------------------------------------------------
    TypeT5 = app.TypeVar5.get()
    CoffeeC5 =  app.CoffeeC5.get()
    RawBeanR5 =  app.RawBeanR5.get()
    DripD5 = app.DripD5.get()
    RoastedR5 = app.RoastedR5.get()

        

    TypeT6 = app.TypeVar6.get()
    CoffeeC6 =  app.CoffeeC6.get()
    RawBeanR6 =  app.RawBeanR6.get()
    DripD6 = app.DripD6.get()
    RoastedR6 = app.RoastedR6.get()

    

#print TypeT1

fileType2 = codecs.open("OneTable.tex", "r", "utf-8")
linesType2 = fileType2.readlines()
fileType2.close()
#
if Cont == 2:
    fileorig = codecs.open("Price_template.tex", "r", "utf-8")
else:
    fileorig = codecs.open("BeanPrices.tex", "r", "utf-8")
lines = fileorig.readlines()
fileorig.close()
#for line in lines:
#    if line[0] == '%' and line == '%%%%%Name%%%%%\n':
#        print line



filew = codecs.open("BeanPrices.tex", "w", "utf-8")
#filew.write(codecs.BOM_UTF8)
#####file = codecs.open("FlashCard.tex", "w", "utf-8")
#####fp = codecs.open(fileName, "r", "utf-8")


#Convert unused lines to %

#linesType2
#list.insert(i, x)
#要逆序處理，否則會亂行


print(linesType2)


TotalPrice = 0
#6
TempString = ''
if CoffeeC6 != DEFAULT_OPTION:
    Tidx = CoffeeList.index(CoffeeC6 )
    if TypeT6 == 2:  #Rawbean
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) * float(RawBeanR6)/1000))
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+str(int(FullCoffeeList[Tidx][2])-2)+'+2/KG'+' & '+(RawBeanR6)+'g'+' & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT6 == 3:  #Drip
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) + 225)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 265)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 250)/19.25)
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 245)/18.5)
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(TempPrice) +' & '+str(DripD6)+' & '+str(TempPrice*DripD6) + '\\\\ \hline')
            TotalPrice += TempPrice*DripD6
    elif TypeT6 == 1 and Discount == False:  #Roasted
            if RoastedR6 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR6 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR6 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR6 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR6 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ ' ' +' & '+str(RoastedR6)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT6 == 1 and Discount == True:
            if RoastedR6 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][4])+10
                    OrigPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR6 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*4/15)*5+10
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR6 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])/5) +5
            elif RoastedR6 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][4])*2+10
                    OrigPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR6 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/15)*5+5
                    OrigPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(OrigPrice) +' & '+str(RoastedR6)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice    

    linesType2.insert(3,TempString+'\n')

#5
TempString = ''
if CoffeeC5 != DEFAULT_OPTION:
    Tidx = CoffeeList.index(CoffeeC5 )
    if TypeT5 == 2:  #Rawbean
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) * float(RawBeanR5)/1000))
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+str(int(FullCoffeeList[Tidx][2])-2)+'+2/KG'+' & '+(RawBeanR5)+'g'+' & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT5 == 3:  #Drip
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) + 225)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 265)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 250)/19.25)
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 245)/18.5)
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(TempPrice) +' & '+str(DripD5)+' & '+str(TempPrice*DripD5) + '\\\\ \hline')
            TotalPrice += TempPrice*DripD5
    elif TypeT5 == 1 and Discount == False:  #Roasted
            if RoastedR5 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR5 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR5 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR5 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR5 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ ' ' +' & '+str(RoastedR5)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT5 == 1 and Discount == True:
            if RoastedR5 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][4])+10
                    OrigPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR5 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*4/15)*5+10
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR5 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/5) +5
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR5 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][4])*2+10
                    OrigPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR5 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/15)*5+5
                    OrigPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(OrigPrice) +' & '+str(RoastedR5)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice    

    linesType2.insert(3,TempString+'\n')


#4
TempString = ''
if CoffeeC4 != DEFAULT_OPTION:
    Tidx = CoffeeList.index(CoffeeC4 )
    if TypeT4 == 2:  #Rawbean
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) * float(RawBeanR4)/1000))
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+str(int(FullCoffeeList[Tidx][2])-2)+'+2/KG'+' & '+(RawBeanR4)+'g'+' & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT4 == 3:  #Drip
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) + 225)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 265)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 250)/19.25)
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 245)/18.5)
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(TempPrice) +' & '+str(DripD4)+' & '+str(TempPrice*DripD4) + '\\\\ \hline')
            TotalPrice += TempPrice*DripD4
    elif TypeT4 == 1 and Discount == False:  #Roasted
            if RoastedR4 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR4 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR4 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR4 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR4 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ ' ' +' & '+str(RoastedR4)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT4 == 1 and Discount == True:
            if RoastedR4 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][4])+10
                    OrigPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR4 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*4/15)*5+10
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR4 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/5) +5
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR4 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][4])*2+10
                    OrigPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR4 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/15)*5+5
                    OrigPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(OrigPrice) +' & '+str(RoastedR4)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice    

    linesType2.insert(3,TempString+'\n')

#3
TempString = ''
if CoffeeC3 != DEFAULT_OPTION:
    Tidx = CoffeeList.index(CoffeeC3 )
    if TypeT3 == 2:  #Rawbean
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) * float(RawBeanR3)/1000))
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+str(int(FullCoffeeList[Tidx][2])-2)+'+2/KG'+' & '+(RawBeanR3)+'g'+' & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT3 == 3:  #Drip
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) + 225)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 265)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 250)/19.25)
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 245)/18.5)
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(TempPrice) +' & '+str(DripD3)+' & '+str(TempPrice*DripD3) + '\\\\ \hline')
            TotalPrice += TempPrice*DripD3
    elif TypeT3 == 1 and Discount == False:  #Roasted
            if RoastedR3 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR3 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR3 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR3 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR3 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ ' ' +' & '+str(RoastedR3)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT3 == 1 and Discount == True:
            if RoastedR3 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][4])+10
                    OrigPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR3 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*4/15)*5+10
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR3 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/5) +5
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR3 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][4])*2+10
                    OrigPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR3 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/15)*5+5
                    OrigPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(OrigPrice) +' & '+str(RoastedR3)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice    

    linesType2.insert(3,TempString+'\n')


#2
TempString = ''
if CoffeeC2 != DEFAULT_OPTION:
    Tidx = CoffeeList.index(CoffeeC2 )
    if TypeT2 == 2:  #Rawbean
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) * float(RawBeanR2)/1000))
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+str(int(FullCoffeeList[Tidx][2])-2)+'+2/KG'+' & '+(RawBeanR2)+'g'+' & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT2 == 3:  #Drip
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) + 225)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 265)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 250)/19.25)
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 245)/18.5)
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(TempPrice) +' & '+str(DripD2)+' & '+str(TempPrice*DripD2) + '\\\\ \hline')
            TotalPrice += TempPrice*DripD2
    elif TypeT2 == 1 and Discount == False:  #Roasted
            if RoastedR2 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR2 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR2 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR2 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR2 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ ' ' +' & '+str(RoastedR2)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT2 == 1 and Discount == True:
            if RoastedR2 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][4])+10
                    OrigPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR2 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*4/15)*5+10
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR2 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/5) +5
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR2 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][4])*2+10
                    OrigPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR2 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/15)*5+5
                    OrigPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(OrigPrice) +' & '+str(RoastedR2)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice    

    linesType2.insert(3,TempString+'\n')

#1
TempString = ''
if CoffeeC1 != DEFAULT_OPTION:
    Tidx = CoffeeList.index(CoffeeC1 )
    if TypeT1 == 2:  #Rawbean
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) * float(RawBeanR1)/1000))
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+str(int(FullCoffeeList[Tidx][2])-2)+'+2/KG'+' & '+(RawBeanR1)+'g'+' & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT1 == 3:  #Drip
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][2]) + 225)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 265)/20)
#            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 250)/19.25)
            TempPrice = int(math.ceil(int(FullCoffeeList[Tidx][5]) + 245)/18.5)
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(TempPrice) +' & '+str(DripD1)+' & '+str(TempPrice*DripD1) + '\\\\ \hline')
            TotalPrice += TempPrice*DripD1
    elif TypeT1 == 1 and Discount == False:  #Roasted
            if RoastedR1 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR1 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR1 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR1 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR1 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ ' ' +' & '+str(RoastedR1)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice
    elif TypeT1 == 1 and Discount == True:
            if RoastedR1 == '1/4':
                    TempPrice = int(FullCoffeeList[Tidx][4])+10
                    OrigPrice = int(FullCoffeeList[Tidx][6])
            elif RoastedR1 == '1/3':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*4/15)*5+10
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])*2/15)*5
            elif RoastedR1 == '1/10':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/5)+5 
                    OrigPrice = int(int(FullCoffeeList[Tidx][5])/5) 
            elif RoastedR1 == '1/2':
                    TempPrice = int(FullCoffeeList[Tidx][4])*2+10
                    OrigPrice = int(FullCoffeeList[Tidx][5])
            elif RoastedR1 == '1/6':
                    TempPrice = int(int(FullCoffeeList[Tidx][4])*2/15)*5+5
                    OrigPrice = int(int(FullCoffeeList[Tidx][6])*2/15)*5
            TempString  = (FullCoffeeList[Tidx][7]+' '+FullCoffeeList[Tidx][9]+' & '+ str(OrigPrice) +' & '+str(RoastedR1)+' Lb & '+str(TempPrice) + '\\\\ \hline')
            TotalPrice += TempPrice

    linesType2.insert(3,TempString+'\n')

temp = u'\\multicolumn{3}{|c|}{運費}'


if Transport != 0:
    linesType2.insert(-2,(temp) +' & '+str(Transport)+'\\\\\hline')
    TotalPrice += Transport

temp = u'\\multicolumn{3}{|c|}{前次餘額}'
if Remainder != 0:
    linesType2.insert(2,(temp) +' & '+str(Remainder)+'\\\\\\hline')
    TotalPrice = Remainder -  TotalPrice   
	
if len(TheName) >1:
    TheName
    print(TheName)
    linesType2[1] = linesType2[1].replace('@NAME@',('\\Large '+str(TheName )))

if Remainder == 0:
    linesType2[1] = linesType2[1].replace('@TOTAL@',('\$ \\Large '+str(TotalPrice)))
else:
    linesType2[1] = linesType2[1].replace('@TOTAL@',('\$ \\large 餘額'+str(TotalPrice)))
linesType2[1] = linesType2[1].replace('@DATE@',(' \\large \\today'))

if Account == 2:
	linesType2[-2] = linesType2[-2].strip('%')

for i in linesType2:
	print (i)
	
	









for i in range(len(lines)-5):
    filew.write(lines[i])

for linei in linesType2:
    print(linei)
    filew.write(linei)
	
filew.write('\n\\bigskip\\bigskip\\bigskip')
filew.write('\n')
filew.write('\n')
filew.write('\n')
filew.write('\n')
filew.write('\n')
filew.write('\n')


	
for i in range(len(lines)-5,len(lines)):
    filew.write(lines[i])

	
fileorig.close()
filew.close()

##            filew.write(CheckBox)
##        elif line == '%%%%%1\n':
##            filew.write(TexPrint[0])
##        elif line == '%%%%%2\n':
##            filew.write(TexPrint[1])
##        elif line == '%%%%%3\n':
##            filew.write(TexPrint[2])
##        elif line == '%%%%%4\n':
##            filew.write(TexPrint[3])
##        elif line == '%%%%%5\n':
##            filew.write(TexPrint[4])
##
##    else:
##        filew.write(line)
##fileorig.close()
####
####
####
##filew.close()
####
####
##quit()


