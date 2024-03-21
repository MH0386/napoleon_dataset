import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

pdfs = []
with open("napoleon_links.txt", "r", encoding="utf-8") as f:
    links = f.readlines()
    for i, link in enumerate(links):
        links[i] = link.replace("\n", "")
    m = 0
    n = 0
    for link in links:
        # check if it is a pdf
        if ".pdf" in link:
            pdfs.append(link)
            continue
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.get_text().split("\n"):
                with open(f"r/{m}.txt", "w", encoding="utf-8") as f:
                    f.write(a + "\n")
            m += 1
        except Exception as e:
            print(f"Error {e} at {link}")
    for link in pdfs:
        try:
            r = requests.get(link)
            pdf_reader = PdfReader(r.content)
            text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    text += text
            with open(f"r/pdf/{n}.txt", "w", encoding="utf-8") as f:
                f.write(text)
            n += 1
        except Exception as e:
            print(f"Error {e} at {link}")
