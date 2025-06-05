#Faça um programa que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load("zelda.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

