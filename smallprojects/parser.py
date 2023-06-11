import mechanicalsoup
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Basic scraping usage for beautifulsoup4
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())


# Basic scraping usage for MechanicalSoup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
print(page)
print(type(page.soup))
print(page.soup)


# Using MechanicalSoup for filling + submitting a form
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zues"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)