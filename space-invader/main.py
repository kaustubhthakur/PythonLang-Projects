import pygame
import os
import time
import random
pygame.font.init()
WIDTH=650
HEIGHT=600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader")

#ENEMIES
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))

#PLAYER
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))


RED_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(WIDTH,HEIGHT))

class Ship:
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health= health
        self.ship_img= None
        self.lasers = []
        self.laser_img = None
        self.cool_down_counter = 0

    def draw(self,window):
        window.blit(self.ship_img,(self.x,self.y))
        

class Player(Ship):
    def __init__(self,x,y,health):
        super() __init__(x,y,health)
        self.ship_img=YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health



def main():
    running = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans",40)
    player_vel = 5
    player = Player(300,550)


    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG,(0,0));

        lives_label = main_font.render(f"Lives:{lives}" ,1, (255,255,255))
        level_label = main_font.render(f"Level:{level}",1,(255,255,255))
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))
        player.draw(WIN)
        pygame.display.update()

    while running:
        clock.tick(FPS)
        redraw_window()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x -player_vel >0:
            player.x-=player_vel
        if keys[pygame.K_d] and ship.x +player_vel+50<WIDTH:
            player.x +=player_vel
        if keys[pygame.K_w] and ship.y -player_vel>0:
            player.y -=player_vel
        if keys[pygame.K_s] and ship.y+player_vel + 50<HEIGHT:
            splayer.y +=player_vel
       

main()



