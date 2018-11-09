import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

camera.start_preview()
camera.annotate_background = picamera.Color('blue')
camera.annotate_foreground = picamera.Color('yellow')
camera.annotate_text = "Time: %s" % time.strftime("%H:%M:%S")
camera.annotate_text_size = 50
time.sleep(5)

camera.capture('/var/www/dist/camera/image.jpg')
camera.stop_preview()

camera.close()
