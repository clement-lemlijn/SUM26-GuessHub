from bs4 import BeautifulSoup
import requests
import json
import re
import time

BASE_URL = "https://www.pornhub.com/pornstars?page="

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = []

def clean_int(text):
    if not text:
        return None
    match = re.search(r"\d+", text.replace(",", ""))
    return int(match.group()) if match else None

def clean_views(text):
    if not text:
        return None
    return text.replace("Views", "").strip()


page = 1
MAX_PAGES = 5   # 👈 ajuste ici (ou remplace par while True si tu veux auto-stop)

while page <= MAX_PAGES:

    print(f"Scraping page {page}...")

    url = BASE_URL + str(page)
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("li.performerCard, li.pornstarLi")

    # stop si page vide
    if not cards:
        print("No more data, stop.")
        break

    for i, card in enumerate(cards):

        img = card.select_one("img")
        name_el = card.select_one(".performerCardName, .pornStarName")
        link = card.select_one("a")

        videos_el = card.select_one(".videosNumber")
        views_el = card.select_one(".viewsNumber")
        rank_el = card.select_one(".rank_number")

        if not img or not name_el:
            continue

        name = name_el.get_text(" ", strip=True)
        slug = link["href"].split("/")[-1] if link else None

        item = {
            "id": len(data) + 1,   # 👈 ID global (important fix)
            "name": name,
            "slug": slug,
            "type": "pornstar" if "/pornstar/" in (link["href"] if link else "") else "model",
            "rank": int(rank_el.text.strip()) if rank_el else None,
            "videos": clean_int(videos_el.text) if videos_el else None,
            "views": clean_views(views_el.text) if views_el else None,
            "image": img.get("src"),
            "verified": bool(card.select_one(".verifiedIcon") or card.select_one(".verifiedPornstar")),
            "awards": ["Pornhub Awards Winner"] if card.select_one(".trophyPornStar") else []
        }

        data.append(item)

    page += 1
    time.sleep(1)  # anti-ban simple


# SAVE JSON
with open("performers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ performers.json généré avec", len(data), "entrées")