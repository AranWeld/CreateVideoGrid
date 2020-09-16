filename = '45.mp4'

# Import needed packages
import numpy as np
import cv2

# Open the video file
cap = cv2.VideoCapture(filename)

#time_length =
fps = cap.get(cv2.CAP_PROP_FRAME_COUNT)
#frame_seq =


#cap.set(cv2.CV_CAP_PROP_POS_FRAMES,-1)

print(fps)
