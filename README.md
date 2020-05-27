# Projet-6-Openclassrooms-RB

Ce script développé en Python 2.7.16 sert à rechercher des mots dans un ou plusieurs répertoires. Il est notamment pertinent pour rechercher dans les répertoires de logs mais il est possible de l'utiliser pour n'importe quel répertoire.

# Dépendance

- Télécharger la dernière version du script search_logs.py
- Créer un fichier de configuration en JSON (vous pouvez télécharger l'exemple repertoire.json) qui doit se trouver dans le même répertoire que le script sinon il faut indiquer le chemin absolu lors du lancement.
- Installer Python 2.7.16.
- Ce script a été développé et testé sous Debian.

# Syntaxe du fichier JSON

Vous pouvez paramétrer autant de répertoires que vous le voulez comme ceci :
[ "/var/log" , "/var/log/apt" , "/var/log/installer" , "/var/log/exemple" ]

# Utilisation du script

Pour lancer le script :
- Utiliser la commande "python search_logs.py".
- Indiquer le nom du fichier JSON (exemple : repertoire.json).
- Taper le ou les mot(s) clé(s) à séparer par un espace pour les rechercher dans les fichiers du répertoire précédemment indiqué.
- Taper "C" si vous souhaitez respecter la casse.
- Taper "E" si vous souhaitez rechercher le mot exact (exemple : "error" trouvera "Error" mais pas "errors").

# Résultat

Le script vous retourne le nombre de lignes comportant le(s) mot(s) clé(s) dans les fichiers des répertoires.
Il crée des fichiers résultats (resultat_logs) comportant ces lignes pour chaque répertoire.
