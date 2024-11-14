#Attach the camera on the board
#Enabe the Camera : Menu>Preferences>Configuration>Interfaces>enable Camera
#sudo apt-get install python-picamera python3-picamera
#Name of file should not be picamera.py
#Reference for other uses of Picamera - https://picamera.readthedocs.io/en/release-1.13/

from picamera import PiCamera
from time import sleep

camera=PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/img.jpg')
camera.stop_preview()
