import codecs
import random

random = random.Random()
r = (random.randrange(0,7))

listas = ["Monosílabos con tílde diacrítica", "Calsificación de las palabras según su acento", "Departamentos de Colombia", "Música para planchar, mejores novelas de los 90´s", "Reproductores de música de los 90´s", "Monedas en LATAM"]
texto1 = codecs.open("Monosílabos_diacrítica.txt" "r", "utf-8")
texto2 = codecs.open("Clas_palabras.txt", "r", "utf-8")
texto3 = codecs.open("Departamentos_de_Colombia.txt", "r", "utf-8")
texto4 = codecs.open("musica_plan.txt", "r", "utf-8")
texto5 = codecs.open("mejores90´s.txt", "r", "utf-8")
texto6 = codecs.open("rerpo_90´s.txt", "r", "utf-8")
texto7 = codecs.open("monedaLA.txt", "r", "utf-8")

a = texto1.readlines()
b = texto2.readlines()
c = texto3.readlines()
d = texto4.readlines()
e = texto5.readlines()
f = texto6.readlines()
g = texto7.readlines()

s = [a,b,c]

m = s[r]