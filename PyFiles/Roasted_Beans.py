# -*- coding: utf-8 -*-  
import sys, re, string
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import csv
import datetime          # for date count
import codecs


global CoffeeList,DEFAULT_OPTION,DateList,DateNumList


Current = datetime.date.today()
Current -= datetime.timedelta(days=23)
DateList = []
DateNumList = []
DateNumListF = []
 
for i in range(25):
    Current += datetime.timedelta(days=1)
    DateList.append(str(Current.month)+' / '+str(Current.day))
    DateNumList.append(i+70-22)
    DateNumListF.append(i-22)

    #無論掛耳或熟豆都先用60

Todaystr = str(datetime.date.today().month)+' / '+str(datetime.date.today().day)
#print DateList
#print DateNumList

DEFAULT_OPTION = 'Choose an Option:'
CoffeeList = []
FullCoffeeList = []

with open('../CoffeeBeans.csv', 'r',encoding="utf-8") as csvfile:
    Listing = csv.reader(csvfile, delimiter=',', quotechar='|')
    row_count = sum(1 for row in Listing)
    #print row_count

with open('../CoffeeBeans.csv', 'r',encoding="utf-8") as csvfile:
    Listing = csv.reader(csvfile, delimiter=',', quotechar='|')    
    global DEFAULTVALUE_OPTION
    count =0
    for row in Listing:
        #print ', '.join(row)
        count = count +1
        
        if count > row_count -42:
            if row[7] == '衣索比亞 耶加雪啡':
                row[7] = '耶加雪啡'
                row[8] = 'Yirgacheffe'
    #        if row[7] == '衣索比亞 西達摩':
    #            row[7]= '西達摩'
    #            row[8] = 'Sidamo'
            FullCoffeeList.append(row[4:])
    #        temp = (row[3]+' '+row[5]+' '+row[9]).strip('   ')
            temp = (row[7]+' '+row[9]).strip('   ')
            CoffeeList.append(temp)
        #print temp

#print CoffeeList
CoffeeList[0]= DEFAULT_OPTION
#CoffeeList = tuple([DEFAULT_OPTION]+CoffeeList[1:])
#tuple(CoffeeList)



class Demo(Frame):
   def __init__(self, master):
      Frame.__init__(self, master, relief=RAISED, bd=2)
      l = Label(self, text=self.label, font=('Helvetica', 12, 'italic bold'),
              background='dark slate blue', foreground='white')
      l.pack(side=TOP, expand=NO, fill=X)

