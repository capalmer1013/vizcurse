import requests
from bs4 import BeautifulSoup
import time
import sys

def scroll_text(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


url = "https://en.wikipedia.org/wiki/Special:Random"

while True:
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    scroll_text(soup.find(id="bodyContent").get_text())


