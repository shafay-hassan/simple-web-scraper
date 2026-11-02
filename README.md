# 01-static-scraper-light — Month 1

What it does:
Scrapes open site that welcomes bots (quotes.toscrape.com), extracts quotes + authors using BeautifulSoup + requests, saves to structured CSV.

Imports used:
- from bs4 import BeautifulSoup
- import requests

Light Protocol:
- One session reused, 1 sec delay, don't crash site
- try/except for request fail
- Respects robots.txt

Run:
pip install -r requirements.txt
python web_scraper.py

Output:
data/quotes.csv

Stack: Python, BeautifulSoup, Requests
License: MIT
