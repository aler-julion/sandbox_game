import random
from ursina import Button, color, scene

class Voxel(Button):
    """Representa um bloco do mundo"""
    
    def __init__(self, position=(0, 0, 0), parent=scene):
        super().__init__(
            parent=parent,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="white_cube",
            color=color.hsv(
                0,
                0,
                random.uniform(0.9, 1),
            ),
            highlight_color=color.lime,
            collider="box",
        )

        # Guarda a posição lógica do bloco.
        self.grid_position = tuple(
            round(value) for value in position
        )