# %%
print('what is webscraping?') 
print(' it is the process of colleceting data from websites using an automated process known as web scraping') 
# %%
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
# %%
