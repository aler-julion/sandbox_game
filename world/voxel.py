from ursina import Button, color, scene
from blocks.block_type import BlockType

class Voxel(Button):
    """Representa um bloco do mundo"""
    
    def __init__(
        self,
        position,
        block_type: BlockType,
        parent=scene,
    ):
        self.block_type = block_type
        
        super().__init__(
            parent=parent,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="block_type.texture",
            color=color.white,
            highlight_color=color.lime,
            collider="box",
        )

        # Guarda a posição lógica do bloco.
        self.grid_position = tuple(
            round(value) for value in position
        )