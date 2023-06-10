# Basic web scraper, returns HTML code from designated site.

from urllib.request import urlopen

# Retrieves HTML bytes
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

# Takes HTML bytes and turns it into readable code
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)

# Get HTML with string method. This extracts the <title> from the web page 
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)