import pygame
import sys

from audio import *
from personnage import *
from ecran import *
from obstacle import *
from parametres import *
import menus  

pygame.init()

# Variables globales pour l'état du menu
menu_demarrage_affiche = True
menu_affiche = False

def gestion_clic_menu_demarrage(pos):
    global menu_demarrage_affiche, menu_affiche
    for i, option_rect in enumerate(menus.menu_options_rect_demarrage):
        if option_rect.collidepoint(pos):
            click_sound.play()
            if i == 0:  # "Démarrer le jeu"
                menu_demarrage_affiche = False
            elif i == 1:  # Paramètres
                afficher_parametres()
                print("Paramètres")
            elif i == 2:  # "Quitter"
                pygame.quit()
                sys.exit()

def gestion_clic_menu_principal(pos):
    global menu_affiche
    for i, option_rect in enumerate(menus.menu_options_rect_principal):
        if option_rect.collidepoint(pos):
            click_sound.play()
            if i == 0:  # "Continuer"
                menu_affiche = False
            elif i == 1:  # "Paramètres"
                afficher_parametres()
                print("Ouvrir les paramètres")
            elif i == 2:  # "Quitter"
                pygame.quit()
                sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if menu_demarrage_affiche:
                gestion_clic_menu_demarrage(event.pos)
            elif menu_affiche:
                gestion_clic_menu_principal(event.pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_affiche = not menu_affiche

    if menu_demarrage_affiche:
        menus.afficher_menu_demarrage()
    elif menu_affiche:
        menus.afficher_menu_principal()
    else:
        if not menu_affiche:
            nouvelle_taille_personnage = (largeur_ecran // 20, hauteur_ecran // 12)
            personnage_image = pygame.transform.scale(personnage_image, nouvelle_taille_personnage)
            personnage_rect.size = nouvelle_taille_personnage

            # Gestion des touches pour déplacer le personnage
            touches = pygame.key.get_pressed()
            if touches[pygame.K_q] and personnage_rect.left > 0:
                personnage_rect.x -= vitesse
            if touches[pygame.K_d] and personnage_rect.right < largeur:
                personnage_rect.x += vitesse
            if touches[pygame.K_z] and personnage_rect.top > 0:
                personnage_rect.y -= vitesse
            if touches[pygame.K_s] and personnage_rect.bottom < hauteur:
                personnage_rect.y += vitesse

            # Vérifier les collisions avec les obstacles
            for obstacle in obstacles:
                if personnage_rect.colliderect(obstacle.rect):
                    options_rect_collision = afficher_fenetre_collision()
                    message_collision = "Bloster est mort !!"
                    collision_sound.play()

                    choix_fait = False
                    while not choix_fait:
                        for event_collision in pygame.event.get():
                            if event_collision.type == pygame.MOUSEBUTTONDOWN and event_collision.button == 1:
                                for i, option_rect in enumerate(options_rect_collision):
                                    if option_rect.collidepoint(event_collision.pos):
                                        if i == 0:
                                            print("Restart le Bloster")
                                            reinitialiser_jeu()
                                            choix_fait = True
                                        elif i == 1:
                                            pygame.quit()
                                            sys.exit()

                                        choix_fait = True

            # Vérifier les collisions avec les obstacles du deuxième groupe
            for obstacle2 in obstacles2:
                if personnage_rect.colliderect(obstacle2.rect):
                    options_rect_collision = afficher_fenetre_collision()
                    message_collision = "Bloster s'est fait détruire !!"
                    collision_sound.play()

                    choix_fait = False
                    while not choix_fait:
                        for event_collision in pygame.event.get():
                            if event_collision.type == pygame.MOUSEBUTTONDOWN and event_collision.button == 1:
                                for i, option_rect in enumerate(options_rect_collision):
                                    if option_rect.collidepoint(event_collision.pos):
                                        if i == 0:
                                            print("Restart le Bloster")
                                            reinitialiser_jeu()
                                            choix_fait = True
                                        elif i == 1:
                                            pygame.quit()
                                            sys.exit()

                                        choix_fait = True

            # Vérifier les collisions avec les obstacles du troixième groupe
            for obstacle3 in obstacles3:
                if personnage_rect.colliderect(obstacle3.rect):
                    options_rect_collision = afficher_fenetre_collision()
                    message_collision = "Bloster s'est fait toucher !!"
                    collision_sound.play()

                    choix_fait = False
                    while not choix_fait:
                        for event_collision in pygame.event.get():
                            if event_collision.type == pygame.MOUSEBUTTONDOWN and event_collision.button == 1:
                                for i, option_rect in enumerate(options_rect_collision):
                                    if option_rect.collidepoint(event_collision.pos):
                                        if i == 0:
                                            print("Restart le Bloster")
                                            reinitialiser_jeu()
                                            choix_fait = True
                                        elif i == 1:
                                            pygame.quit()
                                            sys.exit()

                                        choix_fait = True

        # Mise à jour de l'affichage
        fenetre.fill((0, 0, 0))
        fenetre.blit(personnage_image, personnage_rect)

        # Calculer le temps écoulé depuis la dernière mise à jour
        temps_passe = pygame.time.get_ticks() - temps_actuel
        temps_actuel += temps_passe
        # Convertir le temps en secondes
        temps_ecoule += temps_passe / 1000

        # Afficher le temps en jeu
        font_temps = pygame.font.Font(None, 36)
        texte_temps = font_temps.render(f"Temps : {int(temps_ecoule)} s", True, (255, 255, 255))
        rect_temps = texte_temps.get_rect(topleft=(10, 10))
        fenetre.blit(texte_temps, rect_temps)

        if menu_demarrage_affiche:
            menus.afficher_menu_demarrage()
            menu_surface = pygame.Surface(((largeur // 3), (hauteur // 3)))
            menu_surface.set_alpha(200)
            menu_surface.fill((50, 50, 50))

            menu_rect = menu_surface.get_rect(center=(largeur // 2, hauteur // 2))

            fenetre.blit(menu_surface, menu_rect)

            # Liste pour stocker les rectangles des options du menu
            menu_options_rect = []

            for i, option in enumerate(menu_options):
                texte_option = menu_font.render(option, True, (255, 255, 255))

                # Effet de survol : changement de couleur
                option_rect = texte_option.get_rect(center=(largeur // 2, hauteur // 2 + i * 40))
                if option_rect.collidepoint(pygame.mouse.get_pos()):
                    texte_option = menu_font.render(option, True, (255, 0, 0))

                fenetre.blit(texte_option, option_rect)

                # Ajouter le rectangle de l'option à la liste
                menu_options_rect.append(option_rect)

        # Mise à jour et dessin des obstacles du premier groupe
        obstacles.update()
        obstacles.draw(fenetre)

        # Mise à jour et dessin des obstacles du deuxième groupe
        obstacles2.update()
        obstacles2.draw(fenetre)

        # Mise à jour et dessin des obstacles du deuxième groupe
        obstacles3.update()
        obstacles3.draw(fenetre)

    pygame.display.flip()