import math
import pygame
import random

#game window
pygame.init()
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Placeholder name')

#color defs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class screen():
   def __init__(self, pos: tuple, wid: int, height: int) -> None:
       self.x1 = pos[0]
       self.x2 = pos[1]
       self.x2 = pos[0] + wid
       self.y2 = pos[1] + height
       self.wid = wid
       self.height = height
   
   def draw_screen():
      pass


#main func
def main():

   #main game loop
   run = True
   while run:

      WIN.fill(BLACK)

      #get 'events'
      for event in pygame.event.get():

         if event.type == pygame.QUIT:
            run = False
      
      #rectangle = surface, color, (x1, y1, x2, y2)
      pygame.draw.rect(WIN, RED, pygame.Rect(30, 50, 60, 60), 2)

      pygame.display.flip()

if __name__ == '__main__':
   main()