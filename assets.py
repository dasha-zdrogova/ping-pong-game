import os
import pygame.image

sprites = {}


def load_sprites():
    script_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(script_path, "assets", "sprites")
    for file_name in os.listdir(path):
        sprites[file_name.split(".")[0]] = pygame.image.load(
            os.path.join(path, file_name)
        )


def get_sprite(name):
    return sprites[name]
