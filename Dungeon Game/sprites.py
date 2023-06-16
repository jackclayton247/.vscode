#sprites

import pygame as pg
from settings import *
import math
from os import path
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):    #sprite image
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE

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

    def collide_with_walls_player(self, dir):
        if dir == "x":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0: #check direction of collision and stops that movement
                    self.pos.x = hits[0].rect.left - self.rect.width
                    self.game.gun.pos.x = self.pos.x + 64
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                    self.game.gun.pos.x = self.pos.x + 64
            self.vel.x = 0
            self.rect.x = self.pos.x
        if dir == "y":
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:  #check direction of collision and stops that movement
                    self.pos.y = hits[0].rect.top - self.rect.height
                    self.game.gun.pos.y = self.pos.y + 64
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                    self.game.gun.pos.y = self.pos.y + 64
            self.vel.y = 0
            self.rect.y = self.pos.y

    def update(self): #calls all the functions
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x =self.pos.x
        self.collide_with_walls_player("x")
        self.rect.y =self.pos.y
        self.collide_with_walls_player("y")

class Gun(pg.sprite.Sprite): #weapon image
    def __init__(self, game, x, y):
        self.pos = vec(x+1, y+1.2) * TILESIZE
        self.groups = game.all_sprites,
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.gun_img
        self.base_gun_image = self.image
        self.hitbox_rect = self.base_gun_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.coord = vec(0,0)
        print(self.pos)

    def gun_rotation(self): #roates the gun sprite to point the cursor
        self.mouse_coords = pg.mouse.get_pos()
        self.x_change_mouse_gun = (self.mouse_coords[0] - self.hitbox_rect.centerx)
        self.y_change_mouse_gun = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_gun, self.x_change_mouse_gun))
        self.image = pg.transform.rotate(self.base_gun_image, -self.angle)
        self.rect = self.image.get_rect(center = self.hitbox_rect.center)

    def get_keys(self):
        self.coord = vec(0, 0)   #catches movement events
        keys =pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.coord.x = -PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.coord.x = PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.coord.y = -PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.coord.y = PLAYER_SPEED
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center
        if self.coord.x != 0 and self.coord.y != 0:
            self.coord *= 0.7071

    def update(self):  #calls all the functions
        #self.get_keys()
        self.gun_rotation()
        #self.pos += self.coord * self.game.dt
        #self.rect.x =self.pos.x
        #self.rect.y =self.pos.y


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
