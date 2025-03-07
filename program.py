from multiprocessing.spawn import spawn_main
import tkinter as tk
from tkinter import *
from tkinter import ttk

from setuptools import Command

#Create Intro Menu
start = Tk()
start.title("Climate and Weather Team 20")
start.geometry('500x320')
start.configure(background="darkgrey")

#Creates Headline for Intro
ttk.Label(start, text = "Welcome to Weather + Climate", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 2, column = 5)

#Function for start button
def main ():
    main = Tk()
    main.title("Main Menu")
    main.geometry('500x320')
    main.configure(background="green")
    start.destroy()
    
    #Lable for Main Menu
    ttk.Label(main, text = "Main Menu", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 0)

    #Button1 Option 1
    Button(main,text="Temperature (Degrees F)", width=8, command=op1) .grid(row=8,column=1,sticky=W)

#Button2 Option 2
    Button(main,text="Drew Point (Degrees F)", width=8, command=op2) .grid(row=8,column=2,sticky=W)

#Button3 Option 3
    Button(main,text="Humidity (%)", width=8, command=op3) .grid(row=8,column=3,sticky=W)

    #Button4 Option 4
    Button(main,text="Wind Speed (mph)", width=8, command=op4) .grid(row=8,column=4,sticky=W)

    #Button5 Option 5
    Button(main,text="Pressure (Hg)", width=8, command=op5) .grid(row=8,column=5,sticky=W)
    
    main.mainloop()

#Adding Function for start Button
Button(start,text="Click to start", width=8, command=main) .grid(row=4,column=4,sticky=W)

