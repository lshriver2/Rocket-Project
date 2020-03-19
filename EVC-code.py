import RPi.GPIO as GPIO
import time
from time import sleep
import picamera
from subprocess import call
import datetime as dt


#import time & nbsp;
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(7, 50)
q = GPIO.PWM(11, 50)

vidLength = int(3)
'''
#run motor fast for sleep
print('motor start')

p.start(0)
q.start(0)
p.ChangeDutyCycle(50)
sleep(3)

#run motor slow during vide
p.ChangeDutyCycle(10)
'''
#update
print("about to take video for ", vidLength)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    
    
    nowTime = dt.datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
    print(nowTime)
    
    
    camera.start_preview()
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.start_recording('Video'+nowTime+'.h264')
#    start = dt.datetime.now()
    
    for i in range(vidLength):
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#        camera.wait_recording(0.2)
        sleep(1)
    camera.stop_recording()
    camera.stop_preview()
   
#update # The camera is now closed.  
print("video taken. ")
print("We are going to convert the video.")

# Define the command we want to execute.
command = "MP4Box -add Video"+nowTime+".h264 ConvertedVideo"+nowTime+".mp4"

# Execute our command
call([command], shell=True)

# Video converted.
print("Video converted.")

p.stop()
q.stop()

print("DONE")
