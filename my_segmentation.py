########################################################################
# Projeto           : Desafio Senai: Filtro red color
#
# Nome do programa  : my_segmentation.py
#
# Autor             : Diogo Lima
#
# Data de criacao   : 16-10-2019
#
# Funcionamento     : Le um endereco e uma imagem e recebe um ou dois argumentos de threshold para a cor vermelha. Aceita ruidos
#                     De outras cores ate 120 de azul e verde.
#
# Hist. de Revisao  :
#
# Data        Author      Ref    Revisao
# 16-10-2019  diogo       1      Codigo finalizado
# 01-10-2019  diogo       2      Codigo transformado de C++ para python. Passou a usar os canais HSV.
########################################################################

import cv2
import numpy as np
import sys

def concatenaExibe(img1, img2, showName):
# Une duas imagens horizontalmente
  concat = np.concatenate((img1, img2), axis=1)
  cv2.imshow(showName, concat)

  return concat

########################### CODIGO PRINCIPAL ##########################
path = sys.argv[1];
readA = sys.argv[2];
readB = ""
valueA = int(readA)
valueB = 0;
numargs = 2;

# Check number of arguments

if(len(sys.argv) > 3):
  readB = sys.argv[3];
  valueB = int(readB)
  numargs = numargs + 1;
  
# Load OpenCV image without changing anything on their color pattern
image = cv2.imread(path)

# Split channels from image
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
  
# Segmenting based on the channel intensity

if(numargs <= 3):
  #th, r = cv2.threshold(r, valueA, 255, 0)
  lower_red = np.array([valueA,0,0])
  upper_red = np.array([255,120,120])
elif (numargs > 3):
  #th, r = cv2.threshold(r, valueA, valueB, 0)
  lower_red = np.array([valueA,0,50])
  upper_red = np.array([valueB,120,120])

mask1 = cv2.inRange(hsv, lower_red, upper_red)


color_r = cv2.bitwise_and(image, image, mask = mask1)
  
concatenaExibe(image, color_r, "Segmentacao vermelha:")
  
cv2.waitKey(0)

############################ FIM DO CODIGO ############################
