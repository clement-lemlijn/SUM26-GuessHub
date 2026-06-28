from bs4 import BeautifulSoup
import requests
import json
import re

url = "https://www.pornhub.com/pornstars"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

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

cards = soup.select("li.performerCard, li.pornstarLi")

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
        "id": i + 1,
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

# SAVE JSON
with open("performers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ performers.json généré avec", len(data), "entrées")