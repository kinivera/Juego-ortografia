import codecs
import random
import datetime 
from datetime import timedelta
import pygame,sys
from pygame.locals import *
from pygame_input import *
inputs = Inputs()

rng = random.Random()

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
edad =True
ni=True
jo=True
dialogo= True
name =""
pantalla_actual = "entrada"
# Declaración de constantes y variables #------------------------------------------------------------------------------------------------
blanco = (255, 255, 255)
gris=(124,125,137)
azul=(69,135,245)
verde=(71,243,128)
amarillo=(247,242,70)
rojo=(202,36,13)
negro=(0,0,0)
vr=(18,141,104)
mor=(102,34,215)
naranja=(223,77,6)
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

colb6=[gris,vr]
colb7=[gris,naranja]
colb8=[gris,mor]
#Variables Cronometro------------------------------------------------------------------------------------------------
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 25)
numero_de_fotogramas = 0
tasa_fotogramas = 60
instante_de_partida = 90
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
    print(cursor)
    #print("Estas en",pantalla_actual)
    
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
                
            elif identidad == "11-":
                pantalla.fill(blanco)
                Ni()
                inicio= False 
                
                
            elif identidad == "12+":
                pantalla.fill(blanco)
                Jo()
                dialogo=False
                inicio = False
                
            elif identidad == "26+":
                pantalla.fill(blanco)
                Ni()
                inicio= False  
            
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

#Cronometro --------------------------------------------------------------------------------------------------------------------------------     


#Funciones del juego -------------------------------------------------------------------------------------------------------------------------       
def tiempo(ti,final):
    resultado = False
    ahora2 = datetime.datetime.now()
    inicio2 = ahora2
    if inicio2 >= final:
        resultado = True
    return resultado

def juego(a,b):
    resultado=0
    for i in range(len(a)):
        st = a[i].replace('\r', '')
        if st.replace('\n','')==b:
            resultado+=1
    return b, resultado
#Funcion texto dialogo----------------------------------------------------------------------------------------------------------------------------
def dial():
    global name,consolidado 
    consolidado = 0
    font = pygame.font.Font(None, 50)
    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.KEYDOWN:
                if eventos.unicode.isalpha():
                    name += eventos.unicode
                elif eventos.key == pygame.K_SPACE:
                    name= name+"    "
                elif eventos.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif eventos.key == pygame.K_RETURN:
                    print(name)
                    name= ""
                    while tiempo(ti,final) == False :
                     #while eventos.key != pygame.K_RETURN:
                         res=juego(m,name)
                         consolidado+=res[1]
                         print(res)
                         
                    print("¡Tu resultado es!: ", consolidado) 

            elif eventos.type == QUIT:
                terminar()
                
        botones("volver", pantalla, colb4, b5, tamb5,"Entra")
        texto(2, negro,"Volver",760,769)         
        block = font.render(name, True, negro)
        #block.get_rect().center = pantalla.get_rect().center
        pantalla.blit(block,block.get_rect())
        pygame.display.flip()
#Funcion para jovenes----------------------------------------------------------------------------------------------------------------------------
    
def Jo():
    global pantalla_actual,jo,m,s,ti,final
    pantalla_actual = "jo"
    print("Estas en",pantalla_actual)
    jo = True
    dialogo = True
    r = random.randrange(0,3)
    listas = ["Aplicaciones", "Bandas de rock", "Paises"]
    texto1 = codecs.open("Aplicaciones.txt", "r", "utf-8")
    texto2 = codecs.open("Bandas de rock.txt", "r", "utf-8")
    texto3 = codecs.open("Paises.txt", "r", "utf-8")
    a = texto1.readlines()
    b = texto2.readlines()
    c = texto3.readlines()
    print (listas[r])
    texto(2,negro,"La categoria que te toco es:"+ listas[r],x-40,190)
    s = [a,b,c]
    m = s[r]
    texto(4, azul,"Empieza el juego",x-50,80)
    
    
    ahora = datetime.datetime.now()
    ti = ahora
    final = ti+timedelta(seconds=20)
                           
    
 
                   

    while jo:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()
                
                
            botones("volver", pantalla, colb4, b5, tamb5,"Entra")
            texto(2, negro,"Volver",760,769) 
            dial()
            
            

                            #print(consolidado+=juego(m,z)[1])
                    
                   
        pygame.display.update()

    return 0
#-----------------------------------------------------------------------------------------------------------------------------------------------
def Ni():
    global pantalla_actual,ni
    pantalla_actual = "ni"
    print("Estas en",pantalla_actual)
    ni = True
    while ni:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()
            
            
            texto(4, azul,"Hola",x-50,80)
            botones("volver", pantalla, colb4, b5, tamb5,"Entra")
            texto(2, negro,"Volver",760,769)
            pygame.display.update()

    return 0
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
#-----------------------------------------------------------
def Inicio():
    global pantalla_actual,inicio
    pantalla_actual = "Inicio"
    print("Estas en",pantalla_actual)
    inicio = True
    while inicio:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()
            
            botones("Iniciar", pantalla, colb6, b1, tamb1,"11-")
            texto(2,negro,"Infancia: Menores 11",b1[0]+50,b1[1]+15)
            botones("Instrucciones", pantalla, colb7, b2, tamb2,"12+")
            texto(2,negro,"Jovenes: 12-26",b2[0]+60,b2[1]+15)
            botones("Configuracion", pantalla, colb8, b3, tamb3,"26+")
            texto(2,negro,"Adultos",b3[0]+110,b3[1]+15)
        
            
            texto(4, negro,"Escoge tu rango de edad",x-150,150)
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
            
            texto(2, negro,"Volver",760,769)
            imagen = pygame.image.load("Instruccion1.jpg")
            pantalla.blit(imagen,(0,0))
            
            botones("volver", pantalla, colb4, b5, tamb5,"Entra")
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
    pygame.quit()
    sys.exit()
#-----------------------------------------------------------------------
entrada()