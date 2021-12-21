from dataclasses import dataclass
from typing import Set, Tuple

import requests


@dataclass
class HotShot:
    promotion_name: str
    promotion_total_count: int


def get_xkom_hotshot_product_data() -> HotShot:
    headers = {"x-api-key": "jfsTOgOL23CN2G8Y", "user-agent": "python"}

    r = requests.get(
        "https://mobileapi.x-kom.pl/api/v1/xkom/hotShots/current?onlyHeader=false&commentAmount=15",
        headers=headers,
    )

    data = r.json()

    return HotShot(
        promotion_name=data["PromotionName"],
        promotion_total_count=data["PromotionTotalCount"],
    )


def get_matching_keywords(name: str, keywords: Set[str]) -> Set[str]:
    lowered_name = name.lower()

    return {keyword for keyword in keywords if keyword.lower() in lowered_name}


def check_xkom_hotshot(keywords: Set[str]) -> Tuple[HotShot, Set[str]]:
    hot_shot = get_xkom_hotshot_product_data()
    matching_keywords = get_matching_keywords(hot_shot.promotion_name, keywords)

    return hot_shot, matching_keywords


if __name__ == "__main__":

    print(get_xkom_hotshot_product_data())

    print(get_matching_keywords("Telefon NoKia 3310", {"nokia", "sony"}))

    print(check_xkom_hotshot({"nokia"}))
