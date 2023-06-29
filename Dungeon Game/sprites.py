#sprites

import pygame as pg
from settings import *
import math
from os import path
vec = pg.math.Vector2
from random import uniform

def collide_with_walls(self, group, dir):
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

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):    #sprite image
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
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

    def update(self): #calls all the functions
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

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
        self.coord = vec(0,0)
        self.offset = vec(80, 0)
        self.last_shot = 0
        self.rot = 0


    def gun_rotation(self): #roates the gun sprite to point the cursor
        self.mouse_coords = self.pos - [549.5, 441.5] + pg.mouse.get_pos()
        self.x_change_mouse_gun = (self.mouse_coords[0] - self.hitbox_rect.centerx)
        self.y_change_mouse_gun = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_gun, self.x_change_mouse_gun))
        self.image = pg.transform.rotate(self.base_gun_image, -self.angle)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center = self.pos+offset_rotated)

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
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game, pos, dir)
                self.vel = vec(-KICKBACK, 0).rotate(-self.rot)

    def update(self):  #calls all the functions + jack smells
        self.get_keys()
        self.gun_rotation()
        self.pos += self.coord * self.game.dt

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        magnitude = math.sqrt(self.game.gun.x_change_mouse_gun **2 + self.game.gun.y_change_mouse_gun **2)
        self.pos = [self.game.gun.x_change_mouse_gun / magnitude * 100, self.game.gun.y_change_mouse_gun / magnitude * 100] + self.game.gun.pos
        self.rect.center = pos
        self.vel = [self.game.gun.x_change_mouse_gun / magnitude * BULLET_SPEED, self.game.gun.y_change_mouse_gun / magnitude * BULLET_SPEED]
        self.spawn_time = pg.time.get_ticks()
        self.base_bullet_image = self.image
        self.image = pg.transform.rotate(self.base_bullet_image, -self.game.gun.angle)
        self.rect = self.image.get_rect(center = self.pos)

    def update(self):
        self.pos += (self.vel)
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BULLET_LIFETIME:
            self.kill()
            print(self.game.gun.angle)

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)
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

