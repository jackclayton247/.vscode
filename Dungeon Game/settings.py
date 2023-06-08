#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TWY-6451
#
# Created:     25/05/2023
# Copyright:   (c) TWY-6451 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#player setting
PLAYER_SPEED = 500
