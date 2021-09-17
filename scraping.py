from selenium import webdriver
from bs4 import BeautifulSoup
# import panda as pd

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
url = '<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq'

driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    print(name)
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})