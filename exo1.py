MAX_WIDTH = 100


DATA = {
    "Bloc 1": [
        {"text": "Le code propre facilite la maintenance", "enabled": True},
    ],
    "Bloc 2": [
        {"text": "Tester souvent évite beaucoup d erreurs", "enabled": True},
        {"text": "Cette phrase ne doit pas s afficher", "enabled": False},
    ],
    "Bloc 3": [
        {"text": "Cette phrase ne doit pas s afficher", "enabled": False},
        {"text": "Un bon code doit rester simple et clair", "enabled": False},
        {"text": "La simplicité améliore la qualité du code", "enabled": True},
        {"text": "Refactoriser améliore la compréhension", "enabled": True},
    ],
}


def calculer_largeur(lignes: list[str]) -> int:
    if not lignes:
        return 0
    return min(max(len(ligne) for ligne in lignes), MAX_WIDTH)


def afficher_tout(blocs: list[list[str]]) -> None:
    lignes_affichees: list[str] = [ligne for bloc in blocs for ligne in bloc]
    largeur = calculer_largeur(lignes_affichees)
    bordure = "-" * (largeur + 2)
    vide = "|" + (" " * largeur) + "|"

    print(bordure)
    print(vide)
    for i, lignes in enumerate(blocs):
        for ligne in lignes:
            ligne = ligne[:largeur]
            print(f"|{ligne.rjust(largeur)}|")
        if i != len(blocs) - 1:
            print(bordure)
            print(vide)
    print(bordure)


def main() -> None:
    blocs = []
    for _, items in DATA.items():
        lignes = [it["text"].lower() for it in items if it.get("enabled", True)]
        blocs.append(lignes)

    afficher_tout(blocs)


if __name__ == "__main__":
    main()