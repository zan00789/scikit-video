from __future__ import print_function
from __future__ import division

from skvideo.io import VideoCapture, VideoWriter
import sys

cap_filename, wr_filename = sys.argv[1], sys.argv[2]

cap = VideoCapture(cap_filename)
cap.open()
print(str(cap.get_info()))

retval, image = cap.read()

wr = VideoWriter(wr_filename, 'H264', 30, (image.shape[1], image.shape[0]))
wr.open()

frame_num = 0

while True:
    retval, image = cap.read()
    if not retval:
        break
    wr.write(image)
    
    print("frame %d" % (frame_num))
    frame_num += 1

wr.release()
cap.release()
print("done")
