# test
import pywavefront
import numpy as np


objs = pywavefront.Wavefront('objects/farari_1/farari_obj.obj', cache=True, parse=True)
obj = objs.materials.popitem()[1]
vertex_data = obj.vertices
vertex_data = np.array(vertex_data, dtype='f4')
print(type(vertex_data))
# g


from PIL import Image