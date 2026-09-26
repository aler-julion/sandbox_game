from ursina import Entity, camera, destroy, raycast

from .voxel import Voxel


class World(Entity):
    """Gerencia os blocos e interações do mundo."""

    def __init__(self, player, interaction_distance=5):
        super().__init__()

        self.player = player
        self.interaction_distance = interaction_distance

        # Armazena os blocos existentes no mundo.
        self.blocks = {}

    def add_block(self, position):
        """Adiciona um bloco na posição informada."""

        position = self.to_grid(position)

        # Impede dois blocos na mesma posição.
        if position in self.blocks:
            return

        voxel = Voxel(
            position=position,
            parent=self,
        )

        self.blocks[position] = voxel

    def remove_block(self, voxel):
        """Remove um bloco do mundo."""

        if not isinstance(voxel, Voxel):
            return

        position = voxel.grid_position

        self.blocks.pop(position, None)

        destroy(voxel)

    def get_targeted_block(self):
        """Retorna o bloco que o jogador esta observando"""

        hit = raycast(
            origin=camera.world_position,
            direction=camera.forward,
            distance=self.interaction_distance,
            ignore=[self.player],
            )

        if hit.hit and isinstance(hit.entity, Voxel):
            return hit

        return None

    def input(self, key):
        """Processa a interação do jogador com os blocos."""

        if key not in ("left mouse down", "right mouse down"):
            return

        # Busca o bloco que esta sendo observado pelo jogador.
        hit = self.get_targeted_block()

        if hit is None:
            return

        # Botão esquerdo adiciona um bloco.
        if key == "left mouse down":
            position = hit.entity.position + hit.normal
            self.add_block(position)

        # Botão direito remove o bloco.
        elif key == "right mouse down":
            self.remove_block(hit.entity)

    @staticmethod
    def to_grid(position):
        """Converte uma posição para coordenadas inteiras."""

        return tuple(round(value) for value in position)