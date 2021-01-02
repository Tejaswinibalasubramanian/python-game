import math
import pgzrun
import pygame
from random import randint
RED = (156,9,29) 
HEIGHT = 650
WIDTH = 1000

player = Actor("gun")
player.bottom = HEIGHT
player.x = WIDTH//2

bullets = []
baloons = []
is_player_dead = False
collided = False
score_value = 0
over_font = pygame.font.Font('freesansbold.ttf', 64)

def draw():
    screen.clear()
    screen.blit("screen",(0,0))
    show_score(score_value)
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for baloon in baloons:
       baloon.draw()

def update():
    if not is_player_dead:
        move_player()
        move_bullet()
        move_baloon()
        bullet_collision()
        player_collision()
     
def on_key_down(key):
    if not is_player_dead:
        if key == keys.SPACE:
            create_bullet()
            if not collided:
                    global score_value  
                    score_value -= 1

def move_player():
    if keyboard.left:
        player.x -= 10
    if keyboard.right:
        player.x += 10
    if keyboard.up:
        player.y -= 10
    if keyboard.down:
        player.y += 10
         

def move_bullet():
    for bullet in bullets:
        if bullet.bottom < 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

def move_baloon():
    for baloon in baloons:
        if baloon.top > HEIGHT:
            baloons.remove(baloon)
            create_baloon()
        else:
            baloon.y += 5

def create_bullet():
    bullet = Actor("bullet")
    bullet.x = player.x
    bullet.y = player.top
    bullets.append(bullet)

def create_baloon():
    baloon = Actor("singlebaloon")
    baloon.top = 0
    baloon.x = randint(50, WIDTH-50)
    baloons.append(baloon)

def bullet_collision():
    for bullet in bullets:
        for baloon in baloons:
            if bullet.colliderect(baloon):
                global score_value 
                score_value += 5
                collided = True
                baloons.remove(baloon)
                create_baloon()
                bullets.remove(bullet)
                sounds.shoot.play()
   
                

def player_collision():
    global is_player_dead
    for baloon in baloons:
        if baloon.colliderect(player):
            player.image = "damageship"            
            baloons.remove(baloon)
            global score_value 
            score_value = 0
            show_score(score_value)
            player.image = "gun"
            player.bottom = HEIGHT
            player.x = WIDTH//2
            screen.clear()
            screen.blit("screen",(0,0))            
            player.draw()
            create_baloon()
            
        

def show_score(score_value):
    font = pygame.font.Font('freesansbold.ttf', 32)  
    score = font.render("Score : " + str(score_value), True,(255,255,255))
    screen.blit(score,[0,0])
	
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
create_baloon()


pgzrun.go()

