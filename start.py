from tkinter import font
import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

startFont = pygame.font.Font('freesansbold.ttf', 32)

def start(win, f: font):

   running = True
   while running:

      win.fill((0, 0, 0))

      gtext = f.render('heyo', True, (255, 255, 255))
      win.blit(gtext, (0, 0))

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
      
      pygame.display.flip()
         

start(window, startFont)