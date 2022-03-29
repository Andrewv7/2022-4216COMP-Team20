# buttons

btn6 = Button(mai,text="Temperature", width=20, command=TempComp)
    btn6.place(x=350, y=100)

    btn7 = Button(mai,text="Dew Point", width=20, command=DewComp)
    btn7.place(x=350, y=150)

    btn8 = Button(mai,text="Humidity (%)", width=20, command=HumidityComp)
    btn8.place(x=350, y=200)

    btn9 = Button(mai,text="Wind Speed", width=20, command=WindComp)
    btn9.place(x=350, y=250)
    
#function for buttons
def TempComp ():
    TempComp = Tk()
    TempComp.title("Drew Point (Degrees F)")
    TempComp.geometry('500x320')
    TempComp.configure(background="grey")
def DewComp ():
    DewComp = Tk()
    DewComp.title("Drew Point (Degrees F)")
    DewComp.geometry('500x320')
    DewComp.configure(background="grey")
def HumidityComp ():
    HumidityComp = Tk()
    HumidityComp.title("Drew Point (Degrees F)")
    HumidityComp.geometry('500x320')
    HumidityComp.configure(background="grey")
def WindComp ():
    WindComp = Tk()
    WindComp.title("Drew Point (Degrees F)")
    WindComp.geometry('500x320')
    WindComp.configure(background="grey")
    
    #Ploting 2 graps for 2 years
    def makePlot( year_a, year_b, data_type, value_type):

    year_a_data = getYearData(year_a, data_type, value_type)
    year_b_data = getYearData(year_b, data_type, value_type)

    month_labels =['January','February','March','April' ,'May','June','July','August','September','October','November','December']
    plt.figure(figsize=(12,5))

    plt.plot(month_labels,year_a_data, '-ok',color='green',linestyle='dashed',markerfacecolor='green')
    plt.plot(month_labels,year_b_data, '-ok',color='blue',linestyle='dashed',markerfacecolor='blue')
    plt.grid(axis= 'y')
    plt.title(str(year_a) + " - " + str(year_b))
    plt.xlabel('Month')
    plt.ylabel(data_type + " " + value_type)
    plt.show()
