import cv2
import numpy as np

x = 50
y = 50

camara = cv2.VideoCapture(0)

if camara.isOpened() is False:
    print("Error al acceder a la cámara")
else:
    anchoFrame = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
    altoFrame = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

    opencv = cv2.imread("./img/opencv.png", cv2.IMREAD_UNCHANGED)
    alto, ancho, canales = opencv.shape

    b,g,r,a = cv2.split(opencv) # dividir canales de la imagen: b,g,r y transparencia (alfa)
    opencv = cv2.merge([b,g,r]) # componemos la imagen pero sin canal alfa, ya que lo usuaremos para hacer la máscara


    #fg = np.zeros((altoFrame, anchoFrame, 3), np.uint8)
    #fg[y:y+alto,x:x+ancho] = opencv

    a = a / 255.0
    alfa = cv2.merge([a,a,a])
    #mascara =  np.zeros((altoFrame, anchoFrame, 3), np.uint8)
    #mascara[y:y+alto,x:x+ancho] = alfa
    #mascara_inversa = cv2.bitwise_not(mascara)

    while camara.isOpened() is True:
        ret, frame = camara.read()
        if ret is True:
            frame[y:y+alto, x:x+ancho] = alfa * opencv + (1-alfa) * frame[y:y+alto, x:x+ancho]

            #bg = cv2.bitwise_and(frame, frame)
            #image = cv2.bitwise_or(fg, bg)
            cv2.imshow("MOSCA", frame)
        if cv2.waitKey(20) & 0xFF == ord('x'):
                break
    camera.release();
    cv2.destroyAllWindows()