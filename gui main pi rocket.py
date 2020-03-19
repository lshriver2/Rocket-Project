from tkinter import *
import micropython
import time
from time import sleep
import datetime as dt
import board
import busio
import adafruit_mprls
import adafruit_mpl3115a2
i2c = busio.I2C(board.SCL, board.SDA)
root = Tk()

#----adafruit_mprls set up----------------------------------------
# Simplest use, connect to default over I2C
'''
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
for i in range(1):
#    print((mpr.pressure,))
    print('Pressure 2: {0:0.3f} pascals'.format(mpr.pressure))
    time.sleep(1)
'''
#----adafruit_mpl3115a2 set up----------------------------------------
# Simple demo of the MPL3115A2 sensor.
# Will read the pressure and temperature and print them out every second.
# Author: Tony DiCola

# Initialize the I2C bus.
# i2c = busio.I2C(board.SCL, board.SDA)


# Alternatively you can specify a different I2C address for the device:
#sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

# You can configure the pressure at sealevel to get better altitude estimates.
# This value has to be looked up from your local weather forecast or meteorlogical
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:


def mprls():
    global pressure2
    
    # multiply by 100
    mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
    mprIntScale = int(mpr.pressure)
    mprInt = mprIntScale * 100
    pressure2 = 'Pressure2: {0:0.3f} pascals'.format(mprInt)

def mpl3115a2():
    global pressure1
    global altitude
    global temperature
    
    # Initialize the MPL3115A2.
    sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
    sensor.sealevel_pressure = 102600
    
    pressure1 = 'Pressure1: {0:0.3f} pascals'.format(sensor.pressure)
    #print(pressure1)
            
    altitude = 'Altitude: {0:0.3f} meters'.format(sensor.altitude)
    #print(altitude)
            
    temperature = 'Temperature: {0:0.3f} degrees Celsius'.format(sensor.temperature)
    #print(temperature)

def getData():
    mprls()
    mpl3115a2()

def buttonC():
    global pressure2
    global pressure1
    global altitude
    global temperature
    
    mprls()
    mpl3115a2()
    
    print(pressure2 +'    '+ pressure1 +'    '+  altitude +'    '+  temperature)
    '''
    print(pressure1)
    print(altitude)
    print(temperature)
    print('---------')
'''
    

    
def runRun():
    global pressure2
    global pressure1
    global altitude
    global temperature
    loop = int(input("enter number for loop "))
    
    for i in range(loop):
        getData()
        print(pressure2 +'    '+ pressure1 +'    '+  altitude +'    '+  temperature)
        sleep(0.01)

#remove forget
def forget2():
    w1.grid_remove()
    w2.grid_remove()
    w3.grid_remove()
    w4.grid_remove()

getData()

#l = Label(root, text= pressure2)
#l.pack()
'''
w1 = Label(root, text = pressure2, bg="red", fg="white")
w2 = Label(root, text = pressure1, bg="green", fg="black")
w3 = Label(root, text = altitude, bg="blue", fg="white")
w4 = Label(root, text = temperature, bg="brown", fg="white")

w1.pack()
w2.pack()
w3.pack()
w4.pack()

global w1
global w2
global w3
global w4
'''


def remember():
    global w1
    global w2
    global w3
    global w4

    getData()
    w1 = Label(root, text = pressure2, bg="red", fg="white")
    w2 = Label(root, text = pressure1, bg="green", fg="black")
    w3 = Label(root, text = altitude, bg="blue", fg="white")
    w4 = Label(root, text = temperature, bg="brown", fg="white")
#     l.pack()
    w1.pack()
    w2.pack()
    w3.pack()
    w4.pack()

def forget():
    global w1
    global w2
    global w3
    global w4
    
#    l.pack_forget()
    #w1.after(6000, w1.pack_forget())
    w1.pack_forget()
    w2.pack_forget()
    w3.pack_forget()
    w4.pack_forget()
    getData()

def quick():
    remember()
    forget()
    
b = Button(root, text="Forget about it", command=forget)
b.pack()
b2 = Button(root, text="Wait, I still need you", command=remember)
b2.pack()
b3 = Button(root, text="run quick", command= quick)
b3.pack()
button1 = Button(root, text = 'B', command = buttonC)
button1.pack()
    
'''
w1 = Label(root, text = ' ', bg="red", fg="white").grid(row=0,column=0)
w2 = Label(root, text = ' ', bg="green", fg="black").grid(row=1,column=0)
w3 = Label(root, text = ' ', bg="blue", fg="white").grid(row=2,column=0)
w4 = Label(root, text = ' ', bg="brown", fg="white").grid(row=3,column=0)
button1 = Button(root, text = 'B', command = buttonC).grid(row=4,column=0)
button2 = Button(root, text = 'B', command = forget).grid(row=5,column=0)
'''
       
'''
w1 = Label(root, text = pressure2, bg="red", fg="white").grid(row=0,column=0)
w2 = Label(root, text = pressure1, bg="green", fg="black").grid(row=1,column=0)
w3 = Label(root, text = altitude, bg="blue", fg="white").grid(row=2,column=0)
w4 = Label(root, text = temperature, bg="brown", fg="white").grid(row=3,column=0)
button1 = Button(root, text = 'B', command = buttonC).grid(row=4,column=0)
button2 = Button(root, text = 'forget', command = forget).grid(row=5,column=0)
'''
mainloop()

# runRun()

