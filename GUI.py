#!/usr/bin/env python
#-*- coding: utf-8 -*-
import codecs
import random
import datetime
from datetime import timedelta
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
#Establece el estado de cada venta, si es falso esta cerrada -------------------------------------------------------------
configuraciones= False
entrada_1 = False
inicio = False
instrucciones= False
edad =False
ni=False
jo=False
dialogo= False
di=False
name = ""
pantalla_actual = "entrada"
# Declaración de colores-----------------------------------------------------------------------------------------------
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
#Declaracion datos botones ------------------------------------------------------------------------------------------------
#b=posicion, tamb=tamaño boton, col= colores-------------------------------------------------------------------------------
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
#Funcion que crea todos los botones del juego -----------------------------------------------------------------------------------------------
def botones(texto,superficie,estado,pos,tam,identidad=None):
    global pantalla_actual,instrucciones,inicio,configuraciones,entrada_1
    cursor=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    #print(cursor)
    #print("Estas en",pantalla_actual)

    if pos[1]+tam[0]>cursor[0]>tam[0] and pos[1]+tam[1]>cursor[1]>tam[1] and pos[1]+tam[1]<cursor[1]+tam[1]:#segun la ubicacion del cursor cambia el color del boton y permite saber su ubicacion

        if click[0]==1:#si esta el cursor en la primera posicion y esta corresponde a 1 preguntara por la identidad del boton  
# si se selecciona un boton, este abrira una nueva funcion y cerrara aquella en la que se encuentre 
            if identidad == "Inicio":
                pantalla.fill(blanco)
                Inicio()
                entrada_1= False
            elif identidad == "Instrucciones":
                pantalla.fill(blanco)
                Instrucciones()
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
                inicio = False

            elif identidad == "26+":
                pantalla.fill(blanco)
                Ad()
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


#si el mouse esta sobre el boton cambia su color
        boton = pygame.draw.rect(superficie,estado[1],(pos[0],pos[1],tam[0],tam[1]))
    else:
        boton = pygame.draw.rect(superficie,estado[0],(pos[0],pos[1],tam[0],tam[1]))

#Cronometro --------------------------------------------------------------------------------------------------------------------------------


#Funciones del juego -------------------------------------------------------------------------------------------------------------------------
def tiempo():# funcion para determinar de cuanto tiempo dispone el jugador y para mostrar en pantalla una cuenta regresiva 
    resultado = False
    ahora2 = datetime.datetime.now()
    r = final-ahora2
    crono=str (r)[2:7]
    if ahora2>= final:
        resultado = True
        
    return resultado,crono

def juego(a,b): # recoge la palabra escrita por el jugador y la compara con las listas, para asi determinar si obtiene punto o no
    resultado=0
    for i in range(len(a)):
        st = a[i].replace('\r', '')
        if st.replace('\n','') == b:
            resultado+=1
    return b, resultado
#Funcion texto dialogo----------------------------------------------------------------------------------------------------------------------------
# esta funcion permite agregar texto en la pantalla principal del juego 
def dial():
    global name,consolidado,dial
    consolidado = 0
    font = pygame.font.Font(None, 50)
    my_set = []
    name=""
    di=True
    while (tiempo()[0]==False and di):# Funciona mientras no se acabe el tiempo y la funcion dial este abierta 
    
        for eventos in pygame.event.get():
            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_RETURN:  #cuando se oprime enter ejecuta el juego, y lo agrega a una lista para asegurarse de que no se obtienen dos puntos por una misma palabra         
                    res=juego(m_a,name)
                    if(name not in my_set and res[1]==1):                     
                        consolidado+=res[1]
                        texto(4, verde,"+1",x+100,500)
                        my_set.append(name)
                        print(res)
                    else:
                        texto(4, rojo,"Palabra no valida",x,500)
                
                    pygame.display.flip()
                    pygame.time.wait(500)
                    blanquito = pygame.draw.rect(pantalla,blanco,(x-350,250,900,500))
                    name="" #permite volver a escribir una vez se da enter 
                elif eventos.key == pygame.K_SPACE:#permite agregar espacio
                    name= name+" "
                elif eventos.key == pygame.K_BACKSPACE:#permite borrar 
                    name = name[:-1]
                elif eventos.unicode.isalpha():#permite reconocer todos los caracteres del teclado  
                    name += eventos.unicode
                 #while eventos.key != pygame.K_RETURN:

            elif eventos.type == QUIT:
                terminar()
        
        
        blanquito = pygame.draw.rect(pantalla,blanco,(x,250,900,200))# evita que se sobreescriba la palabra, colocando un cuadrado blanco una y otra vez 
        texto(4, rojo,tiempo()[1],x+100,250)#muestra el cronometro en pantalla 
        botones("volver", pantalla, colb4, b5, tamb5,"Entra")
        texto(2, negro,"Volver",760,769)
        block = font.render(name, True, negro)#texto que se escribe en pantalla 
        blanquito = pygame.draw.rect(pantalla,blanco,(0,altopantalla/2-50,anchopantalla,100))
        pantalla.blit(block,(anchopantalla/2-15*(len(name)/2),altopantalla/2))#Muestra el texto que se escribe y le da la posicion 

        pygame.display.flip() 

