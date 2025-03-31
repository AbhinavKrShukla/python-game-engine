import glm
import pygame

FOV = 50 # deg
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05


class Camera:
	def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):
		self.app = app
		self.aspect_ratio = app.WIN_SIZE[0]/app.WIN_SIZE[1]
		self.position = glm.vec3(position)
		self.up = glm.vec3(0, 1, 0)
		self.right = glm.vec3(1, 0, 0)
		self.forward = glm.vec3(0, 0, -1)
		# for rotation
		self.yaw = yaw
		self.pitch = pitch
		# view matrix
		self.m_view = self.get_view_matrix()
		# projection matrix
		self.m_proj = self.get_projection_matrix()

	def rotate(self):
		rel_x, rel_y = pygame.mouse.get_rel()
		self.yaw += rel_x * SENSITIVITY
		self.pitch -= rel_y * SENSITIVITY
		self.pitch = max(-89, min(89, self.pitch))

		if rel_x != 0 or rel_y != 0:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if mouse_x <= 0 or mouse_x >= self.app.WIN_SIZE[0] - 1 or mouse_y <= 0 or mouse_y >= self.app.WIN_SIZE[1] - 1:
				# Reset the cursor position to the center of the window
				pygame.mouse.set_pos((self.app.WIN_SIZE[0]//2, self.app.WIN_SIZE[1]//2))


	def update_camera_vectors(self):
		yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
		self.forward.x = glm.cos(yaw) * glm.cos(pitch)
		self.forward.y = glm.sin(pitch)
		self.forward.z = glm.sin(yaw) * glm.cos(pitch)

		self.forward = glm.normalize(self.forward)
		self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
		self.up = glm.normalize(glm.cross(self.right, self.forward))

	def update(self):
		self.move()
		self.rotate()
		self.update_camera_vectors()
		self.m_view = self.get_view_matrix()

	def move(self):
		velocity = SPEED * self.app.delta_time
		keys = pygame.key.get_pressed()

		# speed up if space is pressed
		if keys[pygame.K_SPACE]: velocity *= 3

		if keys[pygame.K_w]: self.position += self.forward * velocity
		if keys[pygame.K_s]: self.position -= self.forward * velocity
		if keys[pygame.K_d]: self.position += self.right * velocity
		if keys[pygame.K_a]: self.position -= self.right * velocity
		if keys[pygame.K_q]: self.position += self.up * velocity
		if keys[pygame.K_e]: self.position -= self.up * velocity

		# cat movement
		#if keys[pygame.K_UP]: self.app.



	def get_view_matrix(self):
		# uses glm.lookAt(eye, center, up) -> glm.mat4
		# eye - pos of cam
		# center - pos where cam is looking at (here the center of screen at 0, 0, 0)
		# up - normalised up vec, how cam is oriented ( what dir should be the top and bottom)
		# return glm.lookAt( self.position, glm.vec3(0), glm.vec3(0, 1, 0) )
		return glm.lookAt( self.position, self.position + self.forward, glm.vec3(0, 1, 0) )

	def get_projection_matrix(self):
		return glm.perspective( glm.radians(FOV), self.aspect_ratio, NEAR, FAR )
		