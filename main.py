import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get('')

# Parse the HTML content
soup = BeautifulSoup(r.text, 'html.parser')

# get the text of the html page
print(soup.get_text(separator='\n'))


'''
https://www.history.com/topics/european-history/napoleon
https://www.history.com/news/napoleon-exile-death
https://www.rmg.co.uk/stories/topics/napoleon-bonaparte#:~:text=Napoleon%20Bonaparte%20was%20one%20of,at%20military%20school%20in%20France.
'''