#Funcion para niños----------------------------------------------------------------------------------------------------------------------------

def Ni():
    global pantalla_actual,ni,m_a,s,ti,final
    pantalla_actual = "ni"
    print("Estas en",pantalla_actual)
    ni = True

    rninos = (random.randrange(0,6))# Selecciona un numero al azar dentro del numero de lista que hay 
    
    listas_n = ["Colores", "Figuras", "Frutas", u"Números", "Partes del cuerpo", "Verduras"] # le da el nombre con el que se mostrara a cada lista 
    texto1_n = codecs.open("Respuestas/Colores.txt" ,"r", "utf-8")
    texto2_n = codecs.open("Respuestas/Figuras.txt", "r", "utf-8")
    texto3_n = codecs.open("Respuestas/Frutas.txt", "r", "utf-8")               # abre cada uno de los archivos que contienen las listas segun la categoria 
    texto4_n = codecs.open("Respuestas/Numeros.txt", "r", "utf-8")
    texto5_n = codecs.open("Respuestas/Partes del cuerpo.txt", "r", "utf-8")
    texto6_n = codecs.open("Respuestas/Verduras.txt", "r", "utf-8")
    a_n = texto1_n.readlines()
    b_n = texto2_n.readlines()
    c_n = texto3_n.readlines()
    d_n = texto4_n.readlines()              # lee los archivos 
    e_n = texto5_n.readlines()
    f_n = texto6_n.readlines()   

    #print (listas_n[rninos])
    texto(2,negro,"La categoria que te toco es:" + listas_n[rninos],x-40,190)# imprime en pantalla la categoria 
    s_a = [a_n,b_n,c_n,d_n,e_n,f_n] # Guarda como lista cada uno de los archivos 
    m_a = s_a[rninos] # selecciona el numero de lista escogida dado por el numero al azar 

    imagen = pygame.image.load("Imagenes/4.png") #titulo
    pantalla.blit(imagen,(0,0))
    ti = datetime.datetime.now()# Tiempo actual
    final = ti+timedelta(seconds=21) # Tiempo actual + el temporizador (ajustable)

    dial() 
    di=False
    while ni:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()
            
        pantalla.fill(blanco)
        imagen = pygame.image.load("Imagenes/666.png")
        pantalla.blit(imagen,(100,0))
        texto(4, negro,"Tu resultado es:"+ str (consolidado),200,altopantalla/2)
            

        botones("volver", pantalla, colb4, b5, tamb5,"Entra")
        texto(2, negro,"Volver",760,769)
        pygame.display.update()
    return 0
#funcion para jovenes analogo a la funcion niños-----------------------------------------------------------------------------------------------------------------------------------------------
def Jo():
    global pantalla_actual,jo,m_a,s,ti,final
    pantalla_actual = "jo"
    print("Estas en",pantalla_actual)
    jo = True

    rjovenes = (random.randrange(0,7))
    
    listas_j = ["Aplicaciones", "Bandas de Rock", "Cantantes Colombianos", u"Géneros Musicales", u"Países", u"Superhéroes de Marvel", u"Superhéroes de DC"]
    texto1_j = codecs.open("Respuestas/Aplicaciones.txt","r", "utf-8")
    texto2_j = codecs.open("Respuestas/Bandas de rock.txt", "r", "utf-8")
    texto3_j = codecs.open("Respuestas/Cantantes Colombianos.txt", "r", "utf-8")
    texto4_j = codecs.open("Respuestas/Generos musicales.txt", "r", "utf-8")
    texto5_j = codecs.open("Respuestas/Paises.txt", "r", "utf-8")
    texto6_j = codecs.open("Respuestas/Superheroes de marvel.txt", "r", "utf-8")
    texto7_j = codecs.open("Respuestas/superheroes DC.txt", "r", "utf-8")
    
    a_j = texto1_j.readlines()
    b_j = texto2_j.readlines()
    c_j = texto3_j.readlines()
    d_j = texto4_j.readlines()
    e_j = texto5_j.readlines()
    f_j = texto6_j.readlines()
    g_j = texto7_j.readlines()
        
    print (listas_j[rjovenes])
    texto(2,negro,"La categoria que te toco es:" + listas_j[rjovenes],x-40,190)
    s_a = [a_j,b_j,c_j,d_j,e_j,f_j,g_j]
    m_a = s_a[rjovenes]

    imagen = pygame.image.load("Imagenes/5.png")
    pantalla.blit(imagen,(0,0))
    ti= datetime.datetime.now()
   
    final = ti+timedelta(seconds=21)

    dial()
    di=False
    while jo:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()

        pantalla.fill(blanco)
        imagen = pygame.image.load("Imagenes/666.png")
        pantalla.blit(imagen,(100,0))
        texto(4, negro,"Tu resultado es:"+ str (consolidado),200,altopantalla/2)
        

        botones("volver", pantalla, colb4, b5, tamb5,"Entra")
        texto(2, negro,"Volver",760,769)
        pygame.display.update()
    return 0
