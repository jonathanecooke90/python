# Basic web scraper, returns HTML code from designated site.
import re
from urllib.request import urlopen

# Retrieves HTML bytes
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

# Takes HTML bytes and turns it into readable code
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)


# Scraping HTML with string method. This extracts the <title> from the web page 
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
# print(title)


# Scraping HTML with regex. This extracts the <title> from the page, but correctly.
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()

# Removes HTML tags
title = re.sub("<.*?>", "", title)
print(title)
