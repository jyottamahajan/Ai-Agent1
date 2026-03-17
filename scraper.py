import requests
from bs4 import BeautifulSoup

def scrape_aicte():

    url = "https://www.aicte-india.org/schemes/students-development-schemes"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    scholarships = []

    for link in soup.find_all("a"):

        title = link.text.strip()
        href = link.get("href")

# clean condition

        if not title or not href:
            continue

        # unwanted words (light filter)
        unwanted = [
            "Overview", "FAQ", "Read more", "Click here",
            "Guidelines", "Document"
        ]

        if any(word.lower() in title.lower() for word in unwanted):
            continue

        # important condition
        if "scheme" in title.lower() or "scholarship" in title.lower():

            # remove very short or generic titles
            if len(title.split()) < 2:
                continue

            # fix relative links

            if href.startswith("/"):
                href = "https://www.aicte-india.org" + href



            scholarships.append({
                "title": title,
                "link": href,
                "source": "AICTE"
            })

    return scholarships