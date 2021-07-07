import cv2
import numpy as np
camara = cv2.VideoCapture(0)

if camara.isOpened() is False:
    print("Error al acceder a la cámara")
else:
    ancho = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH) / 2)
    alto = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT) / 2)
    while camara.isOpened() is True:
        ret, frame = camara.read()
        if ret is True:
            #frame = cv2.resize(frame, (ancho, alto))
            #b, g, r = cv2.split(frame)
            #z = np.zeros_like(b)
            #procesado = cv2.GaussianBlur(frame, (11,11), 0)
            #procesado2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("WEBCAM", frame)
            #cv2.imshow("PROCESADO", procesado)
            #cv2.imshow("PROCESADO2", procesado2)
            #cv2.imshow("ROJO", r)
            #cv2.imshow("VERDE", g)
            #cv2.imshow("AZUL", b)
            #cv2.imshow("ROJO SIN GRISES", cv2.merge([z, z, r]))
            #cv2.imshow("VERDE SIN GRISES", cv2.merge([z, g, z]))
            #cv2.imshow("AZUL SIN GRISES", cv2.merge([b, z, z]))
            #cv2.imshow("AMARILLO", cv2.merge([z, g, r]))
            #cv2.imshow("MAGENTA", cv2.merge([b, z, r]))
            #cv2.imshow("CIAN", cv2.merge([b, g, z]))
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mascara = cv2.inRange(hsv, (100, 50, 50), (130, 150, 150))
            mascara2 = cv2.merge([mascara, mascara, mascara])
            mascara2 = cv2.bitwise_not(mascara2) # Invertir mascara 0->1 | 1->0
            fg = cv2.bitwise_and(frame, mascara2) #Se eliminan los 0 de la imagen
            cv2.imshow("HSV", hsv)
            cv2.imshow("MASCARA HSV", mascara)
            cv2.imshow("CHROMA", fg)
            if cv2.waitKey(20) & 0xFF == ord('x'):
                break

    cv2.destroyAllWindows()