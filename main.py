import pygame
import random

#game window
winx = 0
winy = 0
pygame.init()
WIDTH = 1000
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Placeholder name')
#(1000 - 40) / 3 = 320

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
      pygame.draw.rect(WIN, WHITE, pygame.Rect(self.x1, self.y1, self.wid, self.height), 2)

def screen_scroll():
   pass

#aspect ratio of screens should roughly be 16:9
s1 = screen((10, 80), 320, 190)
s2 = screen((10, 280), 320, 190)
s3 = screen((340, 80), 320, 190)
s4 = screen((340, 280), 320, 190) #390, 270
s5 = screen((670, 80), 320, 190)
s6 = screen((670, 280), 320, 190)

#main func
def main():
   global winx, winy

   #main game loop
   run = True
   while run:

      WIN.fill(BLACK)

      #get 'events'
      for event in pygame.event.get():

         if event.type == pygame.QUIT:
            run = False
         
         """if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               winx += 25
            elif event.key == pygame.K_LEFT:
               winx -= 25
            elif event.key == pygame.K_UP:
               winy -= 25
            elif event.key == pygame.K_DOWN:
               winy += 25"""
      
      #rectangle = surface, color, (x1, y1, x2, y2)
      s1.draw_screen()
      s2.draw_screen()
      s3.draw_screen()
      s4.draw_screen()
      s5.draw_screen()
      s6.draw_screen()

      pygame.display.flip()

if __name__ == '__main__':
   main()