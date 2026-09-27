from ursina import Texture, Ursina, load_texture

from core.game import Game
from player.player import Player
from world.floor import Floor
from world.world import World
from ui.debug_hud import DebugHUD

# Mantém as texturas pixeladas sem suavização
Texture.default_filtering = None

# Inicializa o jogo
app = Ursina()

# Teste temporário das texturas.
print("GRASS:", load_texture("grass"))
print("DIRT:", load_texture("dirt"))
print("STONE:", load_texture("stone"))

# Cria o jogador
player = Player(
    position=(10, 2, 10),
    respawn_height=-30,
)

# Cria o mundo
world = World(
    player=player
)

# Cria o chao
floor = Floor(
    world=world,
    width=20,
    depth=20,
)

floor.generate()

# Cria o HUD de debug
debug_hud = DebugHUD(
    player=player,
    world=world,
)

# Eventos gerais do jogo
game = Game()

# Inicia o jogo
app.run()
