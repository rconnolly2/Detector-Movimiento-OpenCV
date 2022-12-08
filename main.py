import cv2
import numpy as np
import time

video = cv2.VideoCapture("sample.mp4")
frame_diferencia = np.zeros((720, 1280), dtype="uint8")

time.sleep(2)
while True:
    ret, frame = video.read()

    if ret == True:
        ret, frame2 = video.read()
        diferencia = cv2.absdiff(frame, frame2)
        diferencia_gris = cv2.cvtColor(diferencia, cv2.COLOR_RGB2GRAY)
        diferencia_gris_blur = cv2.GaussianBlur(diferencia_gris, (5, 5), 0)
        _, threshold = cv2.threshold(diferencia_gris_blur, 10, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow("Detector Personas", threshold)
        ventana = cv2.waitKey(10)
        if ventana == ord("q"):
            break

print(frame.dtype)
video.release()
cv2.destroyAllWindows()
