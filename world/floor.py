class Floor:
    """Gera o chao no mundo"""

    def __init__(
        self,
        world,
        width=40,
        depth=40,
        height=0,
    ):
        self.world = world
        self.width = width
        self.depth = depth
        self.height = height

    def generate(self):
        """Cria os blocos do chao"""

        for z in range(self.depth):
            for x in range(self.width):

                self.world.add_block(
                    (
                        x,
                        self.height,
                        z,
                    )
                )
            