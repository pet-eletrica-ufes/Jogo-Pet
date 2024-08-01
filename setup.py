import os
import sys
from cx_Freeze import setup, Executable

# Encontra o caminho das DLLs do Python
dll_path = os.path.join(sys.prefix, 'DLLs')

# Adiciona caminhos de busca para as DLLs necessárias
include_files = [(dll_path, "DLLs")]

# Adiciona os diretórios de sprites e texto
sprite_directories = [
    ("Sprites/Pixel Adventure 1/Free/Main Characters/Mask Dude", "Sprites/Pixel Adventure 1/Free/Main Characters/Mask Dude"),
    ("Sprites/Pixel Adventure 1/Free/Main Characters/Ninja Frog", "Sprites/Pixel Adventure 1/Free/Main Characters/Ninja Frog"),
    ("Sprites/Pixel Adventure 1/Free/Main Characters/Pink Man", "Sprites/Pixel Adventure 1/Free/Main Characters/Pink Man"),
    ("Sprites/Pixel Adventure 1/Free/Main Characters/Virtual Guy", "Sprites/Pixel Adventure 1/Free/Main Characters/Virtual Guy"),
    ("Sprites/Pixel Adventure 1/Free/Menu/Text", "Sprites/Pixel Adventure 1/Free/Menu/Text")
]

include_files.extend(sprite_directories)

# Dependências adicionais
build_exe_options = {"packages": ["pygame"], "include_files": include_files}

# Configurações do executável
executables = [Executable("teste_pygame.py", base="Win32GUI")]

setup(
    name="Exemplo PyGame",
    version="1.0",
    description="Exemplo simples usando Pygame",
    options={"build_exe": build_exe_options},
    executables=executables
)