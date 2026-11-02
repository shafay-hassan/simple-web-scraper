# 01-static-scraper-light — Month 1

What it does:
Scrapes open site that welcomes bots (quotes.toscrape.com), extracts quotes + authors, saves to CSV — light + ethical, same pattern for B2B.

Protocol:
- One page reused, block png/jpg/jpeg before goto
- domcontentloaded lowercase, 1 sec delay, don't crash site
- try/finally close inside with, real bot UA

Run:
pip install -r requirements.txt
python web_scraper.py

Output: data/quotes.csv

Stack: Python, BeautifulSoup

License: MIT
