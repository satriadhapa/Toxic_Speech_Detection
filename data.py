import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as p
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.tokopedia.com/ptpratamasemesta/review'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)

data = []
for i in range(0, 100):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.findAll('article', attrs = {'class' : 'css-ccpe8t'})
    for container in containers:
        review = container.find('span', attrs = {'data-testid' :'lblItemUlasan'}).text()
        print(review)
        data.append(
            (review)
        )
    
    time.sleep(2)
    driver.find_element(By.CLASS_SELECTOR, "button[aria-label='Laman berikutnya']").click()
    time.sleep(3)

df = p.DataFrame(data, columns=['review'])
print(df)

driver.close()


