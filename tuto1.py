#importa pygame y los modulos del sistema
import pygame,sys
from pygame.locals import *

#para iniciar pygame se escribe
pygame.init()

#-------------------------------------------------------------------------------------
#Colores en pygame
color = (0,140,60)#verde
colorDos = pygame.Color(255,120,9)#naranja

#para crear una ventana
#recibe un arreglo de puntos o tupla
ventana = pygame.display.set_mode((400,300))

#-------------------------------------------------------------------------------------
#contruccion de formas
#linea
colorLinea = pygame.Color(70,80,150)
posXLinea = (60,80)
posYLinea = (160,100)
grosorLinea = 1
#parametros lienzo o ventana, color de la linea 
pygame.draw.line(ventana,colorLinea,posXLinea,posYLinea,grosorLinea)

#-------------------------------------------------------------------------------------
#Dibujar un circulo
colorCirculo = (8,70,120)
puntoCirculo = (80,90)
radioCirculo = 20
pygame.draw.circle(ventana,colorCirculo,puntoCirculo,radioCirculo)
#-------------------------------------------------------------------------------------
#Dibujar un rectangulo
colorRect = (130,70,70)
posRect = (0,0,100,50)
pygame.draw.rect(ventana,colorRect,posRect)
#-------------------------------------------------------------------------------------

#para colocar un titulo a la ventana 
pygame.display.set_caption("Hola mundo")

#bucle infinito que se ejecuta durante toda la aplicacion
while True:
	#se llena la ventana con el color hecho previamente
	#ventana.fill(colorDos)
	#captura los eventos
	for evento in pygame.event.get():
		#si el usuario presiona salir
		if evento.type == QUIT:
			#se cierra todo
			pygame.quit()
			sys.exit()

	pygame.display.update()