import pygame

pygame.init()
pygame.mixer.music.load('ToccatainD.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()