class ReliefDemo(Demo):
   label = 'Relief types: Label widgets with 2d/3d borders'
   def __init__(self, master):
      Demo.__init__(self, master)
      for relief in [RAISED, SUNKEN, RIDGE, GROOVE, FLAT, SOLID]:
         l = Label(self, text=relief, relief=relief, bd=4)
         l.pack(side=LEFT, expand=YES, fill=BOTH,
               padx=4, pady=4, ipadx=4, ipady=4)

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
      Label(f, text='Roast Degree : ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastR1, '淺焙', '中淺焙', '中焙', '中焙略深','中深焙')
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Date : ').pack(side=LEFT)
      op = OptionMenu(f, app.DateD1, *DateList)
      op.pack()
      f.pack()


      
      f = Frame(self)
      Label(f, text='Amount Number :').pack(side=LEFT)
      op = OptionMenu(f, app.AmountA1, *range(21))
      op.pack()
      f.pack()


class OptionCoffee2(Demo):
   label = 'Select Coffee 02:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC2, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Degree : ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastR2, '淺焙', '中淺焙', '中焙', '中焙略深','中深焙')
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Date : ').pack(side=LEFT)
      op = OptionMenu(f, app.DateD2, *DateList)
      op.pack()
      f.pack()



      f = Frame(self)
      Label(f, text='Amount Number :').pack(side=LEFT)
      op = OptionMenu(f, app.AmountA2, *range(21))
      op.pack()
      f.pack()

class OptionCoffee3(Demo):
   label = 'Select Coffee 03:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC3, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Degree : ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastR3, '淺焙', '中淺焙', '中焙', '中焙略深','中深焙')
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Date : ').pack(side=LEFT)
      op = OptionMenu(f, app.DateD3, *DateList)
      op.pack()
      f.pack()



      f = Frame(self)
      Label(f, text='Amount Number :').pack(side=LEFT)
      op = OptionMenu(f, app.AmountA3, *range(21))
      op.pack()
      f.pack()


class OptionCoffee4(Demo):
   label = 'Select Coffee 04:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC4, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Degree : ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastR4, '淺焙', '中淺焙', '中焙', '中焙略深','中深焙')
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Date : ').pack(side=LEFT)
      op = OptionMenu(f, app.DateD4, *DateList)
      op.pack()
      f.pack()



      f = Frame(self)
      Label(f, text='Amount Number :').pack(side=LEFT)
      op = OptionMenu(f, app.AmountA4, *range(21))
      op.pack()
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
      Label(f, text='Roast Degree : ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastR5, '淺焙', '中淺焙', '中焙', '中焙略深','中深焙')
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Date : ').pack(side=LEFT)
      op = OptionMenu(f, app.DateD5, *DateList)
      op.pack()
      f.pack()



      f = Frame(self)
      Label(f, text='Amount Number :').pack(side=LEFT)
      op = OptionMenu(f, app.AmountA5, *range(21))
      op.pack()
      f.pack()


class OptionCoffee6(Demo):
   label = 'Select Coffee 06:'
   def __init__(self, master):
      Demo.__init__(self, master)

      temp = CoffeeList
      f = Frame(self)
      Label(f, text='Coffee : ').pack(side=LEFT)
      op = OptionMenu(f, app.CoffeeC6, *temp)
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Degree : ').pack(side=LEFT)
      op = OptionMenu(f, app.RoastR6,'淺焙', '中淺焙', '中焙', '中焙略深','中深焙')
      op.pack()
      f.pack()

      f = Frame(self)
      Label(f, text='Roast Date : ').pack(side=LEFT)
      op = OptionMenu(f, app.DateD6, *DateList)
      op.pack()
      f.pack()



      f = Frame(self)
      Label(f, text='Amount Number :').pack(side=LEFT)
      op = OptionMenu(f, app.AmountA6, *range(21))
      op.pack()
      f.pack()



#class OptionDemo2(Demo):
#   label = 'OptionMenu2:'
#   def __init__(self, master):
#      Demo.__init__(self, master)
#
#      f = Frame(self)
#      Label(f, text='Justify').pack(side=LEFT)
#      op = OptionMenu(f, app.justifyVar2, 'left', 'center', 'right')
#      op.pack()
#      f.pack()
#
#      f = Frame(self)
#      Label(f, text='Fit to').pack(side=LEFT)
#      op = OptionMenu(f, app.sizeVar2, 'minimum', 'maximum')
#      op.pack()
#      f.pack()
#
#      temp = CoffeeList
#      f = Frame(self)
#      Label(f, text='Fit to').pack(side=LEFT)
#      op = OptionMenu(f, app.Testing2, *temp)
#      op.pack()
#      f.pack()


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

#class ListboxDemo(Demo):
#   label = 'Listbox, Entry, Button,\nand Scrollbar widgets:'
#   def __init__(self, master):
#      Demo.__init__(self, master)
#
#      e = Entry(self, textvariable=app.colorVar)
#      e.pack(side=TOP, fill=X)
#      e.bind('<Return>', self.enterColor)
#      
#      b = Button(self, text='Select color', command=self.selectColor)
#      b.pack(side=BOTTOM, fill=X)
#      
#      self.colorList = Listbox(self, height=6)
#      self.colorList.pack(side=LEFT, expand=YES, fill=BOTH)
##      for color in COLORS:
##         self.colorList.insert(AtEnd(), color)
#      self.colorList.selection_set(COLORS.index(app.colorVar.get()))
#
#      scrollbar = Scrollbar(self)
#      self.colorList.configure(yscrollcommand=(scrollbar, 'set'))
#      scrollbar.configure(command=(self.colorList, 'yview'))
#      scrollbar.pack(side=LEFT, fill=Y)
#
#      self.colorList.bind("<Double-Button-1>", self.selectColor)
#
#   def enterColor(self, event=None):
#      app.canvasDemo.configure()
#
#   def selectColor(self, event=None):
#      colorIndex = map(string.atoi, app.listDemo.colorList.curselection())
#      if not colorIndex: return
#      app.colorVar.set(app.listDemo.colorList.get(colorIndex[0]))
#      app.canvasDemo.configure()

def Char(c): return '0.0+%d char' % c
def Options(**kw): return kw

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
      #self.text.insert(tkinter.AtEnd(), content)

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

#class MessageDemo(Demo):
#   label = 'Message widget:'
#   def __init__(self, master):
#      Demo.__init__(self, master)
#      self.message =  Message(self, text=MessageText)
#      self.message.pack(side=TOP, expand=YES, fill=BOTH)
#      self.message.bind('<Configure>', self.redoAspectRatio)
#   def redoAspectRatio(self, event=None):
#      w,h = self.message.winfo_width(), self.message.winfo_height()
#      self.message.configure(aspect=(100*w)/h)

#class RadiobuttonDemo(Demo):
#   label = 'Radiobutton:'
#   def __init__(self, master):
#      Demo.__init__(self, master)
#      self.count = IntVar()
#      self.count.set(1)
#      Radiobutton(self, text='Pie Slice',
#               variable=app.styleVar, value='pieslice',
#               command=app.canvasDemo.configure).pack(anchor=W)
#      Radiobutton(self, text='Chord',
#               variable=app.styleVar, value='chord',
#               command=app.canvasDemo.configure).pack(anchor=W)
#      Radiobutton(self, text='Arc only',
#               variable=app.styleVar, value='arc',
#               command=app.canvasDemo.configure).pack(anchor=W)

class RadiobuttonCoffee1(Demo):
   label = 'CoffeeType1:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Full',
               variable=app.TypeVar1, value='2').pack(anchor=W)
      Radiobutton(self, text='Partial',
               variable=app.TypeVar1, value='1').pack(anchor=W)


class RadiobuttonCoffee2(Demo):
   label = 'CoffeeType2:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Full',
               variable=app.TypeVar2, value='2').pack(anchor=W)
      Radiobutton(self, text='Partial',
               variable=app.TypeVar2, value='1').pack(anchor=W)


