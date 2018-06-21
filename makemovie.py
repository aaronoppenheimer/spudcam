import subprocess

subprocess.call('ffmpeg -i "pix/allpix/pic%05d.jpg" movie/spud.m4v'.split(' '))



