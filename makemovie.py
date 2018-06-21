import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", help="frame at which to start (leave out to start from 0)")
parser.add_argument("-f", "--frames", help="frames to include (leave out to use all)")

args = parser.parse_args()

start_opt = ''
if args.start:
	print('starting at {0}'.format(args.start))
	start_opt='-start_number {0}'.format(args.start)

frames_opt = ''
if args.frames:
	print('using {0} frames'.format(args.frames))
	frames_opt='-vframes {0}'.format(args.frames)

command = 'ffmpeg {0} {1} -i pix/allpix/pic%05d.jpg movie/spud.m4v'.format(start_opt, frames_opt)
print('command: {0}'.format(command))
subprocess.call(command.split())
