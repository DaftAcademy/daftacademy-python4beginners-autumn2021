from typing import Set

import bs4
import requests


def get_recepie_links(keyword: str) -> Set[str]:
    query_params = {"search_api_views_fulltext": keyword}

    r = requests.get("https://www.kwestiasmaku.com/szukaj", params=query_params)

    soup = bs4.BeautifulSoup(r.text, "html.parser")

    recepie_list_element = soup.find_all(
        "div", {"class": "field field-name-title field-type-ds field-label-hidden"}
    )

    recepie_urls = {
        f"https://www.kwestiasmaku.com{recepie_element.find('a')['href']}"
        for recepie_element in recepie_list_element
    }

    return recepie_urls


if __name__ == "__main__":
    for k in ["placki", "ciasto", "kotlety", "schabowe"]:
        from pprint import pprint

        links = get_recepie_links(k)
        pprint(links)
        print(len(links))
