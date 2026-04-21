import json
import os

def insert_explanation(nb, index, explanation):
    new_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [f"**Explication de la réponse ci-dessus :**\n", explanation]
    }
    # We find the actual cell in the current notebook state
    nb['cells'].insert(index + 1, new_cell)

# 1. TP_mini_GOT
with open('notebooks_temp/TP_mini_GOT-sujet.ipynb', 'r') as f:
    nb = json.load(f)

insert_explanation(nb, 14, "Cette réponse permet de calculer le nombre total d'interactions pour chaque personnage. En utilisant un dictionnaire `scores`, on incrémente la valeur à chaque fois qu'un personnage apparaît dans une relation. Ensuite, `sorted` est utilisé avec une fonction lambda pour trier le dictionnaire par valeur décroissante et récupérer le top 5.")
insert_explanation(nb, 12, "Cette réponse vérifie si les relations sont symétriques ou s'il y a des doublons inversés. En créant deux sets (`ordre1` avec les paires `(a,b)` et `ordre2` avec les paires `(b,a)`) et en faisant leur intersection, on vérifie quelles relations existent dans les deux sens dans le fichier.")
insert_explanation(nb, 10, "Cette réponse permet de compter le nombre de personnages uniques. On crée deux ensembles (sets) `perso1` et `perso2` regroupant respectivement les personnages de la première et deuxième colonne. L'opérateur `|` réalise l'union des deux ensembles, supprimant ainsi les doublons, et `len()` donne le nombre total.")
insert_explanation(nb, 8, "Cette réponse a pour but de nettoyer les données brutes. En utilisant une liste en compréhension avec `relations_[1:]`, on ignore la première ligne (les en-têtes du CSV). De plus, le poids de la relation `w` est converti en entier (`int(w)`) pour pouvoir faire des calculs par la suite.")
insert_explanation(nb, 6, "Cette commande compte et affiche le nombre d'éléments (lignes) contenus dans la liste `relations_`, ce qui donne la taille du jeu de données récupéré depuis le fichier CSV.")

with open('notebooks_temp/TP_mini_GOT-sujet.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)


# 2. TP_mini_vectorisation_collatz
with open('notebooks_temp/TP_mini_vectorisation_collatz-sujet.ipynb', 'r') as f:
    nb = json.load(f)

insert_explanation(nb, 16, "Cette fonction `vols(n)` améliorée calcule les longueurs de vols pour tous les nombres de 1 à n en même temps. Elle initialise un tableau de zéros `compteur`. Tant qu'il reste des éléments différents de 1, elle incrémente le compteur pour ces éléments spécifiques et passe à l'itération suivante via `iteration()`. Elle retourne finalement le tableau des longueurs.")
insert_explanation(nb, 13, "Cette réponse partielle sert à itérer et afficher les étapes de la suite de Collatz de façon vectorisée. Elle crée un tableau `ite` allant de 1 à n, et utilise une boucle `while` qui continue tant qu'au moins un élément n'a pas atteint 1 (grâce à `np.any(ite!=1)`). Elle applique la fonction `iteration` en boucle.")
insert_explanation(nb, 8, "Cette fonction `iteration(u)` applique une étape de la suite de Collatz sur tout un tableau NumPy en parallèle. Elle utilise des 'masques booléens' (`maskpair` pour les pairs, `maskimpair` pour les impairs différents de 1) pour sélectionner et modifier simultanément les bons éléments du tableau sans utiliser de boucle `for` classique en Python, ce qui est beaucoup plus rapide (vectorisation).")

with open('notebooks_temp/TP_mini_vectorisation_collatz-sujet.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)


# 3. TP_mini_regex
with open('notebooks_temp/TP_mini_regex-sujet.ipynb', 'r') as f:
    nb = json.load(f)

insert_explanation(nb, 37, "Cette réponse sert à éliminer les doublons et à trier les noms des auteurs. La fonction `set(Auteurs)` convertit la liste en un ensemble (qui ne peut pas contenir de doublons), puis `sorted()` trie cet ensemble par ordre alphabétique pour obtenir une liste propre et lisible.")
insert_explanation(nb, 36, "Cette réponse utilise une expression régulière (`re.findall`) pour extraire spécifiquement les noms des auteurs dans le code source de la page Wikipédia. L'expression cible les balises `<a>` situées après le mot 'by', et capture grâce aux parenthèses `(.*?)` le texte contenu à l'intérieur du lien HTML (c'est-à-dire le nom de l'auteur).")

with open('notebooks_temp/TP_mini_regex-sujet.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)


# 4. TP_2A_fouille_donnees_A
with open('notebooks_temp/TP_2A_fouille_donnees_A-sujet.ipynb', 'r') as f:
    nb = json.load(f)

insert_explanation(nb, 23, "Cette réponse calcule la consommation moyenne mensuelle pour un compteur spécifique (27712EC1) sur l'année 2016. Une boucle parcourt simultanément les dates et les mesures. Si l'année est 2016, on ajoute la valeur au mois correspondant (`sommes[m]`) et on compte le nombre de mesures (`nbmesures[m]`) pour pouvoir en déduire une moyenne par mois.")
insert_explanation(nb, 20, "Cette réponse permet de visualiser la courbe de charge (consommation) d'un compteur ('870662EC1') sur les 48 premières mesures. Elle utilise `matplotlib.pyplot` pour tracer le graphique (`plt.plot`), et modifie les paramètres globaux `plt.rcParams` pour agrandir la taille de la police et la taille de la figure afin que le graphique soit bien lisible.")
insert_explanation(nb, 16, "Cette réponse sert à convertir des chaînes de caractères représentant des dates en véritables objets `datetime` manipulables en Python. La liste en compréhension parcourt la liste des dates sous forme de texte, et `datetime.strptime` les traduit en utilisant le format spécifié (Année-Mois-Jour Heure:Minute:Seconde).")

with open('notebooks_temp/TP_2A_fouille_donnees_A-sujet.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
