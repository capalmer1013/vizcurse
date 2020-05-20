import cv2
import time
import random

vid = "/home/cpalmer/Downloads/OLD_Balefire_SS1_Lower.mov"

def sleep(start, end, fps):
    t = 1.0/fps
    if t - (end - start) >= 0:
        time.sleep(t-(end - start))

def playVid(fps):
    cap = cv2.VideoCapture(vid)
    try:
        while cap.isOpened():
            startTime = time.time()
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
                
            sleep(startTime, time.time(), fps)
            if cv2.waitKey(1) & 0xff == ord('q'):
                        break
    finally:
        cap.release()
        cv2.destroyAllWindows()

def grainVid(grainSize, fps):
        cap = cv2.VideoCapture(vid)
        #frames = [frame for ret, frame in cap.read()]
        frames = []
        ret, frame = cap.read()
        #while ret:
        for _ in range(1024):
            frames.append(frame)
            ret, frame = cap.read()
        escape = False
        try:
            while True:
                startFrame = random.randint(0, len(frames) - grainSize)
                for i in range(grainSize):
                    startTime = time.time()
                    cv2.imshow('frame', frames[startFrame + i])
                    print(frames[startFrame + i])
                    print(startFrame + i)
                    print("------------------------------------------------------")
                    sleep(startTime, time.time(), fps)
                    if cv2.waitKey(1) & 0xff == ord('q'):
                        escape = True
                        break
                if escape:
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

grainVid(7, 30)
#playVid(30)