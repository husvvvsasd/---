from random import *
from pygame import *
from datetime import datetime


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x_sprite, y_sprite, x_size, y_size, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(x_size, y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_sprite
        self.rect.y = y_sprite
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self, sprite_image, x_sprite, y_sprite,x_size, y_size, speed):    
        super().__init__ (sprite_image, x_sprite, y_sprite,x_size,y_size, speed)
        self.num_bullet = 5
        self.rel_time = False
        self.start_rel =  None
        self.health = 3

    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, sprite_image, x_sprite, y_sprite,x_size, y_size, speed):    
        super().__init__ (sprite_image, x_sprite, y_sprite,x_size,y_size, speed)     
        self.speed_x = speed
        self.speed_y = speed  
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 450:
            self.speed_y *= -1 
 
pong1 = Player('pong.png',10 ,100,50,150,10)            
pong2 = Player('pong.png',450 ,100,50,150,10) 
ball = Ball('ball.png',10 ,10,50,50,3)           
color1 = (255, 255, 255)
game = True
clock=time.Clock()
FPS = 60
window = display.set_mode((500, 500))

window.fill(color1)

font.init()
font1 = font.Font(None,35)

finish = False
font_winp1 = font1.render('WIN p1',True,(0,0,0))
font_winp2 = font1.render('WIN p2',True,(0,0,0))
while game:
    if ball.rect.x >= 500:
        window.blit(font_winp1,(250,250))
        finish = True
    elif ball.rect.x <= 0:
        window.blit(font_winp2,(250,250))
        finish = True
    if not finish:
        window.fill(color1)    
        pong1.update_left()
        pong2.update_right()
        pong1.reset()
        pong2.reset()
        ball.update()
        ball.reset()
        if sprite.collide_rect(ball,pong1) or sprite.collide_rect(ball,pong2):
            ball.speed_x *= -1
        
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)     