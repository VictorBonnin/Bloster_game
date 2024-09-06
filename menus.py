import pygame
import os
from ecran import *  # Assurez-vous que cela importe correctement `largeur`, `hauteur`, et `fenetre`

script_dir = os.path.dirname(__file__)

menu_options_rect_demarrage = []
menu_options_rect_principal = []

chemin_image_fond = os.path.join(script_dir, "img", "accueil.png")
image_fond = pygame.image.load(chemin_image_fond).convert()
image_fond = pygame.transform.scale(image_fond, (largeur, hauteur))

def afficher_menu_demarrage():
    global menu_options_rect_demarrage
    menu_font = pygame.font.Font(None, 36)
    menu_options = ["Démarrer le jeu", "Paramètres", "Quitter"]

    fenetre.blit(image_fond, (0, 0))

    # Charger l'image pour le menu
    chemin_image_menu = os.path.join(script_dir, "img", "ufo.png")
    image_menu = pygame.image.load(chemin_image_menu).convert_alpha()
    image_menu = pygame.transform.scale(image_menu, (largeur // 4, int(hauteur // 4.5)))

    # Création d'un surface semi-transparente pour le menu
    menu_surface = pygame.Surface((largeur // 3, hauteur // 4.5), pygame.SRCALPHA)
    menu_surface.blit(image_menu, (0, 0))

    menu_rect = menu_surface.get_rect(center=(largeur // 4, hauteur // 3))
    fenetre.blit(menu_surface, menu_rect)

    menu_options_rect_demarrage = []
    for i, option in enumerate(menu_options):
        texte_option = menu_font.render(option, True, (255, 255, 255))
        option_rect = texte_option.get_rect(center=(largeur // 4.75, hauteur // 2.2 - 50 + i * 60))
        if option_rect.collidepoint(pygame.mouse.get_pos()):
            texte_option = menu_font.render(option, True, (255, 0, 0))
        fenetre.blit(texte_option, option_rect)
        menu_options_rect_demarrage.append(option_rect)



def afficher_menu_principal():
    global menu_options_rect_principal
    menu_font = pygame.font.Font(None, 36)
    menu_options = ["Continuer", "Paramètres", "Quitter"]

    menu_surface = pygame.Surface((largeur // 3, hauteur // 3))
    menu_surface.set_alpha(200)
    menu_surface.fill((50, 50, 50))

    menu_rect = menu_surface.get_rect(center=(largeur // 2, hauteur // 2))
    fenetre.blit(menu_surface, menu_rect)

    menu_options_rect_principal = []
    for i, option in enumerate(menu_options):
        texte_option = menu_font.render(option, True, (255, 255, 255))
        # suite de la fonction afficher_menu_principal()
        option_rect = texte_option.get_rect(center=(largeur // 2, hauteur // 2 + i * 50))
        if option_rect.collidepoint(pygame.mouse.get_pos()):
            texte_option = menu_font.render(option, True, (255, 0, 0))

        fenetre.blit(texte_option, option_rect)
        menu_options_rect_principal.append(option_rect)
