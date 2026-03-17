# from scraper import scraper
# from sender import send_to_backend

# print("Agent Started...")

# data = scrape_aicte()

# print("Total Scholarships:", len(data))

# send_to_backend(data)

# print("All data sent to backend ✅")


import json
from scraper import scrape_aicte
from sender import send_to_backend

print("Agent Started...")

data = scrape_aicte()
print(f'Total Scholarships Scraped: {len(data)}')



for i in data:
    print(i)

# JSON file me save
with open("scholarships.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data saved successfully ✅")

# Backend me add karne ke liye
send_to_backend(data)