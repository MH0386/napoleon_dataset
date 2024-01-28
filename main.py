import requests
from bs4 import BeautifulSoup

# Specify the URL of the Wikipedia page you want to scrape
url = "https://en.wikipedia.org/wiki/Napoleon"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired text on the page (e.g., the first paragraph)
paragraph = soup.find_all('p')

all_text = "".join(p.text for p in paragraph)
import re


def remove_brackets(text):
    return re.sub(r'\[\w+\]', '', text)



print(remove_brackets(all_text))

'''
https://www.history.com/topics/european-history/napoleon
https://www.history.com/news/napoleon-exile-death
https://www.rmg.co.uk/stories/topics/napoleon-bonaparte#:~:text=Napoleon%20Bonaparte%20was%20one%20of,at%20military%20school%20in%20France.
https://www.britannica.com/biography/Napoleon-I/Exile-on-St-Helena
'''
