from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu "
                     "Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
driver = webdriver.Chrome('./webdrivers/chromedriver', options=options)

driver.get('https://accounts.thingiverse.com/')

user = 'lezzzca@gmail.com'
password = 'camaleon'

input_user = driver.find_element_by_id('username')
input_pass = driver.find_element_by_id('password')

input_user.send_keys(user)
input_pass.send_keys(password)

boton_login = driver.find_element_by_xpath('//*[@id="sso_sign_in"]')

boton_login.click()
