import random
from fonction_pendu import choisir_mot
from fonction_pendu import entrer_lettre
from fonction_pendu import trouver_lettre
from fonction_pendu import cacher_mot
from mots_pendu import mots


nombre_essais = 10
jouer = True

while jouer :
    choix = input("Souhaitez-vous faire une partie ? o/n ")
    if choix == "o":
        # on initialise le jeu
        essais = 0
        mot = choisir_mot()
        lettres_trouvees = []
        lettres_utilisees = []
        print(f'vous avez le droit à {nombre_essais} essais ! Bonne chance !')
    elif choix == "n":
        print("A bientôt :)")
        exit()
    else :
        # on réaffiche le message jusqu'a ce que l'internaute effectue une saisie valide
        print("Veuillez saisir 'o' ou 'n'")
        continue



    while essais < nombre_essais :
        if len(lettres_utilisees) > 0 : # aide mémoire pour l'utilisateur : indique les lettres déjà cherchées
            print(f"Vous avez déjà cherché les lettres suivantes : {lettres_utilisees}")
        lettre_utilisateur = entrer_lettre()
        if lettre_utilisateur in lettres_utilisees : # alerte l'utilisateur en cas de doublon de saisie d'une lettre
            print(f"Attention, vous avez déjà utilisé la lettre '{lettre_utilisateur}' !")
            continue
        lettres_utilisees.append(lettre_utilisateur)
        nouvelle_lettre = trouver_lettre(lettre_utilisateur, mot)
        lettres_trouvees.append(nouvelle_lettre)
        mot_cacher = cacher_mot(mot, lettres_trouvees)
        print(mot_cacher)
        if mot == mot_cacher :
            print(f"Bravo vous avez gagné, le mot mystère était {mot} !")
            break # on sort de la boucle while actuelle pour revenir à la boucle jouer
        essais +=1 
        essais_restant = nombre_essais - essais
        print(f"Il vous reste {essais_restant} essais !")
        if essais == nombre_essais :
            print(f"Perdu ! le mot mystère était : '{mot}'!")