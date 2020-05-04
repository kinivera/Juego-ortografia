import codecs
import random
import datetime 
from datetime import timedelta

rng = random.Random()
r = random.randrange(0,3)

ahora = datetime.datetime.now()
inicio = ahora
final = inicio+timedelta(seconds=10)

print(inicio)
print(final)

def tiempo(inicio,final):
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
 
listas = ["Aplicaciones.txt", "Bandas de rock.txt", "Paises.txt"]
texto1 = codecs.open(listas[0], "r", "utf-8")
texto2 = codecs.open(listas[1], "r", "utf-8")
texto3 = codecs.open(listas[2], "r", "utf-8")
a = texto1.readlines()
b = texto2.readlines()
c = texto3.readlines()

s = [a,b,c]

m = s[r]
print(listas[r])
palabra = input("*  ")

consolidado = 0
while tiempo(inicio,final) == False:
    res=juego(m,palabra)
    consolidado+=res[1]
    print(res)
    #print(consolidado+=juego(m,z)[1])
    palabra = input("*  ")
  
print("¡Tu resultado es!: ", consolidado)

texto1.close()
texto2.close()

