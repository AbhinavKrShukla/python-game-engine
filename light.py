import glm
from random import randint as r


class Light:
	def __init__(self, position=(3, 3, -3), color=(1, 1, 1)):
		self.position = glm.vec3(position)
		self.color = glm.vec3(color)
		# intensities
		self.Ia = 0.1 * self.color	# ambient
		self.Id = 0.8 * self.color	# diffused
		self.Is = 1.0 * self.color	# specular



	def pos_update(self):
		self.position = glm.vec3(*[r(-5, 5) for i in range(3)])
		self.color = glm.vec3(*[r(0, 1) for i in  range(3)])
		# self.position = new_position

