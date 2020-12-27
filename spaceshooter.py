import pgzrun
from random import randint
BLACK = (0,0, 0)
HEIGHT  = 700
WIDTH = 1000

player = Actor("playership")
player.bottom = HEIGHT
player.x = WIDTH//2

bullets = []
enemies = []
is_player_dead = False

def draw():
    screen.clear()
    screen.blit("sky",(0,0))
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()

def update():
    if not is_player_dead:
        move_player()
        move_bullet()
        move_enemy()
        bullet_collision()
        player_collision()

def on_key_down(key):
    if not is_player_dead:
        if key == keys.SPACE:
            create_bullet()

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

def move_enemy():
    for enemy in enemies:
        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            create_enemy()
        else:
            enemy.y += 5

def create_bullet():
    bullet = Actor("bullet")
    bullet.x = player.x
    bullet.y = player.top
    bullets.append(bullet)

def create_enemy():
    enemy = Actor("enemygreen")
    enemy.top = 0
    enemy.x = randint(50, WIDTH-50)
    enemies.append(enemy)

def bullet_collision():
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                create_enemy()
                bullets.remove(bullet)
                sounds.shoot.play()

def player_collision():
    global is_player_dead
    for enemy in enemies:
        if enemy.colliderect(player):
            player.image = "damageship"
            enemies.remove(enemy)
            is_player_dead = True

create_enemy()
pgzrun.go()
