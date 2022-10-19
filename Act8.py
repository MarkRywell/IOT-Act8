from tkinter import *
from random import randint


window = Tk()
height = 375
width = 375
sh = window.winfo_screenheight()
sw = window.winfo_screenwidth()
x = (sw / 2) - (width / 2)
y = (sh / 2) - (height / 2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.title("Smart Greenhouse App")
window.resizable(0, 0)


#VARIABLES#

Temperature = IntVar()
Humidty = IntVar()
Water = IntVar()

global e_text,value1, value2

Title = Frame(window, bd=4, relief=RAISED, background='#136ff0')
Title.pack(side=TOP, fill=BOTH)
Top = Frame(window, bd=4, relief=RAISED, background='#98ed8a')
Top.pack(side=TOP, fill=X)
Bottom = Frame(window, bd=4, relief=RAISED, background='#98ed8a')
Bottom.pack(side=BOTTOM, fill=X)


e_text = randint(19, 30)
value1 = randint(30, 50)
value2 = randint(2, 15)



def get_temperature():
   
   e_text=temp_value.get()
   Label(Top, text=str(e_text) + " C", font= ('Century 15 bold'), background='#98ed8a').grid(row=0, column=6, padx=5)
   temp_value.delete(0,END)

   
def getHumidity():
   global value1
   value1 = humidity_value.get()
   Label(Top, text=str(value1) + "%" , font= ('Century 15 bold'), background='#98ed8a').grid(row=1, column=6, padx=5)
   humidity_value.delete(0,END)

def get_water():
   global value2
   water_level = value2
   value2 = water_value.get()
   value2= water_level + eval(value2)
   Label(Top, text=str(value2) + " mL", font= ('Century 15 bold'), background='#98ed8a').grid(row=2, column=6, padx=5)
   water_value.delete(0,END)

   

Label(Title, text='SMART GREENHOUSE', font=('Berlin Sans FB Demi', 20, 'bold'), background='#136ff0', fg='white').grid(row=0, column=0, padx=52)

Label(Top, text=str(e_text) + " C", font= ('Century 15 bold'), background='#98ed8a').grid(row=0, column=6, padx=5)

Label(Top, text=str(value1) + " %", font= ('Century 15 bold'), background='#98ed8a').grid(row=1, column=6, padx=5)

Label(Top, text=str(value2) + " mL", font= ('Century 15 bold'), background='#98ed8a').grid(row=2, column=6, padx=5)

Label(Top, text="Temperature", font=('Cooper Black', 13), background='#98ed8a').grid(sticky= W, row=0, column=4, pady=8, padx=3)

Label(Top, text="Humidity", font=('Cooper Black', 13), background='#98ed8a').grid(sticky= W, row=1, column=4, pady=8, padx=3)
Label(Top, text="Soil Moisture", font=('Cooper Black', 13), background='#98ed8a').grid(sticky= W, row=2, column=4, pady=8, padx=3)

Label(Bottom, text="Temperature", font=('Cooper Black', 13), background='#98ed8a').grid(sticky= W, row=0, column=4, pady=8, padx=3)
temp_value = Entry(Bottom, textvariable=Temperature, font=('Arial', 10))

temp_value.grid(row=0, column=6, columnspan=1, padx=10, pady=8)
Button(Bottom, text="SET", font=('times new roman', 15), command=get_temperature, relief=RAISED, bd=5).grid(row=0, column=10, padx=12, pady=8)

Label(Bottom, text="Humidity", font=('Cooper Black', 13), background='#98ed8a').grid(sticky= W, row=1, column=4, pady=8, padx=3)
humidity_value = Entry(Bottom, textvariable=Humidty, font=('Arial', 10))

humidity_value.grid(row=1, column=6, columnspan=1, padx=10, pady=8)
Button(Bottom, text="SET", font=('times new roman', 15), command=getHumidity, relief=RAISED, bd=5).grid(row=1, column=10, padx=12, pady=8)

Label(Bottom, text="Water", font=('Cooper Black', 13), background='#98ed8a').grid(sticky= W, row=2, column=4, pady=8, padx=3)
water_value = Entry(Bottom, textvariable=Water, font=('Arial', 10))
water_value.grid(row=2, column=6, columnspan=1, padx=10, pady=8)
Button(Bottom, text="ADD", font=('times new roman', 14), command=get_water, relief=RAISED, bd=5).grid(row=2, column=10, padx=12, pady=8)



window.mainloop()




