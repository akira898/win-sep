import random
import pygame
pygame.mixer.init()
def sound(lista):
    selectSound=random.randint(0,len(lista)-1)
    try:
        voz=pygame.mixer.Sound(lista[selectSound]+".mp3")
        voz.play()
    except FileNotFoundError:
        print("this doesn't exist")