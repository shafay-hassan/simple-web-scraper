# simple-web-scraper

Light, ethical scraper that extracts quotes and authors from quotes.toscrape.com — an open site that welcomes bots. Built with a clean, respectful approach that doesn't overload the target site.

**Features:**
- Uses BeautifulSoup and requests with session reuse
- Handles request failures gracefully
- Structured CSV output

**Installation:**
pip install -r requirements.txt

**Usage:**
python web_scraper.py

**Output:**
`data/quotes.csv` — clean, structured data

**Stack:** Python, BeautifulSoup, Requests, lxml

**License:** MIT
