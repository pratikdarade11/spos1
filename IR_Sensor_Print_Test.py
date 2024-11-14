#Raspberry Pi Libraries 
import RPi.GPIO as GPIO #GPIO library
import time #library for sleep

import Adafruit_CharLCD as LCD

#set mode as BCM
GPIO.setmode(GPIO.BCM)

#set pins
IR_OUT = 21
BUZ = 22

#setup pins at output
GPIO.setup(IR_OUT, GPIO.IN)
GPIO.setup(BUZ, GPIO.OUT)

def destroy():
    GPIO.output (BUZ, GPIO.LOW)
    GPIO.cleanup()

if __name__ =='__main__':
    try:
        while True:
            IR_State = GPIO.input(IR_OUT)
            if (IR_State == True):
                print ("OBJECT DETECTED")
                GPIO.output (BUZ, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output (BUZ, GPIO.LOW)
                
            
            else:
               print ("NO OBJECT")
                
    except KeyboardInterrupt:
        destroy()



    