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
PLAYER_SPEED = 400
PLAYER_IMG = "test2.png"
GUN_IMG = "gun.png"
BULLET_IMG = "bullet.png"

BARREL_OFFSET = vec(1000, 1000)
BULLET_SPEED = 6
BULLET_LIFETIME = 1000000
BULLET_RATE = 150
KICKBACK = 0

