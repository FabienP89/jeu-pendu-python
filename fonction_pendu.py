import random
from mots_pendu import mots


def choisir_mot():
    mot = random.choice(mots)
    print("Le mot vient d'être enregistré !")
    return(mot)

def entrer_lettre():
    lettre_utilisateur = input("Entrez une lettre : ")
    lettre_utilisateur = lettre_utilisateur.lower()
    if len(lettre_utilisateur) > 1 or not lettre_utilisateur.isalpha():
        print("Entrez une lettre correcte")
        return entrer_lettre()
    else :
        return lettre_utilisateur

def trouver_lettre(lettre_utilisateur, mot):
    if lettre_utilisateur in mot :
        print(f"Vous venez de trouver la lettre {lettre_utilisateur} !")
        return lettre_utilisateur
    else :
        print("La lettre n'est pas dans le mot mystère")


def cacher_mot(mot, lettres_trouvees):
    mot_cacher = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cacher += lettre
        else:
            mot_cacher += "*"
    return mot_cacher