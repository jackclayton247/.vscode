#settings
import pygame as pg
import math
vec = pg.math.Vector2

#colour bank
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#game settings
WIDTH = 1024    # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768    # 16 * 48 or 32 * 24 or 64 * 12
FPS = 120
TITLE = "Dungeon Crawler"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#player setting
PLAYER_SPEED = 500
PLAYER_IMG = "test2.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
#gun settings
GUN_IMG = "gun.png"
#bullet settings
BULLET_IMG = "bullet.png"
BARREL_OFFSET = vec(30, 10)
BULLET_SPEED = 20
BULLET_LIFETIME = 100000
BULLET_RATE = 0.1
KICKBACK = 200
GUN_SPREAD = 5
#mob settings
MOB_IMG = "mob.png"
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
