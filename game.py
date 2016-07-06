# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from constantes import *
from classes import *

class Game:
	def __init__(self, map_width, map_height):
		self.map = Map(map_width, map_height)

		# Initialisation (pygame, fenetre etc..)
		self.window = pygame.display.set_mode((map_width * sprite_width, map_height * sprite_height), RESIZABLE)
		icone = pygame.image.load(image_icone)
		pygame.display.set_icon(icone)
		pygame.display.set_caption(titre_fenetre)

		self.state = TitleScreenState()
		self.clearColor = pygame.Surface(self.window.get_size())
		color = 255, 255, 255
		self.clearColor.fill(color)

	def run(self):
		self.continuer = True
		while(self.continuer):
			pygame.time.Clock().tick(60)

			self.state.handleInput(self)
			self.state.update(self)

			self.clearWindow()
			self.state.render(self)
			pygame.display.flip()

	def clearWindow(self):
		self.window.blit(self.clearColor, (0,0))

class GameState:
	def handleInput(self, game):
		pass
	def update(self, game):
		pass
	def render(self, game):
		pass

class TitleScreenState(GameState):
	def __init__(self):
		self.background = pygame.image.load(image_accueil).convert()

	def handleInput(self, game):
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				game.continuer = False

			elif event.type == KEYDOWN and event.key == K_F1:
				game.state = PlayingState()

	def update(self, game):
		pass

	def render(self, game):
		game.window.blit(self.background, (0,0))

class PlayingState(GameState):
	def __init__(self):
		self.cursor = Curseur(image_curseur)
		self.level = Niveau('Maps/n1')
		self.level.generer()
		self.currentPlayer = 0

	def handleInput(self, game):
		for event in pygame.event.get():
			if event.type == QUIT:
				game.continuer = False
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				game.state = TitleScreenState()
			elif event.type == KEYDOWN and event.key == K_e:
				self.currentPlayer = (self.currentPlayer + 1) % player_number
				print(self.currentPlayer)

	def update(self, game):
		pos = pygame.mouse.get_pos()
		self.cursor.AlignOnTopLeft(pos)

	def render(self, game):
		self.level.afficher(game.window)
		game.window.blit(self.cursor.image, (self.cursor.x, self.cursor.y))

class Curseur:
	"""Classe permettant de définir un curseur"""
	def __init__(self, image):
		self.image = pygame.image.load(image).convert_alpha()
		self.x = 0
		self.y = 0

	def AlignOnTopLeft(self, pos):
		self.x = int(pos[0] / sprite_width) * sprite_width
	 	self.y = int(pos[1] / sprite_height) * sprite_height
