import pygame
from pygame.locals import *

#Pantalla
anchopantalla=800
altopantalla=400
pantalla=pygame.display.set_mode((anchopantalla,altopantalla))
pygame.display.set_caption("Proyecto")

pygame.init()

# Declaración de constantes y variables
blanco = (255, 255, 255)
gris=(124,125,137)
azul=(69,135,245)
verde=(71,243,128)
amarillo=(247,242,70)
rojo=(326,26,63)


#Declaracion botones
b1=[300,290]
tamb1=[200,45]
colb1=[gris,azul]

b2=[300,340]
tamb2=[200,45]
colb2=[gris,verde]

b3=[300,390]
tamb3=[200,45]
colb3=[gris,amarillo]

b4=[300,440]
tamb4=[200,45]
colb4=[gris,rojo]


                
   
def textoboton(msg,botonx,botony,ancho,alto):
    textosuperficie, textorect= msg
    textorect.center=(botonx+(ancho/2),botony+(alto/2))
    pantalla.blit(textosuperficie,textorect)
    
def botones(texto,superficie,estado,pos,tam,identidad=None):
    cursor=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if pos[0]+tam[0]>cursor[0]>tam[0] and pos[1]+tam[1]>cursor[1]>tam[1] and pos[1]+tam[1]<cursor[1]+tam[1]:
        if click[0]==1:
            if identidad == "Inicio":
                pass
            elif identidad == "Instrucciones":
                pass
            elif identidad == "Configuracion":
                pass
            elif identidad == "Salir":
                quit()
            boton = pygame.draw.rect(superficie,estado[1],(pos[0],pos[1],tam[0],tam[1]))
    else:
        boton = pygame.draw.rect(superficie,estado[0],(pos[0],pos[1],tam[0],tam[1]))
    
    textoboton(texto, pos[0], pos[1], tam[0], tam[1])
    
    
   
def introduccion():
    introJuego=True
    
    while introJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pantalla.fill(blanco)
            botones("Iniciar", pantalla, colb1, b1, tamb1,"Inicio")
            botones("Instrucciones", pantalla, colb2, b2, tamb2,"Instrucciones")
            botones("Configuracion", pantalla, colb3, b3, tamb3,"Configuracion")
            botones("Salir", pantalla, colb4, b4, tamb4,"Salir")
            
        pygame.display.update()
    
    
    
