import math
import pygame
import random

#game window
pygame.init()
WIDTH = 1000
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Placeholder name')

#color defs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
PURPLE = (127, 0 ,255)
GREY = (160, 160, 160)

screens = []
class screen():
   def __init__(self, pos: tuple, wid: int, height: int) -> None:
       self.x1 = pos[0]
       self.y1 = pos[1]
       self.x2 = pos[0] + wid
       self.y2 = pos[1] + height
       self.wid = wid
       self.height = height
       for screen in screens:
          pass
       screens.append(self)
   
   def draw_screen(self):
      """mx, my = pygame.mouse.get_pos()
      if mx > self.x1 and mx < self.x2 and my > self.y1 and my < self.y2:
         screenColor = WHITE
      else:
         screenColor = GREY"""
      pygame.draw.rect(WIN, WHITE, pygame.Rect(self.x1, self.y1, self.x2, self.y2), 2)

def screen_scroll():
   pass

#aspect ratio of screens should roughly be 16:9
s1 = screen((60, 80), 640, 360)
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
      s1.draw_screen()

      pygame.display.flip()

if __name__ == '__main__':
   main()