class RadiobuttonCoffee3(Demo):
   label = 'CoffeeType3:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Full',
               variable=app.TypeVar3, value='2').pack(anchor=W)
      Radiobutton(self, text='Partial',
               variable=app.TypeVar3, value='1').pack(anchor=W)

class RadiobuttonCoffee4(Demo):
   label = 'CoffeeType4:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Full',
               variable=app.TypeVar4, value='2').pack(anchor=W)
      Radiobutton(self, text='Partial',
               variable=app.TypeVar4, value='1').pack(anchor=W)


class RadiobuttonCoffee5(Demo):
   label = 'CoffeeType5:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Full',
               variable=app.TypeVar5, value='2').pack(anchor=W)
      Radiobutton(self, text='Partial',
               variable=app.TypeVar5, value='1').pack(anchor=W)

class RadiobuttonCoffee6(Demo):
   label = 'CoffeeType6:'
   def __init__(self, master):
      Demo.__init__(self, master)
      Radiobutton(self, text='Full',
               variable=app.TypeVar6, value='2').pack(anchor=W)
      Radiobutton(self, text='Partial',
               variable=app.TypeVar6, value='1').pack(anchor=W)



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

#class MenubarDemo:
#
#   def __init__(self, master):
#      # Create the menu widgets, and register with their parents.
#      menubar = Menu(root)
#      master.config(menu=menubar)
#   
#      controlmenu = Menu(menubar)
#      menubar.add_cascade(label='Controls', menu=controlmenu)
#      
#      radiomenu = Menu(menubar)
#      controlmenu.add_cascade(label='Radiobutton menu', menu=radiomenu)
#   
#      checkmenu = Menu(menubar)
#      controlmenu.add_cascade(label='Checkbutton menu', menu=checkmenu)
#   
#      # Add the command(s) to the menu(s)
#      controlmenu.add_command(label='Exit', foreground='red',
#                        command=menubar.quit)
#
#      radiomenu.add_radiobutton(label='Pie Slice', command=self.notify,
#                          variable=app.styleVar, value='pieslice')
#      radiomenu.add_radiobutton(label='Chord', command=self.notify,
#                          variable=app.styleVar, value='chord')
#      radiomenu.add_radiobutton(label='Arc only', command=self.notify,
#                          variable=app.styleVar, value='arc')
#
#      checkmenu.add_checkbutton(label='Fill', command=self.notify,
#                          variable=app.fillVar, onvalue=1, offvalue=0)
#      checkmenu.add_checkbutton(label='Outline', command=self.notify,
#                          variable=app.outlineVar,onvalue=1,offvalue=0)
#         
#                       
#   def notify(self):
#      app.canvasDemo.configure()
#
#                     
   

class Application:
   def __init__(self):
      root.title('Roasted Beans Labels v20180514')
      self.styleVar = StringVar();      self.styleVar.set('pieslice')
      self.fillVar = BooleanVar();      self.fillVar.set(1)
      self.outlineVar = BooleanVar();      self.outlineVar.set(1)
      self.animateSpeed1 = DoubleVar();   self.animateSpeed1.set(1.0)
      self.animateSpeed2 = DoubleVar();   self.animateSpeed2.set(1.0)
      self.colorVar = StringVar();      self.colorVar.set('aquamarine')

      self.TypeVar1 = IntVar();  self.TypeVar1.set('2')
#---------------------------------------Coffee 01------------------------------------------
      self.CoffeeC1 = StringVar();      self.CoffeeC1.set(DEFAULT_OPTION)
      self.RoastR1 = StringVar();         self.RoastR1.set('中焙')
      self.DateD1 = StringVar();      self.DateD1.set(Todaystr)
      self.AmountA1 = IntVar();      self.AmountA1.set(0)


      self.TypeVar2 = IntVar();  self.TypeVar2.set('2')
#---------------------------------------Coffee 02------------------------------------------
      self.CoffeeC2 = StringVar();      self.CoffeeC2.set(DEFAULT_OPTION)
      self.RoastR2 = StringVar();         self.RoastR2.set('中焙')
      self.DateD2 = StringVar();      self.DateD2.set(Todaystr)
      self.AmountA2 = IntVar();      self.AmountA2.set(0)

      self.TypeVar3 = IntVar();  self.TypeVar3.set('2')
#---------------------------------------Coffee 03------------------------------------------
      self.CoffeeC3 = StringVar();      self.CoffeeC3.set(DEFAULT_OPTION)
      self.RoastR3 = StringVar();         self.RoastR3.set('中焙')
      self.DateD3 = StringVar();      self.DateD3.set(Todaystr)
      self.AmountA3 = IntVar();      self.AmountA3.set(0)

      self.TypeVar4 = IntVar();  self.TypeVar4.set('2')
