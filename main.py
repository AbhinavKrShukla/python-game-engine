import pygame
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
import pyautogui


class GraphicsEngine:

	def __init__(self, win_size = (1920, 1080)):		# 1366, 768
		# init pygame module
		pygame.init()
		# win_info = pygame.display.Info()
		# win_size = (win_info.current_w, win_info.current_h)
		# print(win_size)
		# exit(0)

		# window size
		# self.WIN_SIZE = win_size
		self.WIN_SIZE = pyautogui.size()
		# print(self.WIN_SIZE[0], self.WIN_SIZE[1])
		# WIN_LIST = [1366, 768,]
		# set opengl context
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
		# mouse settings
		pygame.event.set_grab(True)
		pygame.mouse.set_visible(False)
		# create opengl context
		pygame.display.set_mode(self.WIN_SIZE, flags=pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
		# detect and use existing opengl context
		self.ctx = mgl.create_context()
		self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
		# create an object to help track time
		self.clock = pygame.time.Clock()
		self.time = 0
		self.delta_time = 0
		# light
		self.light = Light()
		# camera
		self.camera = Camera(self)
		# mesh
		self.mesh = Mesh(self)
		# scene
		self.scene = Scene(self)

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				self.mesh.destroy()
				pygame.quit()
				sys.exit()

		

	def render(self):
		# clear framebuffer
		self.ctx.clear(color=(0, 0.16, 0.18))
		# render scene
		self.scene.render()
		# swap buffers
		pygame.display.flip()

	def get_time(self):
		self.time = pygame.time.get_ticks() * 0.001

	def run(self):
		
		while True:
			self.get_time()
			self.check_events()
			self.camera.update()
			self.light.pos_update()
			self.render()
			self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
	app = GraphicsEngine()
	app.run()