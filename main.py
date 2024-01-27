import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get('https://www.history.com/topics/european-history/napoleon')

# Parse the HTML content
soup = BeautifulSoup(r.text, 'html.parser')

# get the text of the html page
print(soup.get_text(separator='\n'))
