#!/bin/sh
python /home/pi/src/spudcam/series.py
ffmpeg -framerate 25 -i /home/pi/src/spudcam/pix/series%02d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p -y /home/pi/src/spudcam/pix/sunrise.mp4

