# -*- coding: Utf-8 -*
import pygame
from pygame.locals import *

from classes import *
from constantes import *
from game import *

pygame.init()

game = Game(18, 15)
game.run()
