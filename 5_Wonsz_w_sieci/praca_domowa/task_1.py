from dataclasses import dataclass
from typing import Set, Tuple


@dataclass
class HotShot:
    promotion_name: str
    promotion_total_count: int


def get_xkom_hotshot_product_data() -> HotShot:
    """
    Napisz funkcję która pobiera Gorący strzał z głównej strony https://www.x-kom.pl/.

    Tips:
        1. Sprawdź jak przeglądarka odpytuje API xkomu (konsola developerska w przeglądarce)
        2. Sprawdź czy na pewno masz wszystkie potrzebne nagłówki

    Przykład:
    >>> get_xkom_hotshot_product_data()
    HotShot(promotion_name='ASUS TUF GAMING Z590-PLUS\xa0(Socket 1200)', promotion_total_count=100)
    """


def get_matching_keywords(name: str, keywords: Set[str]) -> Set[str]:
    """
    Napisz funkcję która sprawdza czy którykolwiek ze słów kluczowych znajduje się w
    podanej nazwie. Zwróć set wszystkich słów kluczwych które występują w nazwie.


    Tips:
        1. Pamiętaj aby sprowadzić nazwę produktu do małych liter.

    Przykład:
    >>> get_matching_keywords("Telefon NoKia 3310", {"nokia", "sony"})
    {'nokia'}
    >>> get_matching_keywords("Telefon NoKia 3310plus", {"3310", "nokia"})
    {'nokia', '3310'}

    """


def check_xkom_hotshot(keywords: Set[str]) -> Tuple[HotShot, Set[str]]:
    """
    Napisz funkcję która zwróci dane produktu na gorącym strzale oraz wszystkie słowa
    kluczowe które zawierają się w nazwie produktu.

    Tips:
        1. Użyj tego co już zapiplementówałeś/aś

    Przykład:
    >>> check_xkom_hotshot(keywords={'owoce', 'warzywa'})
    (HotShot(promotion_name='ASUS TUF GAMING Z590-PLUS\xa0(Socket 1200)', promotion_total_count=100), set())
    >>> check_xkom_hotshot(keywords={'nokia'})
    (HotShot(promotion_name='Telefon NoKia 3310', promotion_total_count=100), {'nokia'})
    """
