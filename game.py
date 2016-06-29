import pygame
import math
import random
import time


pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("StarsWars")

WHITE = [255,255,255]
RED = (255, 0, 0)
BLACK = [0,0,0]

background_image = pygame.image.load('galaxy.jpg').convert()
ship_image = pygame.image.load('ship.png').convert()
ship_image.set_colorkey(WHITE)
click_sound = pygame.mixer.Sound("sound.wav")

done = False
screen.blit(background_image, [0,0])
screen.blit(ship_image, [350,450])
pygame.display.flip()
clock = pygame.time.Clock()
time.sleep(0.05)
click_sound.play()
 
# -------- Main Program Loop -----------
i = 0
while not done:
    if i > 500:
        i = 0
    x,y = pygame.mouse.get_pos()
    screen.blit(background_image, [0,i])
    screen.blit(background_image, [0,i-500])
    screen.blit(ship_image, [x,y])
    pygame.display.flip()
    i = i+2
    
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    
 
    # --- Go ahead and update the screen with what we've drawn.
    
 
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()
    
