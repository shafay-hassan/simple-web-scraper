from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page.content, "html.parser")
quotes = soup.find_all("div", class_="quote")

with open("web_scraper_data_output/quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["quote", "author"])

    for quote in quotes:
        text = quote.find("span", class_="text")
        author = quote.find("small", class_="author")
        if text and author:
            print(f"{text.text}\n - {author.text}\n")
            writer.writerow([text.text, author.text])

print("Saved quotes.csv")
