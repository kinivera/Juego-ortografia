# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:32:52 2020

@author: 57313
"""


import pygame
from pygame.locals import *

#Pantalla
anchopantalla=800
altopantalla=400
pantalla=pygame.display.set_mode((anchopantalla,altopantalla))
pygame.display.set_caption("Proyecto")
blanco = (255, 255, 255)

pygame.init()

def introduccion():
    introJuego=True
    
    while introJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pantalla.fill(blanco)
            pygame.display.update()
    