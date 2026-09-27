from .block_type import BlockType


GRASS = BlockType(
    id="grass",
    name="Grass",
    texture="white_cube" # Por enquantos textures brancas, sem assets externos
)

DIRT = BlockType(
    id="dirt",
    name="Dirt",
    texture="white_cube" # Por enquantos textures brancas, sem assets externos
)

STONE = BlockType(
    id="stone",
    name="Stone",
    texture="white_cube" # Por enquantos textures brancas, sem assets externos
)

BLOCKS = {
    GRASS.id: GRASS,
    DIRT.id: DIRT,
    STONE.id: STONE,
}