#---------------------------------------Coffee 04------------------------------------------
      self.CoffeeC4 = StringVar();      self.CoffeeC4.set(DEFAULT_OPTION)
      self.RoastR4 = StringVar();         self.RoastR4.set('中焙')
      self.DateD4 = StringVar();      self.DateD4.set(Todaystr)
      self.AmountA4 = IntVar();      self.AmountA4.set(0)

      self.TypeVar5 = IntVar();  self.TypeVar5.set('2')
#---------------------------------------Coffee 05------------------------------------------
      self.CoffeeC5 = StringVar();      self.CoffeeC5.set(DEFAULT_OPTION)
      self.RoastR5 = StringVar();         self.RoastR5.set('中焙')
      self.DateD5 = StringVar();      self.DateD5.set(Todaystr)
      self.AmountA5 = IntVar();      self.AmountA5.set(0)

      self.TypeVar6 = IntVar();  self.TypeVar6.set('2')
#---------------------------------------Coffee 06------------------------------------------
      self.CoffeeC6 = StringVar();      self.CoffeeC6.set(DEFAULT_OPTION)
      self.RoastR6 = StringVar();         self.RoastR6.set('中焙')
      self.DateD6 = StringVar();      self.DateD6.set(Todaystr)
      self.AmountA6 = IntVar();      self.AmountA6.set(0)


      
      self.justifyVar2 = StringVar();      self.justifyVar2.set('center')
      self.sizeVar2 = StringVar();         self.sizeVar2.set('minimum')
      self.Testing2 = StringVar();      self.Testing2.set(DEFAULT_OPTION)
   
      
   def Go(self):
      #MenubarDemo(root)
      self.reliefDemo = ReliefDemo(root)
      #self.messageDemo = MessageDemo(root)
      self.canvasDemo = CanvasDemo(root)
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

      #self.optionDemo2 = OptionDemo2(root)
      #self.listDemo = ListboxDemo(root)
      #self.radioDemo = RadiobuttonDemo(root)
      self.checkDemo = CheckbuttonDemo(root)
      #self.scaleDemo = ScaleDemo(root)
      #self.textDemo = TextDemo(root)

      self.PackAll(
      [
         [[self.CoffeeType1,self.optionCoffee1,self.CoffeeType2,self.optionCoffee2]],
          [[self.CoffeeType3,self.optionCoffee3,self.CoffeeType4,self.optionCoffee4]],
          [[self.CoffeeType5,self.optionCoffee5,self.CoffeeType6,self.optionCoffee6]]
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
         b = Frame(root, bd=12, relief=FLAT,bg='ivory')
         for row in batch:
            f = Frame(b)
            for widget in row:
               widget.pack(in_=f, side=LEFT, expand=YES, fill=BOTH)
               widget.tkraise()
            f.pack(side=TOP, expand=YES, fill=BOTH)
         b.pack(side=TOP, expand=YES, fill=BOTH)
         

root = Tk()



if __name__ == '__main__':
    app = Application()
    app.Go()
#----------------------------------------------------------------
    TypeT1 = app.TypeVar1.get()
    CoffeeC1 =  app.CoffeeC1.get()
    RoastR1 =  app.RoastR1.get()
    temp1 = app.DateD1.get()
    AmountA1 = app.AmountA1.get()
    if temp1 in DateList:
        if TypeT1 == 1:
            DateD1 = DateNumList[DateList.index(app.DateD1.get())]
        else:
            DateD1 = DateNumListF[DateList.index(app.DateD1.get())]
        

    TypeT2 = app.TypeVar2.get()
    CoffeeC2 =  app.CoffeeC2.get()
    RoastR2 =  app.RoastR2.get()
    temp2 = app.DateD2.get()
    AmountA2 = app.AmountA2.get()
    if temp2 in DateList:
        if TypeT2 == 1:
            DateD2 = DateNumList[DateList.index(app.DateD2.get())]
        else:
            DateD2 = DateNumListF[DateList.index(app.DateD2.get())]

#----------------------------------------------------------------
    TypeT3 = app.TypeVar3.get()
    CoffeeC3 =  app.CoffeeC3.get()
    RoastR3 =  app.RoastR3.get()
    temp3 = app.DateD3.get()
    AmountA3 = app.AmountA3.get()
    if temp3 in DateList:
        if TypeT3 == 1:
            DateD3 = DateNumList[DateList.index(app.DateD3.get())]
        else:
            DateD3 = DateNumListF[DateList.index(app.DateD3.get())]

    TypeT4 = app.TypeVar4.get()
    CoffeeC4 =  app.CoffeeC4.get()
    RoastR4 =  app.RoastR4.get()
    temp4 = app.DateD4.get()
    AmountA4 = app.AmountA4.get()
    if temp4 in DateList:
        if TypeT4 == 1:
            DateD4 = DateNumList[DateList.index(app.DateD4.get())]
        else:
            DateD4 = DateNumListF[DateList.index(app.DateD4.get())]

#----------------------------------------------------------------
    TypeT5 = app.TypeVar5.get()
    CoffeeC5 =  app.CoffeeC5.get()
    RoastR5 =  app.RoastR5.get()
    temp5 = app.DateD5.get()
    AmountA5 = app.AmountA5.get()
    if temp5 in DateList:
        if TypeT5 == 1:
            DateD5 = DateNumList[DateList.index(app.DateD5.get())]
        else:
            DateD5 = DateNumListF[DateList.index(app.DateD5.get())]

    TypeT6 = app.TypeVar6.get()
    CoffeeC6 =  app.CoffeeC6.get()
    RoastR6 =  app.RoastR6.get()
    temp6 = app.DateD6.get()
    AmountA6 = app.AmountA6.get()
    if temp6 in DateList:
        if TypeT6 == 1:
            DateD6 = DateNumList[DateList.index(app.DateD6.get())]
        else:
            DateD6 = DateNumListF[DateList.index(app.DateD6.get())]

#print TypeT1
TotalAmount = AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4+AmountA5*TypeT5+AmountA6*TypeT6

#print CoffeeC1,RoastR1,DateD1,AmountA1

TexAll = [(51,65),(66,80),(86,100),(101,115),(121,135),(136,150),
          (156,170),(171,185),(191,205),(206,220),(226,240),(241,255),
          (261,275),(276,290),(296,310),(311,325),(331,345),(346,360),
          (366,380),(381,395),(401,415),(416,430),(436,450),(451,465),
          (471,485),(486,500),(506,520),(521,535),(541,555),(556,570)]#	
TexNames = [54,69,89,104,124,139,159,174,194,209,229,244,264,279,299,314,334,349,369,384,404,419,439,454,474,489,509,524,544,559]
TexDates = [57,72,92,107,127,142,162,177,197,212,232,247,267,282,302,317,337,352,372,387,407,422,442,457,477,492,512,527,547,562]
TexRoasting = [62,77,97,112,132,147,167,182,202,217,237,252,272,287,307,322,342,357,377,392,412,427,447,462,482,497,517,532,552,567]

#filew = open('Testing.tex','w')
#filew.write(codecs.BOM_UTF8)
filew = codecs.open("RoastedBeans.tex", "w", "utf-8")



fileType2 = codecs.open("FullInfo.tex", "r", "utf-8")
linesType2 = fileType2.readlines()
fileType2.close()
#
fileorig = codecs.open("RoastedBeans_template.tex", "r", "utf-8")
lines = fileorig.readlines()
#for line in lines:
#    if line[0] == '%' and line == '%%%%%Name%%%%%\n':
#        print line


#Convert unused lines to %
if TotalAmount%2 == 1:
    TotalAmount+=1
for unused in range(TotalAmount,len(TexAll)):
    for unline in range(TexAll[unused][0],TexAll[unused][1]+1):
        lines[unline-1] = '%%%'+lines[unline-1]
        #####Add odd and even printing config


Raising = [' ',' ',' ','中深焙','中焙', '中淺焙', '淺焙']
#linesType2
#list.insert(i, x)
#要逆序處理，否則會亂行

TEMP = linesType2[:]
print( TypeT6,AmountA6)
if TypeT6 ==2 :
    Tidx = CoffeeList.index(CoffeeC6)
    TEMP[1] = str(FullCoffeeList[Tidx][3]+' ') +TEMP[1]#Country中文
    TEMP[3] = FullCoffeeList[Tidx][4] +TEMP[3]#Country英文
    TEMP[7] = '\hspace*{'+str(float(12-len(str(FullCoffeeList[Tidx][5])))/10)+'em}'+str(FullCoffeeList[Tidx][5])+TEMP[7] #Location中文
    TEMP[10] = FullCoffeeList[Tidx][6].strip(' ')+', '+FullCoffeeList[Tidx][8]+' ' +FullCoffeeList[Tidx][9]+' '+ TEMP[10] #Location英文
    if len(TEMP[10]) >30:
        TEMP[8] = TEMP[8].replace("-0.05","0.15")
        if len(TEMP[10]) >42 :
            TEMP[9] = TEMP[9].replace("\large","\small")
            TEMP[11] = TEMP[11].replace(".11",".35")
        else:    
            TEMP[9] = TEMP[9].replace("\large"," ")
            TEMP[11] = TEMP[11].replace(".11",".25")    
    TEMP[13] =str(DateD6) + TEMP[13]
    if len(RoastR6) > 3:
        TEMP[19] = '4'+TEMP[19]
        #TEMP[22] = '\small '+RoastR5 + TEMP[22]
        TEMP[21] = TEMP[21].replace("normalsize","small")
    else:
        TEMP[19] = str(Raising.index(RoastR6))+TEMP[19]
    TEMP[22] = RoastR6 + TEMP[22]
    TEMP[24] = '\\\\\\scriptsize 風味參考: '+FullCoffeeList[Tidx][10] +TEMP[24]#test flavour


    for using in range(AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4+AmountA5*TypeT5+AmountA6*TypeT6-1,
                       AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4+AmountA5*TypeT5-1, -1):
        for unline in range(TexAll[using][0],TexAll[using][1]+1):
            lines[unline-1] = '%%%'+lines[unline-1]
        #insert
        if using % 2 == 0:
            for it in range(len(TEMP)-1,-1,-1):
                lines.insert(TexAll[using][0],TEMP[it])


else:
    for using in range(AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4+AmountA5*TypeT5,AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4+AmountA5*TypeT5+AmountA6*TypeT6):
        lines[TexNames[using]-1]=str(CoffeeC6) + lines[TexNames[using]-1]
        lines[TexDates[using]-1]=str(DateD6)+lines[TexDates[using]-1]
        lines[TexRoasting[using]-1]=str(RoastR6)+lines[TexRoasting[using]-1]


TEMP = linesType2[:]
print( TypeT5,AmountA5)
if TypeT5 ==2 :
    Tidx = CoffeeList.index(CoffeeC5)
    TEMP[1] = str(FullCoffeeList[Tidx][3]+' ') +TEMP[1]#Country中文
    TEMP[3] = FullCoffeeList[Tidx][4] +TEMP[3]#Country英文
    TEMP[7] = '\hspace*{'+str(float(12-len(str(FullCoffeeList[Tidx][5])))/10)+'em}'+str(FullCoffeeList[Tidx][5])+TEMP[7] #Location中文
    TEMP[10] = FullCoffeeList[Tidx][6].strip(' ')+', '+FullCoffeeList[Tidx][8]+' ' +FullCoffeeList[Tidx][9]+' '+ TEMP[10] #Location英文
    if len(TEMP[10]) >30:
        TEMP[8] = TEMP[8].replace("-0.05","0.15")
        if len(TEMP[10]) >42 :
            TEMP[9] = TEMP[9].replace("\large","\small")
            TEMP[11] = TEMP[11].replace(".11",".35")
        else:    
            TEMP[9] = TEMP[9].replace("\large"," ")
            TEMP[11] = TEMP[11].replace(".11",".25")    
    TEMP[13] =str(DateD5) + TEMP[13]
    if len(RoastR5) > 3:
        TEMP[19] = '4'+TEMP[19]
        #TEMP[22] = '\small '+RoastR5 + TEMP[22]
        TEMP[21] = TEMP[21].replace("normalsize","small")
    else:
        TEMP[19] = str(Raising.index(RoastR5))+TEMP[19]
    TEMP[22] = RoastR5 + TEMP[22]
    TEMP[24] = '\\\\\\scriptsize 風味參考: '+FullCoffeeList[Tidx][10] +TEMP[24]#test flavour

    for using in range(AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4+AmountA5*TypeT5-1,
                       AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4-1, -1):
        for unline in range(TexAll[using][0],TexAll[using][1]+1):
            lines[unline-1] = '%%%'+lines[unline-1]
        #insert
        if using % 2 == 0:
            for it in range(len(TEMP)-1,-1,-1):
                lines.insert(TexAll[using][0],TEMP[it])
else:
    for using in range(AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4,AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4+AmountA5*TypeT5):
        lines[TexNames[using]-1]=str(CoffeeC5) + lines[TexNames[using]-1]
        lines[TexDates[using]-1]=str(DateD5)+lines[TexDates[using]-1]
        lines[TexRoasting[using]-1]=str(RoastR5)+lines[TexRoasting[using]-1]


TEMP = linesType2[:]
#-----------------------------4------------------------------------------------------------------------------------------------------
print( TypeT4,AmountA4)
if TypeT4 ==2 :
    Tidx = CoffeeList.index(CoffeeC4)
    TEMP[1] = str(FullCoffeeList[Tidx][3]+' ') +TEMP[1]#Country中文
    TEMP[3] = FullCoffeeList[Tidx][4] +TEMP[3]#Country英文
    TEMP[7] = '\hspace*{'+str(float(12-len(str(FullCoffeeList[Tidx][5])))/10)+'em}'+str(FullCoffeeList[Tidx][5])+TEMP[7] #Location中文
    TEMP[10] = FullCoffeeList[Tidx][6].strip(' ')+', '+FullCoffeeList[Tidx][8]+' ' +FullCoffeeList[Tidx][9]+' '+ TEMP[10] #Location英文
    if len(TEMP[10]) >30:
        TEMP[8] = TEMP[8].replace("-0.05","0.15")
        if len(TEMP[10]) >42 :
            TEMP[9] = TEMP[9].replace("\large","\small")
            TEMP[11] = TEMP[11].replace(".11",".35")
        else:    
            TEMP[9] = TEMP[9].replace("\large"," ")
            TEMP[11] = TEMP[11].replace(".11",".25")    
    TEMP[13] =str(DateD4) + TEMP[13]
    if len(RoastR4) > 3:
        TEMP[19] = '4'+TEMP[19]
        #TEMP[22] = '\small '+RoastR5 + TEMP[22]
        TEMP[21] = TEMP[21].replace("normalsize","small")
    else:
        TEMP[19] = str(Raising.index(RoastR4))+TEMP[19]
    TEMP[22] = RoastR4 + TEMP[22]
    TEMP[24] = '\\\\\\scriptsize 風味參考: '+FullCoffeeList[Tidx][10] +TEMP[24]#test flavour

    for using in range(AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4-1,
                       AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3-1, -1):
        for unline in range(TexAll[using][0],TexAll[using][1]+1):
            lines[unline-1] = '%%%'+lines[unline-1]
        #insert
        if using % 2 == 0:
            for it in range(len(TEMP)-1,-1,-1):
                lines.insert(TexAll[using][0],TEMP[it])
else:
    for using in range(AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3,AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3+AmountA4*TypeT4):
        lines[TexNames[using]-1]=str(CoffeeC4) + lines[TexNames[using]-1]
        lines[TexDates[using]-1]=str(DateD4)+lines[TexDates[using]-1]
        lines[TexRoasting[using]-1]=str(RoastR4)+lines[TexRoasting[using]-1]


TEMP = linesType2[:]
#------------------------3------------------------------------------------------------------------------------------------------
print( TypeT3,AmountA3)
if TypeT3 ==2:
    Tidx = CoffeeList.index(CoffeeC3)
    TEMP[1] = str(FullCoffeeList[Tidx][3]+' ') +TEMP[1]#Country中文
    TEMP[3] = FullCoffeeList[Tidx][4] +TEMP[3]#Country英文
    TEMP[7] = '\hspace*{'+str(float(12-len(str(FullCoffeeList[Tidx][5])))/10)+'em}'+str(FullCoffeeList[Tidx][5])+TEMP[7] #Location中文
    TEMP[10] = FullCoffeeList[Tidx][6].strip(' ')+', '+FullCoffeeList[Tidx][8]+' ' +FullCoffeeList[Tidx][9]+' '+ TEMP[10] #Location英文
    if len(TEMP[10]) >30:
        TEMP[8] = TEMP[8].replace("-0.05","0.15")
        if len(TEMP[10]) >42 :
            TEMP[9] = TEMP[9].replace("\large","\small")
            TEMP[11] = TEMP[11].replace(".11",".35")
        else:    
            TEMP[9] = TEMP[9].replace("\large"," ")
            TEMP[11] = TEMP[11].replace(".11",".25")    
    TEMP[13] =str(DateD3) + TEMP[13]
    if len(RoastR3) > 3:
        TEMP[19] = '4'+TEMP[19]
        #TEMP[22] = '\small '+RoastR5 + TEMP[22]
        TEMP[21] = TEMP[21].replace("normalsize","small")
    else:
        TEMP[19] = str(Raising.index(RoastR3))+TEMP[19]
    TEMP[22] = RoastR3 + TEMP[22]
    TEMP[24] = '\\\\\\scriptsize 風味參考: '+FullCoffeeList[Tidx][10] +TEMP[24]#test flavour

    for using in range(AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3-1,
                       AmountA1*TypeT1+AmountA2*TypeT2-1, -1):
        for unline in range(TexAll[using][0],TexAll[using][1]+1):
            lines[unline-1] = '%%%'+lines[unline-1]
        #insert
        if using % 2 == 0:
            for it in range(len(TEMP)-1,-1,-1):
                lines.insert(TexAll[using][0],TEMP[it])
else:
    for using in range(AmountA1*TypeT1+AmountA2*TypeT2,AmountA1*TypeT1+AmountA2*TypeT2+AmountA3*TypeT3):
        lines[TexNames[using]-1]=str(CoffeeC3) + lines[TexNames[using]-1]
        lines[TexDates[using]-1]=str(DateD3)+lines[TexDates[using]-1]
        lines[TexRoasting[using]-1]=str(RoastR3)+lines[TexRoasting[using]-1]


TEMP = linesType2[:]
#----------------------------2------------------------------------------------------------------------------------------------------
print( TypeT2,AmountA2)
if TypeT2 ==2:
    Tidx = CoffeeList.index(CoffeeC2)
    TEMP[1] = str(FullCoffeeList[Tidx][3]+' ') +TEMP[1]#Country中文
    TEMP[3] = FullCoffeeList[Tidx][4] +TEMP[3]#Country英文
    TEMP[7] = '\hspace*{'+str(float(12-len(str(FullCoffeeList[Tidx][5])))/10)+'em}'+str(FullCoffeeList[Tidx][5])+TEMP[7] #Location中文
    TEMP[10] = FullCoffeeList[Tidx][6].strip(' ')+', '+FullCoffeeList[Tidx][8]+' ' +FullCoffeeList[Tidx][9]+' '+ TEMP[10] #Location英文
    if len(TEMP[10]) >30:
        TEMP[8] = TEMP[8].replace("-0.05","0.15")
        if len(TEMP[10]) >42 :
            TEMP[9] = TEMP[9].replace("\large","\small")
            TEMP[11] = TEMP[11].replace(".11",".35")
        else:    
            TEMP[9] = TEMP[9].replace("\large"," ")
            TEMP[11] = TEMP[11].replace(".11",".25")    
    TEMP[13] =str(DateD2) + TEMP[13]
    if len(RoastR2) > 3:
        TEMP[19] = '4'+TEMP[19]
        #TEMP[22] = '\small '+RoastR5 + TEMP[22]
        TEMP[21] = TEMP[21].replace("normalsize","small")
    else:
        TEMP[19] = str(Raising.index(RoastR2))+TEMP[19]
    TEMP[22] = RoastR2 + TEMP[22]
    TEMP[24] = '\\\\\\scriptsize 風味參考: '+FullCoffeeList[Tidx][10] +TEMP[24]#test flavour

    for using in range(AmountA1*TypeT1+AmountA2*TypeT2-1,
                       AmountA1*TypeT1-1, -1):
        for unline in range(TexAll[using][0],TexAll[using][1]+1):
            lines[unline-1] = '%%%'+lines[unline-1]
        #insert
        if using % 2 == 0:
            for it in range(len(TEMP)-1,-1,-1):
                lines.insert(TexAll[using][0],TEMP[it])

else:
    for using in range(AmountA1*TypeT1,AmountA1*TypeT1+AmountA2*TypeT2):
        lines[TexNames[using]-1]=str(CoffeeC2) + lines[TexNames[using]-1]
        lines[TexDates[using]-1]=str(DateD2)+lines[TexDates[using]-1]
        lines[TexRoasting[using]-1]=str(RoastR2)+lines[TexRoasting[using]-1]



TEMP = linesType2[:]
#----------------------------1------------------------------------------------------------------------------------------------------
print( TypeT1,AmountA1)
if TypeT1 == 2 :
    Tidx = CoffeeList.index(CoffeeC1)
    TEMP[1] = str(FullCoffeeList[Tidx][3]+' ') +TEMP[1]#Country中文
    TEMP[3] = FullCoffeeList[Tidx][4] +TEMP[3]#Country英文
    TEMP[7] = '\hspace*{'+str(float(12-len(str(FullCoffeeList[Tidx][5])))/10)+'em}'+str(FullCoffeeList[Tidx][5])+TEMP[7] #Location中文
    TEMP[10] = FullCoffeeList[Tidx][6].strip(' ')+', '+FullCoffeeList[Tidx][8]+' ' +FullCoffeeList[Tidx][9]+' '+ TEMP[10] #Location英文
    if len(TEMP[10]) >30:
        TEMP[8] = TEMP[8].replace("-0.05","0.15")
        if len(TEMP[10]) >42 :
            TEMP[9] = TEMP[9].replace("\large","\small")
            TEMP[11] = TEMP[11].replace(".11",".35")
        else:    
            TEMP[9] = TEMP[9].replace("\large"," ")
            TEMP[11] = TEMP[11].replace(".11",".25")       
    TEMP[13] =str(DateD1) + TEMP[13]
    print( RoastR1,len(RoastR1))
    if len(RoastR1) > 3:
        TEMP[19] = '4'+TEMP[19]
        #TEMP[22] = '\small '+RoastR5 + TEMP[22]
        TEMP[21] = TEMP[21].replace("normalsize","small")
    elif len(RoastR1) == 3:
        TEMP[19] = str(Raising.index(RoastR1))+TEMP[19]
        TEMP[22] = RoastR1 + TEMP[22]
        TEMP[23] = TEMP[23].replace("normalsize","small")
    else:
        TEMP[19] = str(Raising.index(RoastR1))+TEMP[19]
        TEMP[22] = RoastR1 + TEMP[22]
    TEMP[24] = '\\\\\\scriptsize 風味參考: '+FullCoffeeList[Tidx][10] +TEMP[24]#test flavour

    for using in range(AmountA1*TypeT1-1, -1, -1):
        for unline in range(TexAll[using][0],TexAll[using][1]+1):
            lines[unline-1] = '%%%'+lines[unline-1]
        #insert
        if using % 2 == 0:
            for it in range(len(TEMP)-1,-1,-1):
                lines.insert(TexAll[using][0],TEMP[it])
else:
    for using in range(AmountA1*TypeT1):
        lines[TexNames[using]-1]=str(CoffeeC1) + lines[TexNames[using]-1]
        lines[TexDates[using]-1]=str(DateD1)+lines[TexDates[using]-1]
        lines[TexRoasting[using]-1]=str(RoastR1)+lines[TexRoasting[using]-1]













for i in range(len(lines)):
    filew.write(lines[i])
    # if i+1 in TexNames:
    #     filew.write(lines[i][:-1]+str(i+1)+'Name'+lines[i][-1:])
    # elif i+1 in TexRoasting:
    #     filew.write(lines[i][:-1]+str(i+1)+'Roasting'+lines[i][-1:])
    # elif i+1 in TexDates:
    #     filew.write(lines[i][:-1]+str(i+1)+'Date'+lines[i][-1:])
    # else:
    #     filew.write(lines[i])

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

