import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)
/*camera.annotate_text = "Time: " + time.strftime("%H:%M:%S")*/

camera.start_preview()
time.sleep(5)
camera.capture('/var/www/raspberry_reactjs/camera/image.jpg')
camera.stop_preview()
