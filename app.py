from datetime import datetime
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)

# camera.start_recording('my_video.h264')
# camera.wait_recording(60)
# camera.stop_recording()

while True:
    timestamp = datetime.now().strftime('%m-%d_%H:%M')

    camera.start_recording('/var/www/html/{}.h264'.format(timestamp))
    camera.wait_recording(10)
    camera.stop_recording()
