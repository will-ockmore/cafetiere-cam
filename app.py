import ffmpy
from datetime import datetime
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)

while True:
    timestamp = datetime.now().strftime('%m-%d_%H:%M')

    outfile_name = '/var/www/html/{}'.format(timestamp)

    old_filename = outfile_name + '.mjpeg'
    new_filename = outfile_name + '.mp4'

    camera.start_recording(old_filename)
    camera.wait_recording(10)
    camera.stop_recording()

    # ff = ffmpy.FFmpeg(
    #     inputs={old_filename: None},
    #     outputs={new_filename: None}
    # )
    # ff.run()
