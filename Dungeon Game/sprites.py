#sprites

import pygame as pg
from settings import *
from tilemap import *
import math
from os import path
vec = pg.math.Vector2
from random import uniform

def collide_with_walls(sprite, group, dir): #main function for wall collision
        if dir == 'x':
            hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
            if hits:
                if sprite.vel.x > 0:
                    sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
                if sprite.vel.x < 0:
                    sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
                sprite.vel.x = 0
                sprite.hit_rect.centerx = sprite.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
            if hits:
                if sprite.vel.y > 0:
                    sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
                if sprite.vel.y < 0:
                    sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
                sprite.vel.y = 0
                sprite.hit_rect.centery = sprite.pos.y

def sprite_animation():
    pass

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, sprite):    #sprite image
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()  #hitbox
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)    #position
        self.last_shot = 0
        self.lives = PLAYER_LIVES
        self.last_hit = 0
    def get_keys(self):
        self.vel = vec(0, 0)   #catches movement events
        keys =pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
    
    def update(self): #calls all the functions
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        self.get_keys()

    

class Gun(pg.sprite.Sprite): #weapon image
    def __init__(self, game, x, y):
        self.pos = vec(x+0.7, y+1.2) * TILESIZE
        self.groups = game.all_sprites,
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.gun_img
        self.base_gun_image = self.image
        self.hitbox_rect = self.base_gun_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.hit_rect = GUN_HIT_RECT #hitbox
        self.vel = vec(0,0)
        self.offset = vec(80, 0)
        self.last_shot = 0
        self.rot = 0
        self.flipped = False  #tracks state


    def gun_rotation(self): #roates the gun sprite to point the cursor
        self.player_offset = False
        if self.player_offset == True:
            self.mouse_coords = pg.mouse.get_pos()
        else:
            self.mouse_coords = self.pos - PLAYER_CENTER + pg.mouse.get_pos()
        print(self.player_offset)
        self.x_change_mouse_gun = (self.mouse_coords[0] - self.hitbox_rect.centerx)
        self.y_change_mouse_gun = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_gun, self.x_change_mouse_gun))
        self.image = pg.transform.rotate(self.base_gun_image, -self.angle)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center = self.pos + offset_rotated)
        self.pos = self.game.player.pos
        if (-180 <= self.angle < -90 or 90 <= self.angle < 180) and not self.flipped:
            self.base_gun_image = pg.transform.flip(self.base_gun_image, False, True)
            self.flipped = True  #sets the flipped state to true
        elif -90 <= self.angle < 90 and self.flipped:
            self.base_gun_image = pg.transform.flip(self.base_gun_image, False, True)
            self.flipped = False  #sets the flipped state to false

    def get_keys(self):
        self.vel = vec(0, 0)   #catches movement events
        keys =pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
        if keys[pg.K_SPACE]: #shoots
            now = pg.time.get_ticks()
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game, pos, dir)
                self.vel = vec(-KICKBACK, 0).rotate(-self.rot)


    def update(self):  #calls all the functions
        self.get_keys()
        self.gun_rotation()
        self.pos += self.vel * self.game.dt

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img #sprite image
        self.rect = self.image.get_rect()
        magnitude = math.sqrt(self.game.gun.x_change_mouse_gun **2 + self.game.gun.y_change_mouse_gun **2)  #for unit vector calc
        self.pos = [self.game.gun.x_change_mouse_gun / magnitude * 100, self.game.gun.y_change_mouse_gun / magnitude * 100] + self.game.gun.pos  #spawn the bullet based on the gun pos and a factor of the unit vector
        self.rect.center = pos #center
        self.vel = [self.game.gun.x_change_mouse_gun / magnitude * BULLET_SPEED, self.game.gun.y_change_mouse_gun / magnitude * BULLET_SPEED]
        self.spawn_time = pg.time.get_ticks()
        self.base_bullet_image = self.image
        self.image = pg.transform.rotate(self.base_bullet_image, -self.game.gun.angle)  #rotate based on function in gun class
        self.rect = self.image.get_rect(center = self.pos)
        self.hit_rect = self.rect

    def update(self): #calls all funtions
        self.pos += (self.vel)
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BULLET_LIFETIME:
            self.kill()

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img # sprite image
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy() #hitbox
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)  #postion
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = MOB_HEALTH

    def update(self): #calls funtion
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = self.game.mob_img
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(MOB_SPEED, 0).rotate(-self.rot)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x              
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        if self.health <= 0:
            self.kill()

    def draw_health(self):
        health_surface = pg.Surface((self.rect.width, 7))  # Create a new surface for the health bar
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / MOB_HEALTH)
        health_bar = pg.Rect(0, 0, width, 7)
        empty_bar = pg.Rect(width, 0, self.rect.width - width, 7)
        pg.draw.rect(health_surface, col, health_bar)  # Draw the health bar on the health surface
        pg.draw.rect(health_surface, BLACK, empty_bar)
        self.image.blit(health_surface, (0, 0))  # Blit the health surface onto the sprite's image
            

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):   #sprite image
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
