import cv2
import numpy as np
import time

video = cv2.VideoCapture("sample.mp4")
time.sleep(2)
while True:
    ret, frame = video.read()
    print(ret)
    if ret == True:
        cv2.imshow("Detector Personas", frame)
        ventana = cv2.waitKey(10)
        if ventana == ord("q"):
            break


video.release()
cv2.destroyAllWindows()