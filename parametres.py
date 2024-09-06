import pygame
import random
from ecran import *
from audio import *
from obstacle import *
from personnage import *

pygame.init()

images_audio = os.path.dirname(__file__)

# Variable pour le temps écoulé (en secondes)
temps_ecoule = 0
temps_actuel = pygame.time.get_ticks()

def reinitialiser_jeu():
    global temps_ecoule, temps_actuel
    temps_ecoule = 0
    temps_actuel = pygame.time.get_ticks()

    # Réinitialiser la position du personnage
    personnage_rect.x = largeur // 2
    personnage_rect.y = hauteur // 2

    # Réinitialiser la position des obstacles
    for obstacle in obstacles:
        obstacle.rect.x = random.randint(0, largeur - obstacle.rect.width)
        obstacle.rect.y = random.randint(0, hauteur - obstacle.rect.height)

    for obstacle2 in obstacles2:
        obstacle2.rect.x = random.randint(0, largeur - obstacle2.rect.width)
        obstacle2.rect.y = random.randint(0, hauteur - obstacle2.rect.height)

# -------------------------------------------------
# Paramètres audio
taille_police = int(hauteur_ecran * 0.03)
font = pygame.font.Font(None, taille_police)

# Charger les images pour les boutons
image_plus = os.path.join(images_audio, "img", "volume_up.png")
image_moins = os.path.join(images_audio, "img", "volume_down.png")
plus_image = pygame.image.load(image_plus).convert_alpha()
moins_image = pygame.image.load(image_moins).convert_alpha()

# Redimensionner les images pour les boutons
plus_image = pygame.transform.scale(plus_image, (50, 50))
moins_image = pygame.transform.scale(moins_image, (50, 50))

def regler_volume_musique(nouveau_volume):
    global volume_musique
    volume_musique = max(0, min(1, nouveau_volume))
    pygame.mixer.music.set_volume(volume_musique)

def regler_volume_menu(nouveau_volume):
    global volume_menu
    volume_menu = max(0, min(1, nouveau_volume))
    click_sound.set_volume(volume_menu)

def regler_volume_collision(nouveau_volume):
    global volume_collision
    volume_collision = max(0, min(1, nouveau_volume))
    collision_sound.set_volume(volume_collision)

def afficher_parametres():
    global volume_musique, volume_menu, volume_collision
    en_parametres = True
    clock = pygame.time.Clock()

    positions = {
        'musique': (50, 'Musique', lambda: volume_musique),
        'menu': (200, 'Son du menu', lambda: volume_menu),
        'collision': (350, 'Son de collision', lambda: volume_collision)
    }

    boutons = {}
    for cle, (y, label, volume_func) in positions.items():
        boutons[cle] = {
            'plus': pygame.Rect(150, y, 50, 50),
            'moins': pygame.Rect(250, y, 50, 50),
            'label': font.render(label, True, (255, 255, 255)),
            'volume_func': volume_func
        }

    bouton_sortie_rect = pygame.Rect((largeur_ecran / 1.1), (hauteur_ecran / 1.08), (largeur_ecran / 12), (hauteur_ecran / 20))
    bouton_sortie_texte = font.render("Retour", True, (255, 255, 255))

    while en_parametres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_parametres = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for cle, bouton in boutons.items():
                    if bouton['plus'].collidepoint(event.pos):
                        click_sound.play()
                        if cle == 'musique':
                            regler_volume_musique(volume_musique + 0.05)
                        elif cle == 'menu':
                            regler_volume_menu(volume_menu + 0.05)
                        elif cle == 'collision':
                            regler_volume_collision(volume_collision + 0.05)
                    elif bouton['moins'].collidepoint(event.pos):
                        click_sound.play()
                        if cle == 'musique':
                            regler_volume_musique(volume_musique - 0.05)
                        elif cle == 'menu':
                            regler_volume_menu(volume_menu - 0.05)
                        elif cle == 'collision':
                            regler_volume_collision(volume_collision - 0.05)

                if bouton_sortie_rect.collidepoint(event.pos):
                    en_parametres = False

        fenetre.fill((0, 0, 0))

        for cle, bouton in boutons.items():
            fenetre.blit(plus_image, bouton['plus'].topleft)
            fenetre.blit(moins_image, bouton['moins'].topleft)
            fenetre.blit(bouton['label'], (bouton['plus'].x - 100, bouton['plus'].y - 30))
            volume_texte = font.render(f"{int(bouton['volume_func']() * 100)}%", True, (255, 255, 255))
            fenetre.blit(volume_texte, (350, bouton['plus'].y + 15))

        pygame.draw.rect(fenetre, (255, 0, 0), bouton_sortie_rect)
        fenetre.blit(bouton_sortie_texte, (bouton_sortie_rect.x + 10, bouton_sortie_rect.y + 10))

        pygame.display.flip()
        clock.tick(60)