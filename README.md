Exercice 1 :
Créer un programme python qui affiche dans la console des blocs de texte encadrés comme dans l’exemple
fourni.

Contraintes
 La largeur maximale d’un bloc est de 100 caractères et doit être facilement modifiable.
 Tout le texte doit être affiché en minuscules.
 Les blocs peuvent contenir une ou plusieurs lignes.
 Les bordures utilisent - pour les lignes et | pour les côtés.
Organisation des données
 Toutes les phrases doivent être stockées dans un dictionnaire.
 Certaines phrases peuvent rester dans le dictionnaire sans être affichées.
 L’ordre d’affichage doit pouvoir être facilement modifié.
Blocs à produire
Bloc 1
 Le code propre facilite la maintenance
Bloc 2
 Tester souvent évite beaucoup d erreurs
 Cette phrase ne doit pas s afficher
Bloc 3
 Cette phrase ne doit pas s afficher
 Un bon code doit rester simple et clair
 La simplicité améliore la qualité du code
 Refactoriser améliore la compréhension

Règle importante
Les phrases suivantes ne doivent pas apparaître dans la console, même si elles sont dans le dictionnaire :
 la phrase du bloc 2 : « Cette phrase ne doit pas s afficher »
 la phrase du bloc 3 : « Un bon code doit rester simple et clair »
Objectif
Le code doit permettre facilement :
 de modifier le texte
 de changer l’ordre des blocs
 d’ajouter ou supprimer des lignes
 de garder certaines phrases dans le dictionnaire sans les afficher.

Astuce
Utiliser une structure de données centralisée (dictionnaire ou tableau) contenant toutes les phrases, y
compris celles qui ne seront pas affichées.
Les phrases doivent être stockées dans un seul dictionnaire structuré, afin de définir directement à la fois le
contenu et la séquence des blocs sans utiliser une structure supplémentaire.
L’activation ou la désactivation d’une phrase doit pouvoir se faire en modifiant uniquement un paramètre
léger (par exemple un booléen ou un mot-clé), sans changer la logique globale du programme.

Excercice 2 :
Créer un programme Python qui affiche dans la console un menu de restaurant à partir de données
structurées.

Contraintes
• Le menu doit être affiché par catégories (Entrées, Plats, Desserts).
• Chaque catégorie contient plusieurs plats.
• Chaque plat possède :
• un nom
• un prix
• une disponibilité (disponible ou non)
• Les plats non disponibles ne doivent pas être affichés.
• Tous les noms doivent être affichés en minuscules.
• Les prix doivent être affichés avec "€".
Données à gérer
Le programme doit permettre de représenter les informations suivantes :
Entrées
• Salade César — 8€ (disponible)
• Soupe du jour — 6€ (indisponible)
Plats
• Steak frites — 15€ (disponible)
• Poisson grillé — 14€ (disponible)
• Plat du chef — 18€ (indisponible)
Desserts
• Tiramisu — 7€ (disponible)
• Glace — 5€ (disponible)
• Dessert mystère — 9€ (indisponible)
Objectif
Le programme doit être conçu de manière à permettre facilement :
• l’ajout ou la suppression d’une catégorie
• l’ajout ou la suppression d’un plat
• la modification du prix d’un plat
• le changement de la disponibilité d’un plat