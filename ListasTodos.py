import codecs
import random

#niños---------------------------------------------------------------------------------------------------------------------------
random = random.Random()
rniños = (random.randrange(0,6))

listas_n = ["Colores", "Figuras", "Frutas", "Números", "Partes del cuerpo", "Verduras"]
texto1_n = codecs.open("Colores.txt" "r", "utf-8")
texto2_n = codecs.open("Figuras.txt", "r", "utf-8")
texto3_n = codecs.open("Frutas.txt", "r", "utf-8")
texto4_n = codecs.open("Numeros.txt", "r", "utf-8")
texto5_n = codecs.open("Partes del cuerpo.txt", "r", "utf-8")
texto6_n = codecs.open("Verduras.txt", "r", "utf-8")

a_n = texto1_n.readlines()
b_n = texto2_n.readlines()
c_n = texto3_n.readlines()
d_n = texto4_n.readlines()
e_n = texto5_n.readlines()
f_n = texto6_n.readlines()

print (listas_n[rniños])
s_a = [a_n,b_n,c_n,d_n,e_n,f_n]
m_a = s_a[rniños]

#jóvenes-------------------------------------------------------------------------------------------------------------------------


random = random.Random()
rjovenes = (random.randrange(0,7))

listas_j = ["Aplicaciones", "Bandas de Rock", "Cantantes Colombianos", "Géneros Musicales", "Países", "Superhéroes de Marvel", "Superhéroes de DC"]
texto1_j = codecs.open("Aplicaciones.txt" "r", "utf-8")
texto2_j = codecs.open("Bandas de rock.txt", "r", "utf-8")
texto3_j = codecs.open("Cantantes Colombianos.txt", "r", "utf-8")
texto4_j = codecs.open("Generos musicales.txt", "r", "utf-8")
texto5_j = codecs.open("Paises.txt", "r", "utf-8")
texto6_j = codecs.open("Superheroes de marvel.txt", "r", "utf-8")
texto7_j = codecs.open("superheroes DC.txt", "r", "utf-8")

a_j = texto1_j.readlines()
b_j = texto2_j.readlines()
c_j = texto3_j.readlines()
d_j = texto4_j.readlines()
e_j = texto5_j.readlines()
f_j = texto6_j.readlines()
g_j = texto7_j.readlines()

print (listas_j[rjovenes])
s_a = [a_j,b_j,c_j,d_j,e_j,f_j,g_j]
m_a = s_a[rjovenes]

#adultos-------------------------------------------------------------------------------------------------------------------------


random = random.Random()
radultos = (random.randrange(0,7))

listas_a = ["Monosílabos con tílde diacrítica", "Calsificación de las palabras según su acento", "Departamentos de Colombia", "Música para planchar", "mejores novelas de los 90´s", "Reproductores de música de los 90´s", "Monedas en LATAM"]
texto1_a = codecs.open("Monosílabos_diacrítica.txt" "r", "utf-8")
texto2_a = codecs.open("Clas_palabras.txt", "r", "utf-8")
texto3_a = codecs.open("Departamentos_de_Colombia.txt", "r", "utf-8")
texto4_a = codecs.open("musica_plan.txt", "r", "utf-8")
texto5_a = codecs.open("mejores90´s.txt", "r", "utf-8")
texto6_a = codecs.open("rerpo_90´s.txt", "r", "utf-8")
texto7_a = codecs.open("monedaLA.txt", "r", "utf-8")

a_a = texto1_a.readlines()
b_a = texto2_a.readlines()
c_a = texto3_a.readlines()
d_a = texto4_a.readlines()
e_a = texto5_a.readlines()
f_a = texto6_a.readlines()
g_a = texto7_a.readlines()

print (listas_a[radultos])
s_a = [a_a,b_a,c_a,d_a,e_a,f_a,g_a]
m_a = s_a[radultos]