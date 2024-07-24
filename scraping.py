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
print('The output that you’re seeing is the HTML code of the website')
# %%
title_index = html.find("<title>")
title_index
start_index = title_index + len("<title>")
start_index
end_index = html.find("</title>")
end_index
title = html[start_index:end_index]
title
# %%