# funcion para adultos analogo a la funcionniños---------------------------------------------------------------------------------------------
def Ad():
    global pantalla_actual,ad,m_a,s,ti,final
    pantalla_actual = "ad"
    print("Estas en",pantalla_actual)
    ad = True

    radultos = (random.randrange(0,7))
    
    listas_a = [u"Monosílabos con tílde diacrítica", u"Clasificación de las palabras según su acento", "Departamentos de Colombia", u"Música para planchar", "mejores novelas de los 90´s", u"Reproductores de música de los 90´s", "Monedas en LATAM"]
    texto1_a = codecs.open(u"Respuestas/Monosilabos_diacritica.txt" ,"r", "utf-8")
    texto2_a = codecs.open(u"Respuestas/Clas_palabras.txt", "r", "utf-8")
    texto3_a = codecs.open(u"Respuestas/Departamentos_de_Colombia.txt", "r", "utf-8")
    texto4_a = codecs.open(u"Respuestas/musica_plan.txt", "r", "utf-8")
    texto5_a = codecs.open(u"Respuestas/mejores90s.txt", "r", "utf-8")
    texto6_a = codecs.open(u"Respuestas/rerpo_90s.txt", "r", "utf-8")
    texto7_a = codecs.open(u"Respuestas/monedaLA.txt", "r", "utf-8")
    
    a_a = texto1_a.readlines()
    b_a = texto2_a.readlines()
    c_a = texto3_a.readlines()
    d_a = texto4_a.readlines()
    e_a = texto5_a.readlines()
    f_a = texto6_a.readlines()
    g_a = texto7_a.readlines()
    print (listas_a[radultos])
    Font = pygame.font.SysFont("None",30)
    texto_4 = Font.render("La categoria que te toco es:" + listas_a[radultos],True,negro)
    pantalla.blit(texto_4,(anchopantalla/2-texto_4.get_width()/2,190))
    s_a = [a_a,b_a,c_a,d_a,e_a,f_a,g_a]
    m_a = s_a[radultos]

    imagen = pygame.image.load("Imagenes/6.png")
    pantalla.blit(imagen,(0,0))
    ti = datetime.datetime.now()
   
    final = ti+timedelta(seconds=20)

    dial()
    di=False
    while ad:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()

        pantalla.fill(blanco)
        imagen = pygame.image.load("Imagenes/666.png")
        pantalla.blit(imagen,(100,0))
        
   
        texto(4, negro,"Tu resultado es:"+ str (consolidado),200,altopantalla/2)
        

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

# Muestra el menu principal del juego 
        pantalla.fill(blanco)
        imagen = pygame.image.load("Imagenes/1.png")
        pantalla.blit(imagen,(x-35,0))
        botones("Iniciar", pantalla, colb1, b1, tamb1,"Inicio")
        texto(2,negro,"Iniciar",b1[0]+120,b1[1]+15)
        botones("Instrucciones", pantalla, colb2, b2, tamb2,"Instrucciones")
        texto(2,negro,"Instrucciones",b2[0]+100,b2[1]+15)
        botones("Salir", pantalla, colb4, b3, tamb4,"Salir")
        texto(2,negro,"Salir",b3[0]+128,b3[1]+15)
        pygame.display.update()

    return 0
#---------------------------------------------------------------------
    
#una vez dentro del juego permite seleccionar la edad, y segun esta mostrara archivos determinados acorde con la edad del jugador 
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
#-----------------------------------------------------------------------------------------------
# abre una imagen donde aparecen las instrucciones generales del juego
def Instrucciones():
    global pantalla_actual,instrucciones
    pantalla_actual = "Instrucciones"
    print("Estas en",pantalla_actual)
    instrucciones = True
    while instrucciones:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                terminar()


            imagen = pygame.image.load("Imagenes/2.png")
            pantalla.blit(imagen,(x-50,200))
            imagen = pygame.image.load("Imagenes/3.png")
            pantalla.blit(imagen,(60,0))
            botones("volver", pantalla, colb4, b5, tamb5,"Entra")
            texto(2, negro,"Volver",760,769)
            pygame.display.update()

    return 0
#------------------------------------------------------------------------------------------------
#permite cerrar el juego 
def terminar():
    pygame.quit()
    sys.exit()
#-----------------------------------------------------------------------
entrada() 
