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
print('Real-world HTML can be much more complicated and far less predictable than the HTML on the Aphrodite profile page. Here’s another profile page with some messier HTML that you can scrape:')
# %%
url = "http://olympus.realpython.org/profiles/poseidon"
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title
# %%
print('there seems to be something wrong with the title')
# %%
print('Extracting text from HTML using string methods')
title_index = html.find("<title>")
title_index
print('to get the index of the first character of the title we want to find the length using .len fucntion')
start_index = title_index + len("<title>")
start_index
print('Now get the index of the closing </title> tag by passing the string "</title>" to .find():')
end_index = html.find("</title>")
end_index
print('now we can extract the title by slicing the html string')
title = html[start_index:end_index]
title

# %%
print('Real-world HTML can be much more complicated and far less predictable')
url = "http://olympus.realpython.org/profiles/poseidon"
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title
# %%
print('getting to know regular expressions')
print('regexes for short')
print('are patterns that you can use to search for text within a string. Python supports regular expressions through the standard library’s re module.')
print('first thing to do is import the re model')
import re
print('Regular expressions use special characters called metacharacters to denote different patterns')
print('asterisk character (*) stands for zero or more instances of whatever comes just before the asterisk')
print('use .findall() to find any text within a string that matches a given regular expression')
re.findall("ab*c", "ac")
# %%
print('re.findall() is the regular expression that you want to match, and the second argument is the string to test. In the above example, you search for the pattern "ab*c" in the string "ac".')
print('regular expression "ab*c" matches any part of the string that begins with "a", ends with "c", and has zero or more instances of "b" between the two. re.findall() returns a list of all matches')
print('he string "ac" matches this pattern, so it’s returned in the list')
re.findall("ab*c", "abcd")


re.findall("ab*c", "acc")


re.findall("ab*c", "abcac")


re.findall("ab*c", "abdc")
print('if no match is found, then .findall() returns an empty list.')
# %%
print('Pattern matching is case sensitive. If you want to match this pattern regardless of the case, then you can pass a third argument with the value re.IGNORECASE:')
re.findall("ab*c", "ABC")


re.findall("ab*c", "ABC", re.IGNORECASE)
print('next we can command to find all the strings that contain specific letters')
re.findall("a.c", "abc")


re.findall("a.c", "abbc")


re.findall("a.c", "ac")


re.findall("a.c", "acc")
# %%
print('The pattern .* inside a regular expression stands for any character repeated any number of times')
print('you can use "a.*c" to find every substring that starts with "a" and ends with "c", regardless of which letter—or letters—are in between')
re.findall("a.*c", "abc")


re.findall("a.*c", "abbc")


re.findall("a.*c", "ac")


re.findall("a.*c", "acc")
# %%
print('re.search() to search for a particular pattern inside a string')
print('This function is somewhat more complicated than re.findall() because it returns an object called MatchObject that stores different groups of data')
print('because there might be matches inside other matches, and re.search() returns every possible result - so i guess you could say that using re.findall() is more specific')
print('calling .group() on MatchObject will return the first and most inclusive result, which in most cases is just what you want - this can increase the specificity of matches')
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()

# %%
print('useful for parsing out text. = re.sub(), = short for substitute, allows you to replace the text in a string that matches a regular expression with new text', 
      'It behaves sort of like the .replace() string method')
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
string
print('the outcome = 'Everything is ELEPHANTS.'')
print('re.sub() uses the regular expression "<.*>" to find and replace everything between the first < and the last >, which spans from the beginning of <replaced> to the end of <tags>')
# %%
print('Alternatively, you can use the non-greedy matching pattern *?, which works the same way as * except that it matches the shortest possible string of text:')
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
string
# %%
print('Extract Text From HTML With Regular Expressions')
< TITLE >Profile: Dionysus</title  / >

# %%
print('using regular expression can handel this code to best extract text from the html')
# regex_soup.py

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
# %%
print('break the string down into 3 parts:')
print('1. <title.*?> matches the opening <TITLE > tag in html. The <title part of the pattern matches with <TITLE because re.search() is called with re.IGNORECASE, and .*?> matches any text after <TITLE up to the first instance of >.')
print('2. .*? non-greedily matches all text after the opening <TITLE >, stopping at the first match for </title.*?>.')
print('3. </title.*?> differs from the first pattern only in its use of the / character, so it matches the closing </title  / > tag in html.')
