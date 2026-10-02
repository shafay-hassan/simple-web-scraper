from bs4 import BeautifulSoup
import requests

page = requests.get("https://quotes.toscrape.com/")
access = BeautifulSoup(page.text, "lxml")

search = access.find_all("div", class_ = "quote")
with open("quotes.txt", "w", encoding="utf-8") as file:
        for quotes in search:
            text = quotes.find("span", class_ = "text")
            author = quotes.find("small", class_ = "author")
            print(text.text)
            print(author.text)
            print()