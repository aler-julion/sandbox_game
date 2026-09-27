from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class BlockType:
    """Define as propriedades de um tipo de bloco"""

    id: str
    name: str
    texture: str
    