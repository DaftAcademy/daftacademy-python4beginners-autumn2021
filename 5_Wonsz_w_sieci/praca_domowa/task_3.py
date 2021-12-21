from dataclasses import dataclass


@dataclass
class Contact:
    email: str
    phone: str
    address: str
    instagram: str


def get_daftcode_contact_info() -> Contact:
    """
    Napisz funkcję która pobierze z głównej strony Dafta (https://daftcode.pl/)
    dane:
        * Adres email
        * Telefon
        * Adres
        * Link do instagrama

    Tips:
        1. Ugotuj zupę
    """
