import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('./webdrivers/chromedriver')
driver.get('https://www.olx.com.ec/autos_c378')

driver.set_page_load_timeout(45)
# driver.minimize_window()
driver.implicitly_wait(2)

boton_cargarmas = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for carga in range(5):
    try:
        boton_cargarmas.click()
        sleep(random.uniform(8.0, 10.0))
        boton_cargarmas = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

print('Lista de autos')
for auto in autos:
    price = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text

    print(price)
    print(descripcion)
driver.close()