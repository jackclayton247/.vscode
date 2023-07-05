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
CYAN = (0, 255, 255)

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
PLAYER_SPEED = 300
PLAYER_IMG = "player.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 70, 110)
PLAYER_LIVES = 6
HEART_IMG = "heart.png"
HALF_HEART_IMG = "half heart.png"
I_FRAMES = 300
PLAYER_CENTER = [550, 450]

#gun settings
GUN_IMG = "gun.png"
GUN_HIT_RECT = pg.Rect(0, 0, 0, 0)
#bullet settings
BULLET_IMG = "bullet.png"
BARREL_OFFSET = vec(10, 10)
BULLET_SPEED = 20
BULLET_LIFETIME = 100000
BULLET_RATE = 200
KICKBACK = 0
GUN_SPREAD = 5
BULLET_DAMAGE = 10
#mob settings
MOB_IMG = "mob.png"
MOB_SPEED = 100
MOB_HIT_RECT = pg.Rect(0, 0, 60, 110)
MOB_HEALTH = 100
MOB_DAMAGE = 5
