import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

pdfs = []
links_err = []
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
            soup = BeautifulSoup(r.text, "lxml")
            text = soup.get_text()
            with open(f"r/html/{m}.txt", "w", encoding="utf-8") as f:
                f.write(text)
            m += 1
            print(m)
        except Exception as e:
            print(f"Error {e} at {link}")
            links_err.append(link)
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
            links_err.append(link)
    with open("links_err.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(links_err))
