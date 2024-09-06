import pygame

pygame.init()

# Obtenir les informations sur l'écran
info_ecran = pygame.display.Info()
largeur_ecran, hauteur_ecran = info_ecran.current_w, info_ecran.current_h

# Définir la nouvelle taille de la fenêtre
largeur, hauteur = largeur_ecran, hauteur_ecran
taille_fenetre = (largeur, hauteur)

# Créer la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Bloster game")