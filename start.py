import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

def start(win):
   boxes = []

   startFont = pygame.font.Font('freesansbold.ttf', 100)
   subfont = pygame.font.Font('freesansbold.ttf', 50)

   running = True
   while running:

      win.fill((0, 0, 0))

      gtext = startFont.render('Thingy', True, (51, 255, 51))
      gtextRect = gtext.get_rect()
      gtextRect.center = (WIDTH // 2, HEIGHT // 2)
      boxes.append(gtextRect)
      ttext = subfont.render('Tutorial', True, (51, 255, 51))
      ttextRect = ttext.get_rect()
      ttextRect.center = (WIDTH // 2, (HEIGHT // 2) + 100)
      boxes.append(ttextRect)

      win.blit(gtext, gtextRect)
      win.blit(ttext, ttextRect)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
            run = False
         
         elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            #this does nothing right now
            for box in boxes:
               x1, y1 = box.topleft
               x2, y2 = box.bottomright
               if x > x1 and x < x2 and y > y1 and y < y2:
                  running = False
      
      pygame.display.flip()
         

start(window)