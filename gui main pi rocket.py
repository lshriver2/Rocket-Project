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

pressure2 = 0
pressure1 = 0
altitude = 0
temperature = 0


# Open function to open the file "MyFile1.txt"  
# (same directory) in append mode and 
file1 = open("MyFile.txt","a")

'''
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
file1 = open("MyFile1.txt","w+") 
file1.close()
'''



def mprls():
    global pressure2
    
    # multiply by 100
    mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
    mprIntScale = int(mpr.pressure)
    mprInt = mprIntScale * 100
    pressure2 = 'Nose Cone Pressure: {0:0.3f} pascals'.format(mprInt)

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
    
    getData()
    
    print(pressure2 +'    '+ pressure1 +'    '+  altitude +'    '+  temperature)

def runRun():
    global pressure2
    global pressure1
    global altitude
    global temperature
#     loop = int(input("enter number for loop "))
    
    telemetryPrint = pressure2 +'    '+ pressure1 +'    '+  altitude +'    '+ temperature +'    '+ dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    getData()
    print(telemetryPrint)
    file1.write(telemetryPrint +"\n")
    

getData()

width = 40
height = 2
font = 1
font = ("Courier", 24)

w1 = Label(root, text = pressure2, bg="tan", fg="black", width = width, height = height, font = font)
w2 = Label(root, text = pressure1, bg="white", fg="black", width = width, height = height, font = font)
w3 = Label(root, text = altitude, bg="tan", fg="black", width = width, height = height, font = font)
w4 = Label(root, text = temperature, bg="white", fg="black", width = width, height = height, font = font)

w1.pack()
w2.pack()
w3.pack()
w4.pack()

def config():
    global w1
    global w2
    global w3
    global w4

    w1.config(text = pressure2)
    w2.config(text = pressure1)
    w3.config(text = altitude)
    w4.config(text = temperature)
    
    w1.pack()
    w2.pack()
    w3.pack()
    w4.pack()

def remember():
    global w1
    global w2
    global w3
    global w4

    getData()
    config()
    
    runRun()
    root.after(100, remember)

def forget():
    global w1
    global w2
    global w3
    global w4
    
    w1.pack_forget()
    w2.pack_forget()
    w3.pack_forget()
    w4.pack_forget()
    getData()

def quick():
    remember()
    #forget()
    remember()
    

frame1 = Frame(root)
frame1.pack()
'''
bforget = Button(frame1, text="Forget", command=forget)
bforget.pack()
bremember2 = Button(frame1, text="Remember", command=remember)
bremember2.pack(side = RIGHT)
brunQuick = Button(frame1, text="Run Quick", command= quick)
brunQuick.pack(side = RIGHT)
buttonC = Button(frame1, text = 'Button C', command = buttonC)
buttonC.pack(side = RIGHT)
'''
buttonQ = Button(frame1, text = 'Quit', command = root.destroy, width = width, font = ("Courier", 16))
buttonQ.pack()
'''
re = 0
if re == 0:
    re = re+1'''
remember()
  
#root.after(100, remember)
mainloop()
file1.close()
print("File Closed")


