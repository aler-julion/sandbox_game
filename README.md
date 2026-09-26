# Sandbox Game

Projeto pessoal de estudo para desenvolvimento de um jogo voxel em Python utilizando a Ursina Engine.

O objetivo inicial é explorar os principais recursos da engine enquanto construo progressivamente sistemas comuns em jogos baseados em voxels.

## Objetivos

- Aprender a arquitetura e os recursos da Ursina Engine
- Implementar um mundo baseado em voxels
- Trabalhar com interação, colisão e raycasting
- Organizar o projeto em módulos e classes
- Evoluir a estrutura conforme novas funcionalidades forem adicionadas

## Funcionalidades atuais

- Controle em primeira pessoa
- Mundo baseado em blocos
- Geração de plataforma inicial
- Adição de blocos
- Remoção de blocos
- Raycast para seleção de blocos
- Respawn ao cair do mapa
- HUD de debug
- Exibição da posição atual do jogador
- Exibição da posição do bloco observado

## Estrutura do projeto

```text
sandbox_game/
├── core/
│   ├── __init__.py
│   └── game.py
│
├── player/
│   ├── __init__.py
│   └── player.py
│
├── ui/
│   ├── __init__.py
│   └── debug_hud.py
│
├── world/
│   ├── __init__.py
│   ├── floor.py
│   ├── voxel.py
│   └── world.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Tecnologias

- Python
- Ursina Engine
- Panda3D

## Executando o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/aler-julion/sandbox_game.git
```

Entre na pasta do projeto:

```bash
cd sandbox_game
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Windows CMD:

```cmd
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute o jogo

```bash
python main.py
```

## Controles

| Ação | Controle |
|---|---|
| Movimento | W, A, S, D |
| Olhar | Mouse |
| Pular | Espaço |
| Adicionar bloco | Botão esquerdo do mouse |
| Remover bloco | Botão direito do mouse |
| Sair | ESC |

## Arquitetura atual

O projeto está dividido por responsabilidade.

### `player`

Responsável pelo jogador e pelo controle em primeira pessoa.

Atualmente inclui:

- movimentação
- gravidade
- câmera
- mira
- respawn

### `world`

Responsável pelo mundo baseado em voxels.

Atualmente inclui:

- criação de blocos
- remoção de blocos
- armazenamento dos blocos
- raycast para detectar o bloco observado
- geração do chão

### `ui`

Responsável pelos elementos de interface.

Atualmente exibe:

- posição X, Y e Z do jogador
- posição do bloco observado

### `core`

Responsável por comportamentos gerais da aplicação.

Atualmente inclui:

- encerramento do jogo

## Próximos passos

Algumas funcionalidades planejadas:

- Diferentes tipos de blocos
- Cores e texturas por tipo de bloco
- Seleção de bloco
- Inventário
- Geração procedural de terreno
- Chunks
- Sistema de save e load
- Otimização do mundo voxel
- Melhorias na interface

## Status

Em desenvolvimento.

Este projeto é utilizado como sandbox de aprendizado para exploração de desenvolvimento de jogos voxel, arquitetura de software e recursos da Ursina Engine.