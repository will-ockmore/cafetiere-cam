from datetime import datetime
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)

while True:
    timestamp = datetime.now().strftime('%m-%d_%H:%M')

    outfile_name = '/var/www/html/{}'.format(timestamp)

    old_filename = outfile_name + '.h264'

    camera.start_recording(old_filename)
    camera.wait_recording(60)
    camera.stop_recording()
