import pygame
import os
from ecran import *

pygame.init()

# Charger l'image du personnage
image_personnage = os.path.dirname(__file__)
personnage_image = os.path.join(image_personnage, "img", "personnage.png")
personnage_image = pygame.image.load(personnage_image)
taille_personnage = (160, 160)
personnage_image = pygame.transform.scale(personnage_image, taille_personnage)

personnage_rect = personnage_image.get_rect()

# Définir la vitesse du personnage
vitesse = 3

# Initialisez les coordonnées du personnage au centre de la fenêtre
personnage_rect.center = (largeur // 2, hauteur // 2)