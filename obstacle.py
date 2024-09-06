import pygame 
import random
import os
from personnage import *
from audio import *

pygame.init()

images_obstacles = os.path.dirname(__file__)

# Classe pour les obstacles
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_obstacle1 = os.path.join(images_obstacles, "img", "asteroide_1.png")
        self.image = pygame.image.load(image_obstacle1)
        self.image = pygame.transform.scale(self.image, (largeur_ecran // 22, hauteur_ecran // 22)) 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largeur - self.rect.width)
        self.rect.y = random.randint(0, hauteur - self.rect.height)
        self.vitesse_x = random.randint(1, 4)
        self.vitesse_y = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.vitesse_x
        self.rect.y += self.vitesse_y

        if self.rect.left > largeur:
            self.rect.right = 0
            self.rect.y = random.randint(0, hauteur - self.rect.height)

class Obstacle2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_obstacle2 = os.path.join(images_obstacles, "img", "asteroide_1.png")
        self.image = pygame.image.load(image_obstacle2)
        self.image = pygame.transform.scale(self.image, (largeur_ecran // 22, hauteur_ecran // 22))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largeur - self.rect.width)
        self.rect.y = random.randint(0, hauteur - self.rect.height)
        self.vitesse_x = random.randint(1, 4)
        self.vitesse_y = random.randint(-2, 2)

    def update(self):
        self.rect.x += self.vitesse_x
        self.rect.y += self.vitesse_y

        if self.rect.left > largeur:
            self.rect.right = 0
            self.rect.y = random.randint(0, hauteur - self.rect.height)

class Obstacle3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_obstacle3 = os.path.join(images_obstacles, "img", "asteroide_1.png")
        self.image = pygame.image.load(image_obstacle3)
        self.image = pygame.transform.scale(self.image, (largeur_ecran // 22, hauteur_ecran // 22))
        self.rect = self.image.get_rect()

        # Placer l'obstacle en haut de l'écran
        self.rect.x = largeur_ecran // 2
        self.rect.y = 0

        # Initialiser la vitesse
        self.vitesse_x = 0
        self.vitesse_y = 1

        # Gestion du temps et de la visibilité
        self.temps = 0
        self.duree_apparition = 2 * 60  # 2 secondes * 60 ticks par seconde
        self.cycle_complet = 15 * 60  # 15 secondes * 60 ticks par seconde
        self.visible = False  # L'obstacle est initialement invisible

    def update(self):
        self.temps += 1
        if self.temps % self.cycle_complet < self.duree_apparition:
            self.visible = True
        else:
            self.visible = False
            self.rect.y = -100


# Groupe pour les obstacles
obstacles = pygame.sprite.Group()
for _ in range(5):  
    obstacle = Obstacle()
    obstacles.add(obstacle)

obstacles2 = pygame.sprite.Group()
for _ in range(4):
    obstacle2 = Obstacle2()
    obstacles2.add(obstacle2)

obstacles3 = pygame.sprite.Group()
for _ in range(0):
    obstacle3 = Obstacle3()
    obstacles3.add(obstacle3)

# Variable pour le message de collision
message_collision = "Bloster s'est fait toucher"

# Font pour le message de collision
font_collision = pygame.font.Font(None, 36)

# Surface pour afficher le message de collision
surface_collision = pygame.Surface(((largeur // 3), (hauteur // 3)))
surface_collision.set_alpha(200)
surface_collision.fill((50, 50, 50))
rect_collision = surface_collision.get_rect(center=(largeur // 2, hauteur // 2))

def afficher_fenetre_collision():
    global message_collision
    dialogue_font = pygame.font.Font(None, 36)
    options_collision = ["Restart le Bloster",  "Quitter le jeu"]

    dialogue_surface = pygame.Surface(((largeur // 3), (hauteur // 3)))
    dialogue_surface.set_alpha(200)
    dialogue_surface.fill((50, 50, 50))

    dialogue_rect = dialogue_surface.get_rect(center=(largeur // 2, hauteur // 2))

    fenetre.blit(dialogue_surface, dialogue_rect)

    options_rect = []

    for i, option in enumerate(options_collision):
        texte_option = dialogue_font.render(option, True, (255, 255, 255))
        option_rect = texte_option.get_rect(center=(largeur // 2, hauteur // 2 + i * 40))

        if option_rect.collidepoint(pygame.mouse.get_pos()):
            texte_option = dialogue_font.render(option, True, (255, 0, 0))

        fenetre.blit(texte_option, option_rect)
        options_rect.append(option_rect)

    # Afficher le message de collision
    texte_collision = font_collision.render(message_collision, True, (255, 255, 255))
    rect_collision_texte = texte_collision.get_rect(center=(largeur // 2, hauteur // 2 - 40))
    fenetre.blit(texte_collision, rect_collision_texte)

    pygame.display.flip()

    return options_rect