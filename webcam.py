import cv2
import numpy as np
import urllib.request
import argparse
import pyvirtualcam
from pyvirtualcam import PixelFormat


#class Video:
    
    #def  __init__(self, url, img_width=0, img_height=0):
    #    self.img_width = img_width
    #    self.img_height = img_height
    #    self.url = url

    #def show(self):
    #    while True:
    #        frame = self.download()
    #        self.render(frame)

    #        if cv2.waitKey(1) & 0xFF == ord('|'):
    #            break

    #    cv2.destroyAllWindows()

    #def render(self, frame):
    #    frame = cv2.imdecode(frame, -1)
    #    if self.img_height != 0 and self.img_width != 0:
    #        frame = self.resize(frame)
    #    cv2.imshow('cam', frame)

    #def download(self):
    #    frame = urllib.request.urlopen(self.url)
    #    return np.array(bytearray(frame.read()), dtype=np.uint8)

    #def resize(self, frame):
    #    return cv2.resize(frame, dsize=(self.img_width, self.img_height), interpolation=cv2.INTER_CUBIC)

#class VideoCP:

    #def  __init__(self, url, img_width=0, img_height=0):
    #    self.img_width = img_width
    #    self.img_height = img_height
    #    self.url = url

    #def download(self):
    #    frame = urllib.request.urlopen(self.url)
    #    return np.array(bytearray(frame.read()), dtype=np.uint8)


if __name__ == '__main__':

    # type in your cam ip
    # if you don't want to resize image leave
    # `img_width` and `img_height` at 0
    url = 'http://192.168.0.100:10587/shot.jpg'
    img_width = 1920
    img_height = 1080

    #video = VideoCP(url, img_width, img_height)
    #video = Video(url, img_width, img_height)
    #video.show()

    #parser = argparse.ArgumentParser()
    #parser.add_argument("--camera", type=int, default=0, help="ID of webcam device (default: 0)")
    #parser.add_argument("--fps", action="store_true", help="output fps every second")
    #parser.add_argument("--filter", choices=["shake", "none"], default="shake")
    #args = parser.parse_args()
    args_fps=30

    # Set up webcam capture.
    #vc = cv2.VideoCapture(args.camera)

    #if not vc.isOpened():
    #    raise RuntimeError('Could not open video source')

    pref_width = 1080
    pref_height = 1920
    pref_fps_in = 30
    #vc.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
    #vc.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
    #vc.set(cv2.CAP_PROP_FPS, pref_fps_in)

    # Query final capture device values (may be different from preferred settings).
    #width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
    #height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #fps_in = vc.get(cv2.CAP_PROP_FPS)
    #print(f'Webcam capture started ({width}x{height} @ {fps_in}fps)')

    fps_out = 20

    with pyvirtualcam.Camera(img_width, img_height, fps_out, fmt=PixelFormat.BGR, print_fps=args_fps) as cam:#with pyvirtualcam.Camera(width, height, fps_out, fmt=PixelFormat.BGR, print_fps=args.fps) as cam:
        #print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')
        print('Virtual cam start')

        # Shake two channels horizontally each frame.
        #channels = [[0, 1], [0, 2], [1, 2]]

        while True:
            # Read frame from webcam.
            #ret, frame = vc.read()
            #if not ret:
            #    raise RuntimeError('Error fetching frame')

            #if args.filter == "shake":
            #    dx = 15 - cam.frames_sent % 5
            #    c1, c2 = channels[cam.frames_sent % 3]
            #    frame[:,:-dx,c1] = frame[:,dx:,c1]
            #    frame[:,dx:,c2] = frame[:,:-dx,c2]


            frame = urllib.request.urlopen(url)
            frame_array = np.array(bytearray(frame.read()), dtype=np.uint8)
            cvframe = cv2.imdecode(frame_array, -1)
            
            # Send to virtual cam.
            cam.send(cvframe)

            # Wait until it's time for the next frame.
            cam.sleep_until_next_frame()
