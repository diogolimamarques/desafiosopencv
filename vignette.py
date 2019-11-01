########################################################################
# Projeto           : Desafio Senai: Filtro Vignette
#
# Nome do programa  : vignette.py
#
# Autor             : Diogo Lima
#
# Data de criacao   : 16-10-2019
#
# Funcionamento     : Le um arquivo atraves dos argumentos e devolve uma versao em preto e branco com o filtro vignette aplicado
#                     em seu centro. 
#                     Argumentos: Endereco do arquivo, largura e altura do filtro. Caso nao deseje especificar estes valores, 
#                     usa como base 350 para altura e largura.
#
# Hist. de Revisao  :
#
# Data        Author      Ref    Revisao
# 16-10-2019  diogo       1      Codigo finalizado
# 01-11-2019  diogo       2      Codigo passou a aceitar argumentos de entrada. Mudanca para Python. Correcao de bugs.
########################################################################

import cv2
import numpy as np
import sys


########################### CODIGO PRINCIPAL ##########################

# Recieves a matrix, number of rows and columns and returns the maximum value of the matrix.

def getMaximum(maxmatrix, rows, cols):
  maximum = 0
  print(rows)
  print(cols)
  x = 0
  y = 0
  while x < rows-1:
    while y < cols-1:
      maximum = max(maxmatrix[x][y], maximum)
      y = y + 1
    x = x + 1
  return maximum

# Recieves the image and the width and height of the vignette mask
def vignetteFilter(image, width, height):
# Get image width and height
  cols, rows = image.shape

#Create the vignette effect
  gaussianCols = cv2.getGaussianKernel(cols, int(width))
  gaussianRows = cv2.getGaussianKernel(rows, int(height))
  transposedArray = gaussianRows.T
  gaussianMatrix = gaussianCols * transposedArray
  vignetter = gaussianMatrix/(getMaximum(gaussianMatrix, rows, cols))

#Apply the vignette effect to the image
  imagefiltered = image*vignetter

  return imagefiltered
# Read arguments and calculate number of arguments


########################### CODIGO PRINCIPAL ##########################

path = sys.argv[1]
numargs = 1
# Check number of arguments

if(len(sys.argv) > 2):
  width = sys.argv[2]
  height = sys.argv[3]
  numargs = numargs + 2
else:
  width = 350
  height = 350

# Load OpenCV image without changing anything on their color pattern
image = cv2.imread(path, 0)

imagefiltered = vignetteFilter(image, width, height)

cv2.imwrite('VignetteImage.png',imagefiltered)
image = cv2.imread('VignetteImage.png')
cv2.imshow("Vignetter:", image)
 
cv2.waitKey(0)

############################ FIM DO CODIGO ############################
