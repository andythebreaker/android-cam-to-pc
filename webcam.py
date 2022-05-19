import cv2
import numpy as np
import urllib.request
import argparse
import pyvirtualcam
from pyvirtualcam import PixelFormat

if __name__ == '__main__':
    
    myrtmp_addr = "rtmp://merry.ee.ncku.edu.tw:51935"
    cap = cv2.VideoCapture(myrtmp_addr)
    err0,frame0 = cap.read()
    frame_tmp=frame0
    
    if err0:
        height, width, chna1 = frame0.shape
        
        args_fps=30

        pref_width = 1080
        pref_height = 1920
        #pref_fps_in = 30

        fps_out = 20

        with pyvirtualcam.Camera(width, height, fps_out, fmt=PixelFormat.BGR, print_fps=args_fps) as cam:#with pyvirtualcam.Camera(width, height, fps_out, fmt=PixelFormat.BGR, print_fps=args.fps) as cam:
            print('Virtual cam start')
            tmp_err=True
            while tmp_err:
                
                err,frame = cap.read()
                tmp_err=err

                if frame:

                    # Send to virtual cam.
                    #cam.send(cvframe)
                    cam.send(frame)
                    frame_tmp=frame

                    # Wait until it's time for the next frame.
                    cam.sleep_until_next_frame()
                else:
                    cam.send(frame_tmp)
                    print("fuckedup")
                    cam.sleep_until_next_frame()