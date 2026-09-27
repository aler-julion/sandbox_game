from ursina import Entity, Text, camera


class DebugHUD(Entity):
    """Exibe informações de posição na tela."""

    def __init__(self, player, world):
        super().__init__()

        self.player = player
        self.world = world

        # Texto no canto superior esquerdo.
        self.text = Text(
            parent=camera.ui,
            text="",
            x=-0.87,
            y=0.46,
            origin=(-0.5, 0.5),
            scale=0.9,
        )

    def update(self):
        """Atualiza as informações exibidas."""

        player_position = self.player.position
        targeted_block = self.world.get_targeted_block()

        # Posição atual do jogador.
        player_info = (
            f"Posicao: "
            f"X: {player_position.x:.2f} | "
            f"Y: {player_position.y:.2f} | "
            f"Z: {player_position.z:.2f}"
        )

        # Posição do bloco observado.
        if targeted_block:
            block_position = targeted_block.entity.grid_position
            block_type = targeted_block.entity.block_type

            block_info = (
                f"Bloco: {block_type.name} | "
                f"X: {block_position[0]} | "
                f"Y: {block_position[1]} | "
                f"Z: {block_position[2]}"
            )

        else:
            block_info = "Bloco: Nenhum"

        self.text.text = (
            f"{player_info}\n"
            f"{block_info}"
        )