from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Dish:
    name: str
    price_eur: int
    available: bool = True





MENU: dict[str, list[Dish]] = {
    "--- entrées ---": [
        Dish(name="Salade César", price_eur=8, available=True),
        Dish(name="Soupe du jour", price_eur=6, available=False),
    ],
    "--- plats ---": [
        Dish(name="Steak frites", price_eur=15, available=True),
        Dish(name="Poisson grillé", price_eur=14, available=True),
        Dish(name="Plat du chef", price_eur=18, available=False),
    ],
    "--- desserts ---": [
        Dish(name="Tiramisu", price_eur=7, available=True),
        Dish(name="Glace", price_eur=5, available=True),
        Dish(name="Dessert mystère", price_eur=9, available=False),
    ],
}

def add_category(menu: dict[str, list[Dish]], category: str) -> None:
    menu.setdefault(category, [])


def remove_category(menu: dict[str, list[Dish]], category: str) -> None:
    menu.pop(category, None)


def add_dish(menu: dict[str, list[Dish]], category: str, dish: Dish) -> None:
    add_category(menu, category)
    menu[category].append(dish)


def remove_dish(menu: dict[str, list[Dish]], category: str, dish_name: str) -> None:
    dishes = menu.get(category)
    if not dishes:
        return
    name_lc = dish_name.strip().lower()
    menu[category] = [d for d in dishes if d.name.strip().lower() != name_lc]


def update_price(menu: dict[str, list[Dish]], category: str, dish_name: str, new_price_eur: int) -> None:
    dishes = menu.get(category)
    if not dishes:
        return
    name_lc = dish_name.strip().lower()
    for dish in dishes:
        if dish.name.strip().lower() == name_lc:
            dish.price_eur = new_price_eur
            return


def set_availability(menu: dict[str, list[Dish]], category: str, dish_name: str, available: bool) -> None:
    dishes = menu.get(category)
    if not dishes:
        return
    name_lc = dish_name.strip().lower()
    for dish in dishes:
        if dish.name.strip().lower() == name_lc:
            dish.available = available
            return


def format_price_eur(price_eur: int) -> str:
    return f"{price_eur}€"


def print_menu(menu: dict[str, list[Dish]]) -> None:
    for category, dishes in menu.items():
        available_dishes = [d for d in dishes if d.available]
        if not available_dishes:
            continue

        print(category)
        for dish in available_dishes:
            print(f"{dish.name.lower()} — {format_price_eur(dish.price_eur)}")
        print()


def main() -> None:
    # Démo modifiation du menu avec des function .
    #
    # print("MENU INITIAL\n")
    # print_menu(MENU)
    #
    # set_availability(MENU, "--- entrées ---", "Soupe du jour", True)
    # update_price(MENU, "--- plats ---", "Steak frites", 16)
    # add_dish(MENU, "--- desserts ---", Dish(name="Crème brûlée", price_eur=8, available=True))
    # remove_dish(MENU, "--- plats ---", "Poisson grillé")
    #
    # print("MENU APRÈS MODIFS\n")
    # print_menu(MENU)

    print_menu(MENU)


if __name__ == "__main__":
    main()
