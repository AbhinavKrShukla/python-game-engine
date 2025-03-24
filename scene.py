from model import *
from random import randint as r


class Scene:
	def __init__(self, app):
		self.app = app
		self.objects = []
		self.load()
		

	def add_objects(self, obj):
		self.objects.append(obj)

	def load(self):
		app = self.app
		add = self.add_objects

		'''
		add(Cube(app))
		add(Cube(app, tex_id=1, pos=(-2.5, 0, 0), rot=(45, 0, 0), scale=(1, 2, 1)))
		add(Cube(app, tex_id=2, pos=(2.5, 0, 0), rot=(0, 0, 45), scale=(1, 1, 2)))
		'''
		n, s = 100, 2
		for x in range(-n, n, s):
			for z in range(-n, n, s):
				tex = r(0, 2)
				add(Cube(app, pos=(x, -s, z), tex_id=tex))

		add(Cat(app, pos=(0, 5, -10), rot=(-90, 0, 0)))
		# add(Farari(app, pos=(25, 3, -10)))




	def render(self):
		for obj in self.objects:
			obj.render()