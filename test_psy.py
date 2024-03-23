import random

# lettres de la première phase
phase1 = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
# associations des mots pour chaque lettre
phase2 = [
    ["A", "B"],
    ["C", "D"],
    ["E", "F"],
    ["G", "H"],
    ["I", "J"],
    ["K", "L"],
    ["M", "N"],
    ["O", "P"],
    ["Q", "R"],
    ["S", "T"],
    ["U", "V"],
    ["W", "X"],
    ["Y", "Z"],
]
# associations des positions des mots
phase3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12, 13]]
phase4 = [[1, 2], [3, 4], [5, 6]]

# thematique à remplir
rez = ["vie", "mort", "vie sexuelle"]

# dictionnaire vide des reponses de la phase 1
resp1 = {}
# index associés à chaque lettre
index = list(range(len(phase1)))
# on reste sur la phase 1 tant que toutes les lettres n'ont pas été répondus
while len(index) != 0:
    i = random.choice(index)  # choix aléatoire d'un indice
    resp1[phase1[i]] = str(
        input(phase1[i] + " : ")
    )  # entrée du mot pour la lettre correspondant à l'indice
    index.remove(
        i
    )  # suppresion de l'indice de la liste des indices qu'il reste à remplir

resp2 = {}
index = list(range(len(phase2)))
while len(index) != 0:
    i = random.choice(index)
    mots = ""  # initialisation des mots à faire correspondre
    # on ajoute à la chaine de caractère chaque mot défini par les associations définis pour la phase 2
    for lettre in phase2[i]:
        mots = mots + resp1[lettre] + " / " * (lettre != phase2[i][len(phase2[i]) - 1])
    resp2[str(i)] = str(
        input(mots + " : ")
    )  # entree du mot correspondant aux mots ajouté à la chaine de caractère
    index.remove(i)

# on repete  pour chaque phase
resp3 = {}
index = list(range(len(phase3)))
while len(index) != 0:
    i = random.choice(index)
    mots = ""
    for lettre in phase3[i]:
        mots = (
            mots
            + resp2[str(lettre - 1)]
            + " / "
            * (
                lettre != phase3[i][len(phase3[i]) - 1]
            )  # on met un slach a près le mot tant qu'on n'est pas arrivé au denier
        )
    resp3[str(i)] = str(input(mots + " : "))
    index.remove(i)

resp4 = {}
index = list(range(len(phase4)))
while len(index) != 0:
    i = random.choice(index)
    mots = ""
    for lettre in phase4[i]:
        mots = (
            mots
            + resp3[str(lettre - 1)]
            + " / " * (lettre != phase4[i][len(phase4[i]) - 1])
        )
    resp4[rez[i]] = str(
        input(mots + " : ")
    )  # association de la thématique et du mot qui correspond
    index.remove(i)

print("\n --------------------------------- \n Résultats : \n")
# affichage pour chaque thématique
for key, values in resp4.items():
    print(key + " : " + values)
