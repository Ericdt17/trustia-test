# Configuration de la largeur maximale du bloc
MAX_WIDTH = 100

# Définition des phrases
phrases = {
    "p1": "Le code propre facilite la maintenance",
    "p2": "Tester souvent evite beaucoup d erreurs",
    "p3": "Cette phrase ne doit pas s afficher",
    "p4": "Un bon code doit rester simple et clair",
    "p5": "La simplicite ameliore la qualite du code",
    "p6": "Refactoriser ameliore la comprehension"
}

# exclusions par bloc (les ids restent dans `phrases`, mais peuvent être masqués selon le bloc)
exclusions_par_bloc = {
    "bloc2": {"p3"},
    "bloc3": {"p4"},
}

# définition des blocs
blocs = {
    "bloc1": ["p1"],
    "bloc2": ["p2", "p3"],
    "bloc3": ["p3", "p4", "p5", "p6"]
}

# ordre d'affichage
ordre_blocs = ["bloc1", "bloc2", "bloc3"]

# ==============================
# FONCTIONS
# ==============================

def filtrer_phrases(bloc, cles):
    #Affiche les phrases autorisées
    exclues = exclusions_par_bloc.get(bloc, set())
    return [
        phrases[cle].lower()
        for cle in cles
        if cle in phrases and cle not in exclues
    ]


def calculer_largeur(lignes):
    #Calcul la largeur du bloc
    if not lignes:
        return 0
    max_len = max(len(ligne) for ligne in lignes)
    return min(max_len, MAX_WIDTH)


def afficher_bloc(lignes, largeur, imprimer_haut=True):
    #Affiche un bloc formaté
    if not lignes:
        return

    bordure = "-" * (largeur + 4)

    # ligne du haut
    if imprimer_haut:
        print(bordure)

    # contenu
    for ligne in lignes:
        ligne = ligne[:largeur]  # coupe si dépasse
        print(f"| {ligne.rjust(largeur)} |")

    # ligne du bas
    print(bordure)


# ==============================
# EXECUTION
# ==============================

def main():
    blocs_a_afficher = []

    for bloc in ordre_blocs:
        cles = blocs.get(bloc, [])
        lignes = filtrer_phrases(bloc, cles)
        if lignes:
            blocs_a_afficher.append((bloc, lignes))

    # largeur commune fixe: 100 max (modifiable via MAX_WIDTH)
    largeur_commune = MAX_WIDTH

    for i, (_, lignes) in enumerate(blocs_a_afficher):
        afficher_bloc(lignes, largeur_commune, imprimer_haut=True)
        if i != len(blocs_a_afficher) - 1:
            print()


if __name__ == "__main__":
    main()