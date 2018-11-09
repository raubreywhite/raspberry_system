from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/var/www/raspberry_reactjs/camera/image.jpg')
camera.stop_preview()
