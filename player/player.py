from ursina import color
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    """Controla o jogador em primeira pessoa"""

    def __init__(
        self, 
        position=(10, 2, 10),
        respawn_height=-30,
    ):
        super().__init__(
            position=position,
            speed=5,
        )


        # Guarda a posição inicial
        self.spawn_position = position

        # Alterura limite para considerar na queda
        self.respawn_height = respawn_height

        
        # Configura a mira.
        #self.cursor.color = color.light_gray
        self.cursor.scale = 0.012

    def update(self):
        """Atualiza o jogador e verifica se caiu do mapa"""

        # Manter o movimento e a gravidade do controller original
        super().update()

        if self.y < self.respawn_height:
            self.respawn()

    def respawn(self):
        """Respawna o jogador ao ponto inicial"""

        self.position = self.spawn_position
        self.air_time = 0
        self.grounded = False