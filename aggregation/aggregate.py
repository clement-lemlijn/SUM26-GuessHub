from bs4 import BeautifulSoup
import requests
import json
import time

BASE_URL = "https://www.pornhub.com/pornstars?page="

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_page(page):
    url = BASE_URL + str(page)
    print(f"Scraping page {page}")

    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")

    data = []

    for card in soup.select("li.performerCard"):
        img = card.select_one("img")
        link = card.select_one("a")

        if not img or not link:
            continue

        name = img.get("alt")
        image = img.get("src")
        profile = "https://www.pornhub.com" + link.get("href")

        data.append({
            "name": name,
            "image": image,
            "profile": profile
        })

    return data


all_data = []

MAX_PAGES = 5  # 👈 ajuste ici

for page in range(1, MAX_PAGES + 1):
    all_data.extend(scrape_page(page))
    time.sleep(1)  # anti-bot simple

with open("performers.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)

print("Done:", len(all_data))