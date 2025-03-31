# Python - 3D Graphics Engine

## Description
This project is a 3D graphics engine built using Python, ModernGL, and Pygame. It is designed to render 3D models and scenes with lighting and camera controls.

## Installation
1. Ensure you have Python installed on your system.
2. Install the required packages using pip:
   ```
   pip install pygame moderngl numpy PyOpenGL
   ```

## Usage
Run the main script to start the graphics engine:
```bash
python main.py
```

## Features
- **GraphicsEngine**: Initializes the graphics context and manages the rendering loop.
- **Camera**: Handles camera movement and perspective projection.
- **Models**: Includes base models and specific models like Cube and Cat for rendering.

## Modules Overview
- **main.py**: Entry point of the application, initializes the `GraphicsEngine`.
- **camera.py**: Contains the `Camera` class for handling view and projection matrices.
- **model.py**: Defines the `BaseModel` class and specific models like `Cube`.

## Dependencies
- Python
- Pygame
- ModernGL
- Numpy
- PyOpenGL

## Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
