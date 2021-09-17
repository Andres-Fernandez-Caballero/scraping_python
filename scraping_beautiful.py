from datetime import time

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find("container")
titulo = soup.title.string
#print(titulo)
titulopagina = soup.h1.string
#print(titulopagina)

# results = soup.find(id="ResultsContainer")
# print(results)

jobs_elements = soup.find_all("div", class_="card-content")
# print(jobs_elements)

for job_element in jobs_elements:
    titulo = job_element.find("h2", class_="title")
    fecha = job_element.find('')
    print(titulo.string)

