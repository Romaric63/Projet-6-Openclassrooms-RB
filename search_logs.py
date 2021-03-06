# Version 2.0
# Date : 27/05/2020
# Auteur : Romaric Béraud
# Ce script a pour but de rechercher des mots clés dans des fichiers (exemple : logs)

# Importe le module glob
import glob
# Importe le module os
import os
# Importe le module json
import json

# Demande à l'utilisateur le nom du fichier JSON
fichier_json = raw_input("Tapez le nom du fichier JSON : ")
# Demande à l'utilisateur le mot clé à rechercher
liste_mot_cle = raw_input("Quels mots rechercher ? : ").split(" ")
# Demande à l'utilisateur s'il souhaite respecter la casse
casse = raw_input("Tapez C si vous souhaitez respecter la casse : ")
# Demande à l'utilisateur s'il souhaite que le mot soit exact (qu'il soit entouré d'espaces)
espace = raw_input("Tapez E si vous souhaitez que les mots soient exacts : ")
# Initialisation de la variable nombre_lignes comptant les lignes trouvées avec le mot clé dans les fichiers d'un répertoire
nombre_lignes = 0

# Fonction permettant d'écrire dans les lignes dans le fichier resultat_logs du répertoire correspondant
def collecte_resultat():
    with open("resultat_logs", "a") as fichier_resultat:
        fichier_resultat.write(ligne)

# Ouverture du fichier JSON contenant les noms des répertoires
with open(fichier_json) as fichier_config:
    # Récupération du contenu sous forme de liste dans la variable liste_repertoire
    liste_repertoire = json.load(fichier_config)
    # Pour chaque répertoire présent dans liste_repertoire :
    for repertoire in liste_repertoire:
        # On se déplace dans le répertoire
        os.chdir(repertoire)
        # Si le fichier resultat_logs est déjà présent dans le répertoire :
        if os.path.isfile("resultat_logs"):
            # On le supprime car on ne souhaite pas réécrire à la suite
            os.remove("resultat_logs")
        # Pour chaque fichier présent dans le répertoire :
        for fichier in glob.glob("*"):
            # Si le fichier est bien un fichier (pas un répertoire) :
            if os.path.isfile(fichier):
                # Ouverture du fichier
                with open(fichier, "r") as fichier_ouvert:
                    # Pour chaque ligne d'un fichier :
                    for ligne in fichier_ouvert.readlines():
                        # Pour chaque mot clé de la liste :
                            for mot_cle in liste_mot_cle:
                                # Si on respecte la casse :
                                if casse == "C":
                                    # Si on veut le mot exact :
                                    if espace == "E":
                                        # Condition pour rechercher le mot exact en respectant la casse
                                        if mot_cle.rjust(len(mot_cle)+1).ljust(len(mot_cle)+2) in ligne:
                                            # Appel de la fonction collecte_resultat()
                                            collecte_resultat()
                                            # Compteur du nombre de lignes
                                            nombre_lignes = nombre_lignes + 1
                                    # Si on ne veut pas le mot exact :
                                    else:
                                        # Condition pour rechercher le mot en respectant la casse
                                        if mot_cle in ligne:
                                            collecte_resultat()
                                            nombre_lignes = nombre_lignes + 1
                                # Si on ne respecte pas la casse :
                                else:
                                    # Si on veut le mot exact :
                                    if espace == "E":
                                        # Condition pour rechercher le mot exact
                                        if mot_cle.lower().rjust(len(mot_cle)+1).ljust(len(mot_cle)+2) in ligne.lower():
                                            collecte_resultat()
                                            nombre_lignes = nombre_lignes + 1
                                    # Si on ne veut pas le mot exact
                                    else:
                                        # Condition pour rechercher le mot
                                        if mot_cle.lower() in ligne.lower():
                                            collecte_resultat()
                                            nombre_lignes = nombre_lignes + 1
                                
        # Informe l'utilisateur du nombre de lignes comprennant le mot clé dans les fichiers d'un répertoire et lui donne le chemin du fichier résultat
        print "Les",nombre_lignes,"lignes comprennant ce mot dans les fichiers sont presentes dans le fichier resultat_logs du repertoire",repertoire,"\n"
        # Le compteur de lignes doit être remis à 0 afin de pouvoir compter pour les autres répertoires
        nombre_lignes = 0
