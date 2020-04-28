import pygame,sys
from pygame.locals import *



#Pantalla #------------------------------------------------------------------------------------------------
anchopantalla=900
altopantalla=800
pantalla=pygame.display.set_mode((anchopantalla,altopantalla))
x=(anchopantalla/3)

pantalla=pygame.display.set_mode((anchopantalla,altopantalla))
pygame.display.set_caption("Proyecto")

pygame.init()
#-----------------------------------------------------------------------------------------------------------------
configuraciones= True
entrada_1 = True
inicio = True
instrucciones= True
pantalla_actual = "entrada"
# Declaración de constantes y variables #------------------------------------------------------------------------------------------------
blanco = (255, 255, 255)
gris=(124,125,137)
azul=(69,135,245)
verde=(71,243,128)
amarillo=(247,242,70)
rojo=(202,36,13)
negro=(0,0,0)
#Declaracion botones #------------------------------------------------------------------------------------------------
b1=[x,290]
tamb1=[300,45]
colb1=[gris,azul]

b2=[x,340]
tamb2=[300,45]
colb2=[gris,verde]

b3=[x,390]
tamb3=[300,45]
colb3=[gris,amarillo]

b4=[x,440]
tamb4=[300,45]
colb4=[gris,rojo]

b5=[741,760]
tamb5=[100,45]
# fuentes y texto ----------------------------------------------------------------------------
def texto(tama,color,msg,x=0,y=0):
    if tama == 1:
        Font = pygame.font.SysFont("None",15)
    elif tama == 2:
        Font = pygame.font.SysFont("None",30)
    elif tama == 3:
        Font = pygame.font.SysFont("None",45)
    elif tama == 4:
        Font = pygame.font.SysFont("Century",60)

    texto = Font.render(msg,True,color)
    pantalla.blit(texto,(x,y))
#-----------------------------------------------------------------------------------------------
def botones(texto,superficie,estado,pos,tam,identidad=None):
    global pantalla_actual,instrucciones,inicio,configuraciones,entrada_1
    cursor=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    #print(cursor)
    print("Estas en",pantalla_actual)
    if pos[1]+tam[0]>cursor[0]>tam[0] and pos[1]+tam[1]>cursor[1]>tam[1] and pos[1]+tam[1]<cursor[1]+tam[1]:

        if click[0]==1:

            if identidad == "Inicio":
                pantalla.fill(blanco)
                Inicio()
                entrada_1= False
            elif identidad == "Instrucciones":
                pantalla.fill(blanco)
                Instrucciones()
                entrada_1= False
            elif identidad == "Configuracion":
                pantalla.fill(blanco)
                Configuracion()
                entrada_1= False
            elif identidad == "Salir":
                terminar()
                entrada_1= False
            elif identidad == "Entra":
                pantalla.fill(blanco)
                pygame.display.update()
                if pantalla_actual == "Instrucciones":
                    instrucciones = False
                elif pantalla_actual == "Configuracion":
                    configuraciones = False
                elif pantalla_actual == "Inicio":
                    inicio = False
                entrada()



        boton = pygame.draw.rect(superficie,estado[1],(pos[0],pos[1],tam[0],tam[1]))
    else:
        boton = pygame.draw.rect(superficie,estado[0],(pos[0],pos[1],tam[0],tam[1]))

#---------------------------------------------------------------------------------------------
def entrada():
    global pantalla_actual,entrada_1
    pantalla_actual = "entrada_1"
    print("Estas en",pantalla_actual)
    entrada_1 = True
    while entrada_1:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()

        pantalla.fill(blanco)
        texto(4, azul,"Proyecto listas",x-50,80)
        botones("Iniciar", pantalla, colb1, b1, tamb1,"Inicio")
        texto(2,negro,"Iniciar",b1[0]+120,b1[1]+15)
        botones("Instrucciones", pantalla, colb2, b2, tamb2,"Instrucciones")
        texto(2,negro,"Instrucciones",b2[0]+100,b2[1]+15)
        botones("Configuracion", pantalla, colb3, b3, tamb3,"Configuracion")
        texto(2,negro,"Configuracion",b3[0]+100,b3[1]+15)
        botones("Salir", pantalla, colb4, b4, tamb4,"Salir")
        texto(2,negro,"Salir",b4[0]+128,b4[1]+15)
        pygame.display.update()

    return 0
#-----------------------------------------------------------------------------------------------
def Inicio():
    global pantalla_actual,inicio
    pantalla_actual = "Inicio"
    print("Estas en",pantalla_actual)
    inicio = True
    while inicio:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()
            texto(4, azul,"Proyecto listas",x-50,80)
            botones("volver", pantalla, colb4, b5, tamb5,"Entra")
            texto(2, negro,"Volver",760,769)
            pygame.display.update()

    return 0
#------------------------------------------------------------------------------------------------
def Instrucciones():
    global pantalla_actual,instrucciones
    pantalla_actual = "Instrucciones"
    print("Estas en",pantalla_actual)
    instrucciones = True
    while instrucciones:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()


            texto(4, azul,"Instrucciones",x-50,80)
            texto(1, negro,"aun no sabemos",x-50,250)
            botones("volver", pantalla, colb4, b5, tamb5,"Entra")
            texto(2, negro,"Volver",760,769)
            pygame.display.update()

    return 0
#------------------------------------------------------------------------------------------------
def Configuracion():
    global pantalla_actual,Configuraciones
    pantalla_actual = "Configuracion"
    print("Estas en",pantalla_actual)
    configuraciones = True
    while configuraciones :
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()


            texto(4, azul,"Configuracion",x-50,80)
            texto(1, negro,"aun no sabemos",x-50,250)
            botones("volver", pantalla, colb4, b5, tamb5,"Entra")
            texto(2, negro,"Volver",760,769)
            pygame.display.update()

    return 0
#------------------------------------------------------------------------------------------------
def terminar():
    print("He salido del programa, chaooooo: te quelo mucho mi amor .... :*")
  pygame.quit()
  sys.exit()
#-----------------------------------------------------------------------
entrada()
