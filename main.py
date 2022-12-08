import cv2
import numpy as np
import time

video = cv2.VideoCapture("sample.mp4")
frame_diferencia = np.zeros((720, 1280), dtype="uint8")
lista_contornos_validos = []

time.sleep(2)
while True:
    ret, frame = video.read()

    if ret == True:
        ret, frame2 = video.read()
        diferencia = cv2.absdiff(frame, frame2)
        diferencia_gris = cv2.cvtColor(diferencia, cv2.COLOR_RGB2GRAY)
        diferencia_gris_blur = cv2.GaussianBlur(diferencia_gris, (5, 5), 0)
        _, threshold = cv2.threshold(diferencia_gris_blur, 10, 255, cv2.THRESH_BINARY)

        kernel = np.zeros((5,5), np.uint8)
        threshold_dilatado = cv2.dilate(threshold, kernel, iterations=2)

        #Contornos deteccion y filtro de contornos por tamaño de su area
        contornos, _ = cv2.findContours(threshold_dilatado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # filtro =>
        iterador = 0
        for contorno in contornos:
            iterador = iterador+1
            x, y, w, h = cv2.boundingRect(contorno)
            area = w*h
            if area >= 50000:
                cv2.drawContours(frame, [contorno], 0, (255, 0, 0), 3)
        

        cv2.imshow("Detector Personas", frame)
        ventana = cv2.waitKey(10)
        if ventana == ord("q"):
            break

print(frame.dtype)
video.release()
cv2.destroyAllWindows()
