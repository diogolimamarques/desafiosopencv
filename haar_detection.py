########################################################################
# Projeto           : Desafio Senai: Detecção de features do rosto
#
# Nome do programa  : haar_detection.py
#
# Autor             : Diogo Lima
#
# Data de criacao   : 01-11-2019
#
# Funcionamento     : Faz uso da webcam para detectar, em tempo real, o rosto, os olhos e a boca do usuario. Devido a 
#                     imperfeicoes no modelo de haar cascade utilizado, gera alguns falsos positivos.
#
# Hist. de Revisao  :
#
# Data        Author      Ref    Revisao
# 01-11-2019  diogo       1      Conversao do codigo base de C++ para Python
# 02-11-2019  diogo       2      Correcao de problemas com o haar_cascade da boca
# 02-11-2019  diogo       3      Estruturacao dos comentarios
########################################################################

import cv2 as cv
import numpy as np

# Funcao que tem como objetivo a deteccao das features e exibicao dos circulos em volta das mesmas.

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        mouth = mouth_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
        for (x3,y3,w3,h3) in mouth:
            mouth_center = (x + x3 + w3//2, y + y3 + h3//2)
            radius = int(round((w3 + h3)*0.25))
            frame = cv.circle(frame, mouth_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face Detection', frame)

########################### CODIGO PRINCIPAL ##########################

# Instanciando as variaveis com os enderecos dos classificadores
face_cascade = cv.CascadeClassifier("./haar_data/haar_face.xml")
eyes_cascade = cv.CascadeClassifier("./haar_data/haar_eyeglasses.xml")
mouth_cascade = cv.CascadeClassifier("./haar_data/haar_mouth.xml")

camera_device = 0 #Camera padrao

# Lendo a webcam
cap = cv.VideoCapture(camera_device)

if not cap.isOpened:
    print('--(!)Erro na webcam')
    exit(0)

# Loop para a chamada da funcao de deteccao
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) Erro de captura de frame')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break

############################ FIM DO CODIGO ############################

