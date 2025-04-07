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
        if keys_pressed[K_s] and self.rect.y < 695:
            self.rect.y += self.speed

    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 695:
            self.rect.y += self.speed


pong1 = Player('pong.png',10 ,10,100,100,10)            
pong2 = Player('pong.png',100 ,100,100,100,10)            
color1 = (255, 255, 255)
game = True
clock=time.Clock()
FPS = 60
window = display.set_mode((500, 500))

window.fill(color1)





while game:
    window.fill(color1)    
    pong1.update_left()
    pong2.update_right()
    pong1.reset()
    pong2.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)     