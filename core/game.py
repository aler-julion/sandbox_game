from ursina import Entity, application

class Game(Entity):
    """Controla eventos gerais no jogo"""

    def input (self, key):

        if key == "escape":
            application.quit()