#importa pygame y los modulos del sistema
import pygame,sys
from pygame.locals import *

#para iniciar pygame se escribe
pygame.init()

#para crear una ventana
#recibe un arreglo de puntos o tupla
ventana = pygame.display.set_mode((400,300))

#para colocar un titulo a la ventana 
pygame.display.set_caption("Hola mundo")

#bucle infinito que se ejecuta durante toda la aplicación
while True:
	#captura los eventos
	for evento in pygame.event.get():
		#si el usuario presiona salir
		if evento.type == QUIT:
			#se cierra todo
			pygame.quit()
			sys.exit()

	pygame.display.update()