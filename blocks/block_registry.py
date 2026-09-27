from .block_type import BlockType


GRASS = BlockType(
    id="grass",
    name="Grass",
    texture="grass" # Por enquantos textures brancas, sem assets externos
)

DIRT = BlockType(
    id="dirt",
    name="Dirt",
    texture="dirt" # Por enquantos textures brancas, sem assets externos
)

STONE = BlockType(
    id="stone",
    name="Stone",
    texture="stone" # Por enquantos textures brancas, sem assets externos
)

BLOCKS = {
    GRASS.id: GRASS,
    DIRT.id: DIRT,
    STONE.id: STONE,
}