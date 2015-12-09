#importa pygame y los modulos del sistema
import pygame,sys
from pygame.locals import *

#para iniciar pygame se escribe
pygame.init()

#-------------------------------------------------------------------------------------
#Colores en pygame
color = (0,140,60)#verde
colorDos = pygame.Color(255,120,9)#naranja
#-------------------------------------------------------------------------------------

#para crear una ventana
#recibe un arreglo de puntos o tupla
ventana = pygame.display.set_mode((400,300))

#para colocar un titulo a la ventana 
pygame.display.set_caption("Hola mundo")

#bucle infinito que se ejecuta durante toda la aplicacion
while True:
	#se llena la ventana con el color hecho previamente
	ventana.fill(colorDos)
	#captura los eventos
	for evento in pygame.event.get():
		#si el usuario presiona salir
		if evento.type == QUIT:
			#se cierra todo
			pygame.quit()
			sys.exit()

	pygame.display.update()