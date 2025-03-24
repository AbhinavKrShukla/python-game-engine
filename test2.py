import struct
import moderngl
import numpy as np
from PIL import Image

# Create a ModernGL context
ctx = moderngl.create_context(standalone=True)

# Vertex and fragment shaders
vertex_shader = """
#version 330
in vec2 in_vert;
void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
}
"""

fragment_shader = """
#version 330
out vec4 fragColor;
void main() {
    fragColor = vec4(1.0, 1.0, 0.0, 1.0);  // Red color
}
"""

# Create a shader program
program = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

# Define the vertices of a triangle
vertices = np.array([
    -0.6, -0.6,
    0.6, -0.6,
    0.0, 0.6,
], dtype='f4')

# Create a vertex buffer
vbo = ctx.buffer(vertices.tobytes())

# Create a vertex array
vao = ctx.simple_vertex_array(program, vbo, 'in_vert')

# Create a framebuffer to render to
fbo = ctx.framebuffer(color_attachments=[ctx.renderbuffer((800, 600))])

# Bind the framebuffer and clear the screen
fbo.use()
ctx.clear()

# Render the triangle
vao.render(moderngl.TRIANGLES)

# Read the pixel data from the framebuffer
pixels = fbo.read(components=3, dtype='f1')

# Convert pixel data to an image using PIL
image = Image.frombytes('RGB', fbo.size, pixels)

# Display the image
image.show()
