from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

def gotoLink():
	elems = driver.find_elements_by_xpath("//a[@href]")
	link = random.choice([x.get_attribute("href") for x in elems])
	if "google" in link:
		driver.get("https://en.wikipedia.org/wiki/Main_Page")
	else: 
		driver.get(link)


while True:
	try:
		gotoLink()
	except:
		driver.get("https://en.wikipedia.org/wiki/Main_Page")

