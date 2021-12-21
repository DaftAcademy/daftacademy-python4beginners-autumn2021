from dataclasses import dataclass

import bs4
import requests


@dataclass
class Contact:
    email: str
    phone: str
    address: str
    instagram: str


def get_daftcode_contact_info() -> Contact:
    r = requests.get("https://daftcode.pl/")

    soup = bs4.BeautifulSoup(r.text, "html.parser")

    email = soup.select_one(
        "#footer > div:nth-child(3) > div > div.col-lg-3.col-md-6.mb-50.footer__contact > div.footer__item.footer__item--e-mail > div.footer__item-link"
    ).text
    phone = soup.select_one(
        "#footer > div:nth-child(3) > div > div.col-lg-3.col-md-6.mb-50.footer__contact > div.footer__item.footer__item--telephone > div.footer__item-link > a"
    ).text

    address = soup.select_one(
        "#footer > div:nth-child(3) > div > div.col-lg-3.col-md-6.mb-50.footer__contact > div.footer__item.footer__item--address > div.footer__item-link > a"
    ).text

    instagram = soup.select_one(
        "#footer > div:nth-child(3) > div > div.col-lg-3.col-md-6.mb-50.footer__contact > div.footer__item.footer__item--social-media > div.social-links.mt-20.flex.flex--spread > a.social__icon.social__icon--instagram"
    )["href"]

    return Contact(email=email, phone=phone, address=address, instagram=instagram)


if __name__ == "__main__":
    print(get_daftcode_contact_info())
