import pygame
import moderngl as mgl

my_textures = ['wooden_crate.jpg' , 'metallic_crate.jpg', 'metallic_crate_2.jpg']

class Texture:
	def __init__(self, ctx):
		self.ctx = ctx
		self.textures = {}
		self.textures['none'] = self.get_Texture(path='textures/def.png')

		for i in range(len(my_textures)):
			# self.textures[i] = self.get_Texture(path='textures/{0}'.format(my_textures[i]))
			self.textures[i] = self.get_Texture(path=f'textures/{my_textures[i]}')

		# cat texture
		self.textures['cat'] = self.get_Texture(path='objects/cat/20430_cat_diff_v1.jpg')
		'''
		self.textures[0] = self.get_Texture(path='textures/wooden_crate.jpg')
		self.textures[1] = self.get_Texture(path='textures/t1.jfif')
		self.textures[2] = self.get_Texture(path='textures/wooden_crate.jpg')
		'''
	def get_Texture(self, path):
		texture = pygame.image.load(path).convert()
		texture = pygame.transform.flip(texture, flip_x=False, flip_y=True)			
		texture = self.ctx.texture(size=texture.get_size(), components=3,
								data=pygame.image.tostring(texture, 'RGB'))
		# mipmaps
		texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
		texture.build_mipmaps()
		# AF
		texture.anisotropy = 32.0
		return texture

	def destroy(self):
		[tex.release() for tex in self.textures.values()]