#Option 1 Function
def op1 ():
    op1 = Tk()
    op1.title("Temperature (Degrees F)")
    op1.geometry('500x320')
    op1.configure(background="blue")

    ttk.Label(op1, text = "Temperature (Degrees F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# label max/average/min 
    ttk.Label(op1, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op1, width = 27, textvariable = n)

# Adding combobox drop down list
    yearchoosen['values'] = (' 2013',
                         ' 2014',
                         ' 2015',
                          ' 2016',
                          ' 2017',
                          ' 2018',
                          ' 2019',
                          ' 2020',
                          ' 2021',)
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

# label month
    ttk.Label(op1, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 6, padx = 10, pady = 25)

# Combobox creation month
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(op1, width = 27, textvariable = n)
  
# Adding combobox drop down list
    monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
    monthchoosen.grid(column = 1, row = 6)
    monthchoosen.current()

# label year
    ttk.Label(op1, text = "Select the  :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op1, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = (' Minimum ', 
                          ' Average ',
                          ' Maximum ')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click ():
     MyLabel=Label(op1, text="Look! I clicked on a Button!!")
     MyLabel.pack

#addbutton 
    Button(op1,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
    Button(op1,text="Quit", width=6, command=op1.destroy) .grid(row=8,column=2,sticky=W)

    op1.mainloop()

    #Option 2 Function
def op2 ():
    op2 = Tk()
    op2.title("Drew Point (Degrees F)")
    op2.geometry('500x320')
    op2.configure(background="white")

    ttk.Label(op2, text = "Drew Point (Degrees F)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 2)

# label max/average/min 
    ttk.Label(op2, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op2, width = 27, textvariable = n)

# Adding combobox drop down list
    yearchoosen['values'] = (' 2013',
                         ' 2014',
                         ' 2015',
                          ' 2016',
                          ' 2017',
                          ' 2018',
                          ' 2019',
                          ' 2020',
                          ' 2021',)
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

# label month
    ttk.Label(op2, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 6, padx = 10, pady = 25)

# Combobox creation month
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(op2, width = 27, textvariable = n)
  
# Adding combobox drop down list
    monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
    monthchoosen.grid(column = 1, row = 6)
    monthchoosen.current()

# label year
    ttk.Label(op2, text = "Select the  :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op2, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = (' Minimum ', 
                          ' Average ',
                          ' Maximum ')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click ():
     MyLabel=Label(op2, text="Look! I clicked on a Button!!")
     MyLabel.pack

#addbutton 
    Button(op2,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
    Button(op2,text="Quit", width=6, command=op2.destroy) .grid(row=8,column=2,sticky=W)
    
    
    op2.mainloop()

#Option 3 Function
def op3 ():
    op3 = Tk()
    op3.title("Humidity (%)")
    op3.geometry('500x320')
    op3.configure(background="yellow")
    

    ttk.Label(op3, text = "Humidity (%)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 3)

# label max/average/min 
    ttk.Label(op3, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op3, width = 27, textvariable = n)

# Adding combobox drop down list
    yearchoosen['values'] = (' 2013',
                         ' 2014',
                         ' 2015',
                          ' 2016',
                          ' 2017',
                          ' 2018',
                          ' 2019',
                          ' 2020',
                          ' 2021',)
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

# label month
    ttk.Label(op3, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 6, padx = 10, pady = 25)

# Combobox creation month
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(op3, width = 27, textvariable = n)
  
# Adding combobox drop down list
    monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
    monthchoosen.grid(column = 1, row = 6)
    monthchoosen.current()

# label year
    ttk.Label(op3, text = "Select the  :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op3, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = (' Minimum ', 
                          ' Average ',
                          ' Maximum ')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click ():
     MyLabel=Label(op3, text="Look! I clicked on a Button!!")
     MyLabel.pack

#addbutton 
    Button(op3,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
    Button(op3,text="Quit", width=6, command=op3.destroy) .grid(row=8,column=2,sticky=W)
    
    op3.mainloop()

    #Option 4 Function
def op4 ():
    op4 = Tk()
    op4.title("Wind Speed (mph)")
    op4.geometry('500x320')
    op4.configure(background="red")

    ttk.Label(op4, text = "Wind Speed (mph)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 4)

# label max/average/min 
    ttk.Label(op4, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op4, width = 27, textvariable = n)

# Adding combobox drop down list
    yearchoosen['values'] = (' 2013',
                         ' 2014',
                         ' 2015',
                          ' 2016',
                          ' 2017',
                          ' 2018',
                          ' 2019',
                          ' 2020',
                          ' 2021',)
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

# label month
    ttk.Label(op4, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 6, padx = 10, pady = 25)

# Combobox creation month
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(op4, width = 27, textvariable = n)
  
# Adding combobox drop down list
    monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
    monthchoosen.grid(column = 1, row = 6)
    monthchoosen.current()

# label year
    ttk.Label(op4, text = "Select the  :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op4, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = (' Minimum ', 
                          ' Average ',
                          ' Maximum ')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click ():
     MyLabel=Label(op4, text="Look! I clicked on a Button!!")
     MyLabel.pack

#addbutton 
    Button(op4,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
    Button(op4,text="Quit", width=6, command=op4.destroy) .grid(row=8,column=2,sticky=W)
    
    op4.mainloop()

    #Option 1 Function
def op5 ():
    op5 = Tk()
    op5.title("Pressure (Hg)")
    op5.geometry('500x320')
    op5.configure(background="black")

    ttk.Label(op5, text = "Pressure (Hg)", 
          background = 'black', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 5)

# label max/average/min 
    ttk.Label(op5, text = "Select the Year :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    yearchoosen = ttk.Combobox(op5, width = 27, textvariable = n)

# Adding combobox drop down list
    yearchoosen['values'] = (' 2013',
                         ' 2014',
                         ' 2015',
                          ' 2016',
                          ' 2017',
                          ' 2018',
                          ' 2019',
                          ' 2020',
                          ' 2021',)
    yearchoosen.grid(column = 1, row = 5)
    yearchoosen.current()

# label month
    ttk.Label(op5, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 6, padx = 10, pady = 25)

# Combobox creation month
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(op5, width = 27, textvariable = n)
  
# Adding combobox drop down list
    monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
    monthchoosen.grid(column = 1, row = 6)
    monthchoosen.current()

# label year
    ttk.Label(op5, text = "Select the  :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 7, padx = 10, pady = 25)  

# Combobox creation
    n = tk.StringVar()
    typevalue = ttk.Combobox(op5, width = 27, textvariable = n)

# Adding combobox drop down list
    typevalue['values'] = (' Minimum ', 
                          ' Average ',
                          ' Maximum ')
    typevalue.grid(column = 1, row = 7)
    typevalue.current()

#Submitbutton function
    def click ():
     MyLabel=Label(op2, text="Look! I clicked on a Button!!")
     MyLabel.pack

#addbutton 
    Button(op5,text="Submit", width=6, command=click) .grid(row=8,column=1,sticky=W)

#add exit button
    Button(op5,text="Quit", width=6, command=op5.destroy) .grid(row=8,column=2,sticky=W)
    
    op5.mainloop()

start.mainloop()




