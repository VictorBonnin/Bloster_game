import pygame
import os

from ecran import *

pygame.init()

pygame.mixer.init()

fichiers_audio = os.path.dirname(__file__)

# -------------------------------------------------
# Musique d'ambiance
chemin_audio = os.path.join(fichiers_audio, "Audio", "Legendary ahh sound.mp3")
pygame.mixer.music.load(chemin_audio)
pygame.mixer.music.play(-1)
volume_musique = 0.2
pygame.mixer.music.set_volume(volume_musique)

# -------------------------------------------------
# Musique menus
click_sound_path = os.path.join(fichiers_audio, "Audio", "menusound1.wav")
click_sound = pygame.mixer.Sound(click_sound_path)
volume_menu = 0.2
click_sound.set_volume(volume_menu)

# -------------------------------------------------
# Musique collisions
collision_sound_path = os.path.join(fichiers_audio, "Audio", "auaua.wav")
collision_sound = pygame.mixer.Sound(collision_sound_path)
volume_collision = 0.1
collision_sound.set_volume(volume_collision)